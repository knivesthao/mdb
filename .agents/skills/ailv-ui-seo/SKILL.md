---
name: ailv-ui-seo
description: "The best page is the one people actually find — humans through search, agents through the map."
sources:
  - title: Google Search Essentials
    url: https://developers.google.com/search/docs/essentials
  - title: Sitemaps.org
    url: https://www.sitemaps.org/protocol.html
  - title: Google Trends
    url: https://trends.google.com/trends/
helper: scripts/helper.py
example: examples/output.md
---

# Be findable

`ailv-ui-seo` (Be findable): Every public page earns its visitors: one H1, a plain-words title under 60 characters, a meta description under 160 characters, semantic landmarks (header, main, footer), and real links — never JavaScript-only navigation. Ship a sitemap.xml listing every public page and name it in robots.txt; keep llms.txt current so agents find the machine doors too. Meeting every requirement earns eligibility, never a guarantee — engines still choose what to crawl and serve. Keep money behind the wall: premium content, checkout, billing, and account pages carry noindex and stay out of the sitemap — crawlers earn the free pages, never the paid ones. Keep pages light so they load fast on phones. Before adding a page or skill, check Google Trends for what people actually search — build where demand already exists, not where you guess it.

## Checks

- one H1 plus meta title and description per page
- sitemap lists public pages only, paid pages noindexed
- Trends checked before new pages
