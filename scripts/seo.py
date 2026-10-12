"""Generate production search metadata for the static SpheresX website."""
import html
import json
import re
from xml.etree import ElementTree as ET

SITE = 'https://spheresx.com'
LOGO = SITE + '/assets/spheresx-logo-hires.png'


def canonical_url(path):
    if path == 'index.html':
        return SITE + '/'
    # Legacy insight pages reproduce blog content; consolidate search signals.
    if path == 'insights.html':
        path = 'blog.html'
    elif path.startswith('insights/'):
        path = 'blog/' + path.split('/', 1)[1]
    return SITE + '/' + path


def apply_seo(dist):
    urls = []
    for page in sorted(dist.rglob('*.html')):
        path = page.relative_to(dist).as_posix()
        source = page.read_text()
        title = html.unescape(re.search(r'<title>(.*?)</title>', source).group(1))
        if path == 'index.html':
            title = 'SpheresX | Web, Mobile & AI Development in Lahore'
            source = re.sub(r'<title>.*?</title>', '<title>' + html.escape(title) + '</title>', source)
        description = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', source).group(1))
        url = canonical_url(path)
        metadata = [
            f'<link rel="canonical" href="{url}">',
            '<link rel="icon" type="image/png" href="' + LOGO + '">',
            '<meta name="robots" content="' + ('noindex,follow' if path == '404.html' else 'index,follow,max-image-preview:large') + '">',
        ]
        for key, value in {
            'og:type': 'website', 'og:site_name': 'SpheresX', 'og:locale': 'en_PK',
            'og:title': title, 'og:description': description, 'og:url': url,
            'og:image': LOGO, 'og:image:alt': 'SpheresX — software development company',
        }.items():
            metadata.append(f'<meta property="{key}" content="{html.escape(value, quote=True)}">')
        for key, value in {'twitter:card': 'summary', 'twitter:title': title,
                           'twitter:description': description, 'twitter:image': LOGO}.items():
            metadata.append(f'<meta name="{key}" content="{html.escape(value, quote=True)}">')
        graph = []
        if path == 'index.html':
            graph.extend([
                {'@type': 'Organization', '@id': SITE + '/#organization',
                 'name': 'SpheresX', 'alternateName': 'Spheresx', 'url': SITE + '/',
                 'description': description, 'logo': LOGO,
                 'email': 'mobile.appdevu@gmail.com', 'telephone': '+923074460609',
                 'address': {'@type': 'PostalAddress', 'addressLocality': 'Lahore', 'addressCountry': 'PK'},
                 'sameAs': ['https://www.linkedin.com/company/spheresx/']},
                {'@type': 'WebSite', '@id': SITE + '/#website', 'name': 'SpheresX',
                 'alternateName': 'Spheresx', 'url': SITE + '/',
                 'publisher': {'@id': SITE + '/#organization'}},
            ])
        if path != '404.html':
            graph.append({'@type': 'WebPage', '@id': url + '#webpage', 'url': url,
                          'name': title, 'description': description,
                          'isPartOf': {'@id': SITE + '/#website'},
                          'about': {'@id': SITE + '/#organization'}, 'inLanguage': 'en'})
            if path != 'index.html':
                crumbs = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}]
                if '/' in path:
                    section = path.split('/')[0]
                    section = 'blog' if section == 'insights' else section
                    crumbs.append({'@type': 'ListItem', 'position': 2, 'name': section.title(), 'item': SITE + '/' + section + '.html'})
                crumbs.append({'@type': 'ListItem', 'position': len(crumbs) + 1,
                               'name': title.removesuffix(' | SpheresX'), 'item': url})
                graph.append({'@type': 'BreadcrumbList', 'itemListElement': crumbs})
        if graph:
            encoded = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('<', '\\u003c')
            metadata.append('<script type="application/ld+json">' + encoded + '</script>')
        page.write_text(source.replace('</head>', ''.join(metadata) + '</head>', 1))
        if path != '404.html' and path != 'insights.html' and not path.startswith('insights/'):
            urls.append(url)

    namespace = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('', namespace)
    sitemap = ET.Element('{' + namespace + '}urlset')
    for url in urls:
        entry = ET.SubElement(sitemap, '{' + namespace + '}url')
        ET.SubElement(entry, '{' + namespace + '}loc').text = url
    ET.ElementTree(sitemap).write(dist / 'sitemap.xml', encoding='utf-8', xml_declaration=True)
    (dist / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + SITE + '/sitemap.xml\n')
    print('SEO metadata generated; sitemap contains', len(urls), 'canonical pages')
