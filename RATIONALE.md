# Farsight Africa Group: website concept

Concept by TheCompany.design. **Not approved by Farsight. Do not publish.** The page carries a "concept" bar at the top, a `noindex` tag and a concept line in the footer.

Open `index.html`, or run the `farsight` server in `.claude/launch.json` (port 4176). Pages are generated: edit `build.py` (inner pages) or `src/home.html` (homepage body), then run `python build.py`.

## Audience
Government officials, UN and donor procurement officers, and corporate partners, often on a phone. They are checking five things: is this firm legitimate, has it worked for institutions like mine, who runs it, where is it, and how do I reach it. The page answers those questions in that order.

## The three biggest decisions

1. **Proof goes in the hero, not a stock photo.** The space where the current site has a photo now holds a "Selected engagements" card: the Liberia Revenue Authority, Somalia's Planning Ministry (NDP-9), UNICEF Somalia and the AU/UN Information Support Team, with the years each page states. The client logo wall sits directly underneath. A procurement officer sees institutional credentials on the first screen, with no scrolling and no dropdowns.
2. **A publication tone instead of a corporate template.** A serif headline (Source Serif 4) with a plain sans body (Public Sans). The page is mostly light, with one navy section and generous whitespace. The colours were sampled from the logo file (navy `#263a6e`, blue `#0b7ac2`) and the site's map (orange `#f68523`). Orange is decorative only, because it fails contrast as small text on white. The visuals use the live site's own photos and icons, alongside document-style cards and a simple map drawn from public boundary data.
3. **One tap to make contact, everywhere.** Phone numbers use `tel:` and email uses `mailto:` in the mobile menu, the offices section, the contact section and the footer. The enquiry form validates every field. Because there is no backend, the page says so and opens the visitor's email app with the message filled in. It never shows a fake "sent".

Services are written as one-line definitions so the difference is clear at a glance. Public Sector Advisory is advice to government; Strategic Communication is reaching the public.

## [CONFIRM] placeholders (visible on the page)
- Monrovia office phone number (the live site lists none).
- WhatsApp number, and who answers it.
- Response time for enquiries (none is promised).

## Assets copied from the live site
All original files are in `assets/live/`, with web-optimised copies in `assets/img/`.

Used on the homepage:
- **Hero:** `banner-1.jpg`, the live hero photo, framed beside the engagements card.
- **Services:** `services-1` to `services-4.jpg`, paired with the same services as on the live homepage.
- **Sectors:** `icon-1` to `icon-3.png`.
- **Leadership:** the three real portraits from /about-us/leadership-team/.
- **Technology & Innovation:** the Hornswitch logo, plus one sentence from that service page.
- **Favicon:** `favicon.png`.

Copied but not used on the homepage, kept for the later service pages:
- `inner-banner.jpg`
- the diagrams `overview.png`, `comm.png`, `non-tax.png` and `non-tax-1.png`
- the ITAS module screenshot

**Trade-off:** the hero and service images are stock photos. Part A of the brief calls the stock people photo the weakest part of the current homepage. They are used here because the designer asked for the live assets, and each one is a single file to swap once Farsight supplies real field or event photos.

## Content assumptions and notes
- All copy comes from live pages on farsightafrica.com, read on 20 Nov 2026, and is trimmed without changing meaning. Testimonials are copied word for word and attributed by organisation logo only, as the site does: M&C Saatchi, UNICEF, UNSOS.
- Case-study years ("February 2021 – Ongoing", 2020, 2019, 2014–2019) come from the individual case-study pages.
- The logo wall has 13 logos, cut from the site's single `clients.jpg`. They are low resolution, so ask Farsight for vector files. Also confirm they are comfortable showing these logos in a concept shared outside the company.
- Countries of practice come from the live map image: Kenya, Somalia, South Sudan, Liberia, The Gambia, Morocco, UAE. The new map treats Somalia and Somaliland as one highlighted area, with no internal border drawn. The Gambia is too small to see at this scale, but it is in the text list.
- Leadership shows senior management only. The Advisory Board (Steve Turner) is reached through the "Full leadership team" link.
- Bios are shortened from /about-us/leadership-team/.
- No founding year, staff count, project count or country count is stated anywhere.
- Fonts load from Google Fonts. Boundary data for the map: world-atlas 2.0.2 (Natural Earth, public domain).

## Checks run
- Captured at 360, 390, 768, 1280 and 1920px (`screenshots/`, a hero view and a full page at each width). No horizontal scroll at any width, and the hero headline never clips.
- One H1, no broken images, no console errors.
- All 15 links to farsightafrica.com return 200.
- Mobile menu opens, moves focus, closes on Escape and returns focus to the button. Every interactive element is at least 44px tall.
- Form validation tested: empty fields, then an invalid email. Errors appear and focus moves to the first bad field.
- Reveal animations are off under `prefers-reduced-motion`.

## Full site (phase 2)

There are 18 pages, keeping the live URL structure:
- **Home**
- **About:** Get to Know Us; Mission, Vision & Culture; Farsight Unique Profile; Leadership Team; Press Release
- **Services:** Service Overview, plus the four service pages
- **Clients & Case Studies:** Clients; Case Studies; the four case-study pages, at their original dated URLs
- **Contact Us**

**Structure decisions**
1. **Shared header with dropdowns.** About, Services and Clients & Case Studies open keyboard-operable dropdowns: Escape closes them and returns focus to the button. On phones, a single menu lists every page, grouped by section, with call and email buttons.
2. **Section sub-navigation.** About and Services pages carry a sticky row of links to their sibling pages, replacing the live site's sidebar.
3. **Service pages are long-form, not tabbed.** The live tabs became sections with a sticky "On this page" list that highlights where you are. Content stays readable on a phone and findable by search. The service diagrams sit inside the sections they explain, and each opens full size.
4. **Case studies are documents.** Each has a facts panel (client logo, client, country, implementation dates, linked services), the project summary, the Farsight manager's comment as a pull quote, the outcome where the page states one, and links to the other case studies.
5. **Every inner page ends with a short call-to-action band** linking to the enquiry form and the Nairobi phone number.

**Content notes for the full site**
- All copy comes from the live pages. Obvious typos and grammar slips are corrected without changing meaning, for example "pleases" to "pleased", "advice" to "advise" and "will developing" to "will develop".
- "Since our establishment in 2010" appears on the live Get to Know Us page, so it is used there and in that page's facts panel. It is not used on the homepage.
- The Advisory Board (Steve Turner, Joel Gachomo, George Nyabuga) has no photos on the live site, so their cards use initials.
- The press release PDF is copied to `assets/docs/` and linked as a download.
- The contact page links to Google Maps rather than embedding it, so no third-party script loads.
- The NDP-9 case study links to its two YouTube mini-documentaries, as the live page does.

**More [CONFIRM] placeholders**
- Advisory Board photos (three).
- Press release date and a one-line summary.

**Checks run on all 18 pages**
- Every page at 360, 390, 768, 1280 and 1920px: no horizontal scroll, exactly one H1, no broken images, no console errors, no duplicate IDs, and no tap targets under 32px.
- A crawl from the homepage over HTTP reaches all 18 pages and 62 files, with no errors.
- Dropdowns tested with a real mouse and keyboard.
- Full-page screenshots of every page at 390 and 1280px are in `screenshots/site/`.

## Revision: more premium, cleaner, less wordy (20 Nov 2026)

This revision followed the request to make the site "more premium and clean, also less wordy especially the header".

**Homepage**
- **Hero:** now only the headline, one line ("Advisory and implementation for government, business and development."), two buttons and the photo. The "Selected engagements" card and the office list are gone, and proof now starts with the client logos directly below.
- **Client logos:** cut to 8, with a link to all clients. The full wall of 13 is on the Clients page.
- **Services:** four photo tiles, each with a one-line description.
- **Case studies:** a short list of client, short project name and year. The full official titles are on the case-study pages.
- **Shorter sections:**
  - Sector blurbs are one sentence each.
  - "Why Farsight" became five short lines.
  - Leadership shows name and title only.
  - The contact block is just the email and phone numbers.
- **Unchanged:** the testimonials are still quoted word for word.

**Inner pages**
- Page headers drop the label above the title and use a one-line intro, or none.
- Case cards drop their summaries.
- Call-to-action bands drop their supporting sentence.
- The concept bar, form note and careers line are shorter.

**Styling**
- Headings use the regular (400) weight.
- There's more space between sections.
- The orange markers on section labels are gone.
- Quotes are no longer in cards.
- Paired form fields sit side by side.
- The Monrovia map label moved so it isn't clipped.

**Short labels written for this revision:** these are summaries of live-site copy, not new claims. For example "Tax, revenue and information systems for government" and "Information Support Team communications".

**Placeholder changes:** the press release now asks Farsight to confirm only its date. The one-line summary was dropped from that [CONFIRM].

## Redesign: dark & cinematic (20 Nov 2026)

After the cleaner light version, the designer said the overall design still felt plain and flat, and chose the "Dark & cinematic" direction.

**What changed**
- **Colour:**
  - A deep navy field (`#0f1730`, darkened from the brand navy) for the header, hero, case studies, the "Why Farsight" statement, offices, the call-to-action bands and the footer.
  - Crisp white and pale grey sections in between, so the page alternates dark and light.
  - Orange is kept for the main button, thin rules and the map pins.
- **Hero:**
  - A large white serif headline with an orange rule.
  - The photo bleeds to the right edge of the screen.
  - The client logos continue on the same dark field below it.
- **Navigation:** dark, with the links centered between the logo and an orange "Contact us" button. The duplicate "Contact" text link is removed on desktop.
- **Services:** full-height photo tiles with the text over a dark fade.
- **Case studies:** a large-type list on navy.
- **Inner pages:** dark headers with white titles, dark sub-navigation and dark call-to-action bands. Reading content stays on white.
- **Assets made for the dark sections:**
  - An all-white version of the Farsight logo (`assets/farsight-logo-white.png`), made by recolouring the original file. The shapes are untouched.
  - White client logos (`assets/clients/white/`).
  - A dark version of the countries map (`assets/map-dark.svg`).

**New [CONFIRM]:** ask Farsight for an official reversed (white) logo. The current one is recoloured from their full-colour file.

**Files and checks**
- The earlier light stylesheet is replaced. A copy of it was kept outside the project for reference.
- CSS and JS links now carry a version tag, so browsers always load the latest files after a rebuild.
- All 18 pages pass the checks at 360, 390, 768, 1280 and 1920px.
