# nimishhomelab

Static portfolio site for [nimishhomelab.com](https://nimishhomelab.com/).

The site is a small multi-page portfolio for recruiter and technical hiring-manager review. It now combines:

- one current professional role summary
- security infrastructure project work, including the SIEM HomeLab through Part 3
- security data analysis project work
- one shipped software example
- supporting security training evidence from TryHackMe

There is no framework, package manager, or build step. The site is plain HTML and CSS.

## Current structure

- `index.html` is the homepage.
- `projects/wazuh/index.html` is the SIEM HomeLab case study for Wazuh Indexer, Wazuh Dashboard, and Graylog Server.
- `projects/malicious-url-detection/index.html` is the malicious URL classification case study.
- `assets/site.css` contains the shared visual system for all pages.
- `assets/Nimish-Sood-Resume.pdf` is the public resume asset linked from the homepage.
- `scripts/generate_resume_pdf.py` rebuilds the resume PDF from a text-based source.
- `404.html` is the custom not-found page.
- `_headers` defines cache and security headers for static hosts that support that format.

## Portfolio direction

The current homepage is organized around:

- current professional experience at AKA Energy Systems
- public project evidence from the SIEM HomeLab and malicious URL case studies
- one shipped application with a public repo and deployment
- supporting security training evidence from TryHackMe
- direct resume and contact access

The site avoids portfolio-strategy language and keeps the copy focused on scope, artifacts, status, and limitations.

Employer work is summarized with public-safe detail only. Public projects remain separate from professional work.
The SIEM HomeLab case study reflects the public repo through Part 3: Wazuh Indexer, Wazuh Dashboard, and Graylog Server.

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
- edit SIEM HomeLab case study in [projects/wazuh/index.html](/C:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/projects/wazuh/index.html)
- edit malicious URL case study in [projects/malicious-url-detection/index.html](/C:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/projects/malicious-url-detection/index.html)
- edit shared styling in [assets/site.css](/C:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/assets/site.css)
- edit the resume source in [scripts/generate_resume_pdf.py](/C:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/scripts/generate_resume_pdf.py) and rebuild [assets/Nimish-Sood-Resume.pdf](/C:/Users/Nimish/Desktop/nimishhomelab/nimishhomelab/assets/Nimish-Sood-Resume.pdf)

Fonts are loaded from Google Fonts. There is no CSS build pipeline.

## Verification checklist

After edits, verify:

- homepage loads without broken styles
- both case-study routes return `200`
- resume link works
- navigation anchors still point to live homepage sections
- `_headers` still matches the intended indexing and cache behavior
