# AGENTS.md

Owner: `evento-globolo`  
Tracking: `DEN-1889`

Preserve the responsive Astro product site, product-specific event-platform copy, existing production build and test scripts, configured GitHub Pages URL, SEO metadata, and deployment behavior. Do not replace working product content with a placeholder or generic template.

Before proposing changes, run:

```bash
npm test
npm run build
python3 scripts/verify_repo.py
```

Use focused pull requests, preserve public URLs and interface compatibility, add tests with behavior changes, never commit credentials or customer data, and resolve conflicts semantically using both sides and the relevant history.
