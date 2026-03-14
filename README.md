# nimishhomelab

Personal portfolio site for [nimishhomelab.com](https://nimishhomelab.com/).

This project is a single-page static site that presents Nimish Sood's work in cybersecurity, homelab infrastructure, applied ML, and software projects. It is built with plain HTML and CSS, with no framework, build step, or package manager.

## What is in this repo

- `index.html` contains the full landing page, layout, content, and styles.
- `404.html` provides a simple fallback page for unknown routes.
- `_headers` defines security and caching headers for hosts that support that file format.

## Site sections

The homepage includes:

- an intro and contact links
- a featured projects section
- homelab infrastructure details
- AI and ML work
- self-hosted service links

## Running locally

Because this is a static site, you can open `index.html` directly in a browser.

If you want a local server instead, run one from the project folder. For example:

```powershell
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deployment notes

This repo is set up like a simple static hosting deployment:

- `index.html` is the main entry point
- `404.html` handles missing pages
- `_headers` adds security-related response headers and cache rules where supported

The `_headers` file currently includes policies such as:

- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy: no-referrer`
- `Permissions-Policy` restrictions
- `Strict-Transport-Security`

## Editing the site

To update the content or design, edit [index.html](/c:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/index.html). Fonts are loaded from Google Fonts, and the styling is embedded directly in the page.

## Domain and purpose

The site is intended to act as a public portfolio and technical landing page for:

- cybersecurity and SIEM work
- homelab and self-hosting projects
- applied ML and local LLM experiments
- co-op, internship, and project opportunities
