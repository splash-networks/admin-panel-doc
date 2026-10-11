# CLAUDE.md

Documentation portal for **Splash Air** (Splash Networks' captive portal / guest Wi-Fi admin panel), published at https://docs.splashnetworks.co. Built with MkDocs + Material theme and deployed to GitHub Pages.

## Commands

```bash
pip install mkdocs mkdocs-material mkdocs-glightbox   # setup
python -m mkdocs serve                                # live preview at http://127.0.0.1:8000
python -m mkdocs build --strict                       # catch broken links / missing nav pages
```

`site/` is local build output (untracked) — never edit or commit it.

## Deployment

Pushing to `main` triggers `.github/workflows/mkdocs.yml`: `mkdocs gh-deploy` builds to the `gh-pages` branch, deploys it to Pages, then posts a Discord notification. There is no staging — anything merged to `main` goes live, so verify locally with `mkdocs serve` first. If you add a new MkDocs plugin, also add it to the `pip install` step in the workflow.

## Layout

- `mkdocs.yml` — site config and the **explicit `nav`**. New pages must be added to `nav` or they won't appear in the sidebar. Nav placement is independent of file location: `docs/api.md` is listed under "Accessing Customer Data" but stays at the root so its URL remains `/api/`.
- `hooks.py` — MkDocs hook that sets the copyright year dynamically; don't hardcode the year.
- `docs/*.md` — top-level feature pages (plans, vouchers, automations, surveys, RADIUS, walled garden, etc.).
- `docs/portals/<vendor>.md` — one hardware integration guide per vendor (Omada, UniFi, Meraki, Mikrotik, Ruckus, …). Nav is alphabetical by display name.
- `docs/assets/images/<section>/[<vendor>/]<name>.png` — screenshots, mirroring the page structure (e.g. `assets/images/portals/omada/portal.png`).
- `docs/files/api.json` — OpenAPI spec rendered by Scalar on `docs/api.md`. It is **auto-updated by commits from the `splash-networks/admin-panel` repo** ("chore: update API spec …") — don't hand-edit it.

## Writing conventions

- Pages start directly with content or `##` headings; the page title comes from `nav`, so most pages have no `#` H1.
- Use relative links between pages (`../defining-templates.md`, `../walled-garden.md`) and relative image paths. Pages in `docs/` use `assets/images/...`; pages in subfolders use `../assets/images/...`.
- Images: `![Alt Text](path.png)`. Glightbox makes them click-to-zoom. To resize/center, wrap in a figure:
  ```html
  <figure markdown="span">
    ![Access Control](../assets/images/portals/omada/access-control.png){ width="80%" }
  </figure>
  ```
- UI navigation paths are written plainly: `Settings > Authentication > Portal`. Field/option names in **bold**, literal values in `` `code` ``.
- Copyable values use fenced blocks with `{ .copy }`; settings lists use plain fenced blocks (see portal "Portal Settings" sections).
- Support tables use `:material-check:` / `:material-close:` icons.
- Product terms are capitalized as in the app: Splash Air, Portal, Template, Venue, Business, and Flow types (Simple / OTP / Link / Payment / Voucher Flow).
- Second person, short imperative steps (Microsoft Writing Style Guide is a good reference). There is no automated spell check, so proofread carefully.

## Vendor portal guide structure

Portal pages follow a common pattern — keep new vendor guides consistent with existing ones (`docs/portals/omada.md` is a good reference):

1. Prerequisite link to [create a template](../defining-templates.md)
2. `## Add a Portal` — steps in Splash Air (controller/portal creation, Guest Portal URL)
3. `## Portal Settings` — portal detail fields
4. `## <Vendor> Controller Settings` — RADIUS profile, external portal URL, pre-auth/walled garden entries
5. `## Troubleshooting` (optional) — traffic flow diagram, common issues

When adding a vendor, also update the hardware support table(s) in `docs/defining-templates.md` (Link Flow / dynamic session extension / voucher compatibility).
