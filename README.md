# SpheresX Website

Complete HTML, CSS and JavaScript website with Python source generator.

## Upload to GitHub

1. Extract this ZIP and open the inner **SpheresX-Website** folder.
2. Create a repository named `spheresx-website` in your own GitHub account.
3. Upload this folder's contents, preserving `docs/` and `scripts/` at the repository root. Do not upload the ZIP itself. GitHub Desktop is an easy option for uploading all files at once.
4. In the repository go to **Settings → Pages**.
5. Select **Deploy from a branch**, branch **main**, folder **/docs**, then **Save**.
6. GitHub displays the published URL after deployment. A project repository normally uses `https://YOUR-USERNAME.github.io/spheresx-website/`.

A public repository can be used with GitHub Free. Publishing it makes your website and source publicly accessible.

Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Preview locally

From this folder:

```bash
python3 -m http.server 8000 --directory docs
```

Open http://localhost:8000 . Press Ctrl+C to stop.

## Edit the website

- `docs/`: ready-to-publish pages and assets. Direct edits work, but rebuilding overwrites generated pages.
- `scripts/build-pages.py`: page generator and shared navigation, footer, styling and JavaScript.
- `scripts/home-template.html`: original homepage source.
- `scripts/projects.json`: portfolio data.
- `scripts/reviews.json`: attributed recommendation excerpts and summaries.
- `scripts/blog-articles.json`: additional blog articles. The initial three articles are in the generator.
- `docs/assets/spheresx-logo-hires.png`: high-resolution logo reconstructed from the supplied screenshot.

After source edits, regenerate:

```bash
python3 scripts/build-pages.py
```

Python uses its standard library only. No npm install is needed. Commit the updated `docs/` folder to publish changes.

## Current functionality

Project and blog filters, mobile navigation, screenshot viewer, separate service/project/blog pages, and email/WhatsApp/telephone links. The inquiry form opens an email client; it does not submit to a server. There is no database or admin dashboard. Store and video links use external services. Recommendation sources link to the founder's portfolio; there are no Google ratings.

The exported links work with both a repository subpath and a custom domain. This download contains no ChatGPT hosting credentials, Git history or private deployment configuration.

## Production SEO

The build generates canonical URLs for `https://spheresx.com/`, Open Graph metadata,
Organization/WebSite/WebPage/BreadcrumbList JSON-LD, `docs/robots.txt`, and
`docs/sitemap.xml`. Legacy `insights` pages canonicalize to the equivalent blog
pages; the 404 page is excluded from indexing. Change `SITE` in `scripts/seo.py`
before deploying to a different production domain. Preview copies retain the
production canonical URLs intentionally.

To release, deploy the contents of `docs/` through the site's existing hosting
configuration. Verify `/sitemap.xml` returns XML with HTTP 200 and check the live
homepage source for its canonical link and JSON-LD. Cloudflare's managed robots
feature may add text; confirm the live response includes the sitemap directive
and does not block Googlebot.

After deployment, verify ownership of `spheresx.com` in Google Search Console
(a Domain property uses a DNS TXT record supplied by Google). Submit
`https://spheresx.com/sitemap.xml` under Sitemaps, inspect the homepage URL,
and request indexing. Use Google's Rich Results Test to check the live markup.
Watch Search Console impressions and clicks for the SpheresX query over time.
Neither metadata nor sitemap submission guarantees indexing or a top ranking.

For a Google Business Profile, confirm the business meets customers in person
at its office or at customer locations. Online-only businesses are ineligible.
Claim an existing listing instead of creating a duplicate, verify ownership,
and add the real business name, website, phone, address/service area, hours,
logo and genuine photos. Keep details consistent with the website. No street
address or opening hours have been invented in this build.

Google reviews must be submitted by real customers through their own Google
accounts. Once the profile exists, obtain its review link from “Get more reviews”.
The existing founder recommendations remain attributed portfolio testimonials;
they have not been converted into Google reviews or fabricated star ratings.
Google decides whether a knowledge panel or other search features appear.

Official references:
- https://developers.google.com/search/docs/appearance/structured-data/organization
- https://developers.google.com/search/docs/appearance/establish-business-details
- https://support.google.com/business/answer/13763036
- https://support.google.com/business/answer/16816815
