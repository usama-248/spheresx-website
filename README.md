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
