# evento-globolo.github.io

Marketing, documentation, privacy, support, and public integration guidance for Evento Globolo.

Initialized through `DEN-1889` as a testable `marketing` foundation. Product behavior continues through focused pull requests.

The complete native Astro document lives at `src/pages/index.astro`. GitHub Pages publishes only its tested `dist/` artifact.

```bash
npm ci --ignore-scripts
npm test
npm run build
python3 scripts/verify_repo.py
```
