# Marketing-site architecture

`evento-globolo.github.io` is the public Astro marketing and documentation surface for Evento Globolo. The existing responsive product site, channel-specific narrative, SEO, build/test scripts, and GitHub Pages configuration are canonical and must be evolved in place rather than replaced by a bootstrap placeholder.

## Fleet relationships

- `evgl-interfaces` owns OpenAPI, AsyncAPI, JSON Schema, event, and provider contracts.
- `evgl-api`, `evgl-mash-web`, `evgl-leptos-web`, and `evgl-dioxus-web` own runtime behavior.
- `evgl-sync` owns offline-first event, attendee, venue, and publication synchronization.
- `evgl-cli` owns operator workflows through flags-2-env.
- `evgl-infra` owns deployment, observability, and bounded Cloudflare Worker behavior.
- `evento-globolo-clients` and `evento-globolo-libs` own typed consumption and reusable domain logic.
- `evento-globolo.github.io` owns the public product narrative and integration guidance.
- `evento-globolo-monorepo` coordinates pinned revisions and cross-repository compatibility.

The marketing site may explain and link versioned contracts but must not duplicate service logic or become a generic edge proxy. Public copy, accessibility, performance, and stable URLs are product behavior and require review and tests.
# Architecture

Marketing, documentation, privacy, support, and public integration guidance for Evento Globolo.

## Fleet

- `evgl-interfaces`
- `evgl-api`
- `evgl-mash-web`
- `evgl-leptos-web`
- `evgl-dioxus-web`
- `evgl-sync`
- `evgl-cli`
- `evgl-infra`
- `evento-globolo-clients`
- `evento-globolo-libs`
- `evento-globolo.github.io`
- `evento-globolo-monorepo`

Interfaces own wire formats; libraries own reusable domain behavior; clients consume versioned contracts; runtimes own deployment behavior; monorepos coordinate pinned revisions. Edge code is allowlisted and never a generic proxy.
