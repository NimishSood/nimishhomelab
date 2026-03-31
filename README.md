# nimishhomelab

Static portfolio site for [nimishhomelab.com](https://nimishhomelab.com/).

The site is now a small multi-page portfolio built for recruiter and technical hiring-manager review. It is intentionally security-first: the main proof points are a Wazuh homelab, a malicious URL detection project with saved metrics, and one shipped software project.

There is no framework, package manager, or build step. The site is plain HTML and CSS.

## Current structure

- `index.html` is the homepage.
- `projects/wazuh/index.html` is the Wazuh homelab case study.
- `projects/malicious-url-detection/index.html` is the malicious URL detection case study.
- `assets/site.css` contains the shared visual system for all pages.
- `assets/Nimish-Sood-Resume.pdf` is the public resume asset linked from the homepage.
- `404.html` is the custom not-found page.
- `_headers` defines cache and security headers for static hosts that support that format.

## Portfolio direction

This repo no longer presents the portfolio as a broad “student does everything” site.

The current content is organized around:

- security infrastructure evidence
- security data analysis evidence
- one compact shipped-product example
- direct contact and resume access

AI/LLM work is intentionally kept secondary as an experiments note rather than a main portfolio pillar.

Unstable homelab service links were removed from the public site. The public proof path is now documentation, repo artifacts, diagrams, and saved results rather than uptime-dependent endpoints.

## Running locally

Because this is a static site, you can preview it with any basic static file server.

Example:

```powershell
python -m http.server 8000
```

Then open:

- `http://localhost:8000/`
- `http://localhost:8000/projects/wazuh/`
- `http://localhost:8000/projects/malicious-url-detection/`

## Deployment notes

This repo is structured for simple static hosting.

- `index.html`, the case-study routes, and `404.html` are served as static HTML.
- `assets/` is cacheable static content.
- `_headers` applies security headers and cache policy where supported by the host.

The current `_headers` file is aligned with the HTML metadata:

- public pages are not marked `noindex, nofollow`
- static assets are cacheable
- security headers remain enabled

## Editing the site

Common update points:

- edit homepage content in [index.html](/C:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/index.html)
- edit Wazuh case study in [projects/wazuh/index.html](/C:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/projects/wazuh/index.html)
- edit malicious URL case study in [projects/malicious-url-detection/index.html](/C:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/projects/malicious-url-detection/index.html)
- edit shared styling in [assets/site.css](/C:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/assets/site.css)
- replace the resume asset in [assets/Nimish-Sood-Resume.pdf](/C:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/assets/Nimish-Sood-Resume.pdf)

Fonts are loaded from Google Fonts. There is no CSS build pipeline.

## Verification checklist

After edits, verify:

- homepage loads without broken styles
- both case-study routes return `200`
- resume link works
- `_headers` still matches the intended indexing and cache behavior
- no dead public demo links were added accidentally
