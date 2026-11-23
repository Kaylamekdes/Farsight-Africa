"""Static site generator for the Farsight Africa Group redesign concept.

Run:  python build.py
Writes one index.html per page, mirroring the live site's URLs, with relative
links so the site works from a dev server or straight from disk.
All copy is taken from farsightafrica.com (read 20 Nov 2026); typos are lightly corrected.
"""
import html
import os
import re
import time

VER = str(int(time.time()))  # cache-busting tag for CSS/JS

ROOT = os.path.dirname(os.path.abspath(__file__))
E = html.escape

# ---------------------------------------------------------------- site map
NAV = [
    ("Home", "", None),
    ("About", None, [
        ("Get to Know Us", "about-us/get-to-know-us/"),
        ("Mission, Vision & Culture", "about-us/mission-vision-culture/"),
        ("Farsight Unique Profile", "about-us/farsight-unique-profile/"),
        ("Leadership Team", "about-us/leadership-team/"),
        ("Press Release", "about-us/press-release/"),
    ]),
    ("Services", None, [
        ("Service Overview", "services/service-overview/"),
        ("Public Sector Advisory", "services/public-sector-advisory/"),
        ("Technology & Innovation", "services/technology-innovation/"),
        ("M&E Research and Learning", "services/me-research-and-learning/"),
        ("Strategic Communication", "services/strategic-communication/"),
    ]),
    ("Clients & Case Studies", None, [
        ("Clients", "clients-case-studies/clients/"),
        ("Case Studies", "clients-case-studies/case-studies/"),
    ]),
    ("Contact", "contact-us/", None),
]

CASES = [
    dict(
        path="2022/07/15/supply-installation-configuration-and-implementation-of-an-integrated-tax-administration-system-itas-liberia-revenue-authority-lra/",
        short="ITAS for the Liberia Revenue Authority",
        title="Supply, Installation, Configuration and Implementation of an Integrated Tax Administration System (ITAS) – Liberia Revenue Authority (LRA)",
        client="Liberia Revenue Authority (LRA)", country="Liberia", years="February 2021 – Ongoing",
        services=[("Technology & Innovation", "services/technology-innovation/"), ("Public Sector Advisory", "services/public-sector-advisory/")],
        teaser="Supply, installation, configuration, integration and support of all hardware equipment and overall project management, jointly funded by the World Bank.",
        summary=[("p", "The Liberia Revenue Authority (LRA) needed a credible firm to supply, install, configure and implement an Integrated Tax Administration System. The Public Financial Management Reform for Institutional Strengthening launched this project, jointly funded by the World Bank, to enable LRA to achieve efficiently its objectives in implementing, leveraging and continuously improving a new ITAS solution based on best practices."),
                 ("p", "We have been tasked with the supply, installation, configuration, integration and support of all hardware equipment and overall project management.")],
        comment="Farsight is proud to be part of the LRA Transformation Journey that will modernise tax and revenue collections and enable the citizen to contribute to the tax of the country in a more efficient manner, while giving LRA the needed insights.",
        outcome=[("p", "LRA is aiming to deploy a modern tax administration application that will help meet the following desired outcomes:"),
                 ("ul", ["Improved taxpayer registration through online registration", "Improved online and on-time filing", "Improved online and on-time tax payment", "Increase tax revenue", "Increase taxpayer compliance levels"]),
                 ("p", "We are working with our implementation partners to ensure these are realised through the ITAS system.")],
        logo=("lra.png", 207, 57, "Liberia Revenue Authority"),
    ),
    dict(
        path="2021/11/30/communication-services-for-the-national-development-plan-ndp-9/",
        short="NDP-9 communications for Somalia’s Ministry of Planning",
        title="Communication Services for the National Development Plan (NDP-9) – Ministry of Planning, Investment and Economic Development (MOPIED), Federal Government of Somalia",
        client="Ministry of Planning, Investment and Economic Development (MOPIED), Federal Government of Somalia", country="Somalia", years="2020",
        services=[("Strategic Communication", "services/strategic-communication/")],
        teaser="Content on the purpose, process and actions of NDP-9: audio-visual content for radio, TV and digital, and mini-documentaries in English and Somali.",
        summary=[("p", "The Ministry of Planning, Investment, and Economic Development (MOPIED) contracted Farsight Africa Group to create content on the purpose, process, and actions of the National Development Plan-9. The campaign involved:"),
                 ("ul", ["Strengthening the quality of information disseminated on the NDP-9 at both state and national levels; creative ways were devised through pro-active communications.",
                         "Production of audio-visual content for dissemination to radio, TV and digital platforms.",
                         "Creating mini-documentaries that explained the actions the government is taking to reach its goals and how citizens can participate and contribute to the development of the nation."]),
                 ("links", [("Watch the mini-documentary in English", "https://www.youtube.com/watch?v=bD1QGhMFQME"), ("Watch the mini-documentary in Somali", "https://youtu.be/65Yt9YLhLs4")])],
        comment="At the time of this project Somalia was trying to qualify for a special program for debt relief with the IMF. The success of this project contributed to the larger initiative. We were proud of our client and of our own work when the program was accessed.",
        outcome=None,
        logo=("somalia-fgs.png", 168, 145, "Federal Republic of Somalia"),
    ),
    dict(
        path="2021/11/29/gender-dimensions-in-affected-communities-related-to-unicef-somalia-interventions/",
        short="Gender dimensions study for UNICEF Somalia",
        title="Gender Dimensions in Affected Communities Related to UNICEF Somalia Interventions – UNICEF",
        client="UNICEF Somalia", country="Somalia", years="2019",
        services=[("M&E Research and Learning", "services/me-research-and-learning/")],
        teaser="Household surveys, key informant interviews, focus group discussions and institutional capacity assessment across Somaliland, Puntland and central south regions.",
        summary=[("p", "The study entails a survey of gender dimensions of various aspects of UNICEF programming in Somalia. The study includes household surveys, key informant interviews, focus group discussions (FGDs), and institutional capacity assessment of WASH, nutrition, child protection and other thematic areas."),
                 ("p", "The target locations were Somaliland, Puntland and central south regions.")],
        comment="From the field team to the project personnel the study ran smoothly. The study has allowed us to provide an evidence-base and direction for gender-transformative and inclusive approaches to supplement the UNICEF Somalia humanitarian and development response.",
        outcome=None,
        logo=("unicef.png", 124, 126, "UNICEF"),
    ),
    dict(
        path="2021/11/29/african-union-united-nations-information-support-team-au-un-ist/",
        short="Communications support for the AU/UN Information Support Team",
        title="Multidisciplinary Communications Support Services – African Union/United Nations Information Support Team",
        client="African Union / United Nations, Somalia", country="Somalia", years="2014 – 2019",
        services=[("Strategic Communication", "services/strategic-communication/"), ("M&E Research and Learning", "services/me-research-and-learning/")],
        teaser="Research and monitoring, advocacy and outreach campaigns, media monitoring and analytics, and capacity building in Mogadishu and the regions.",
        summary=[("p", "Farsight was tasked with developing multi-disciplinary information support services in the areas of: research and monitoring through baseline, endline and midline surveys, FGDs and KIIs; advocacy and outreach campaigns; media monitoring and analytics; capacity building and production of novelty items. The engagement activities included:"),
                 ("ul", ["Awareness programmes and training workshops in Mogadishu and the regions",
                         "Coordination and set up of stakeholders and partners for engagement, including regional and federal administrations, media, community leaders, religious leaders and opinion leaders",
                         "Media relations and liaison", "Counter terrorism and radicalisation", "Community policing and traditional dispute resolution"])],
        comment="Our team took a hands-on approach, which brought a significant level of credibility, enabling us to deliver world-class research and capacity building to receptive networks and stakeholders in the region. Key to our work was the facilitation of behavioural change communications that were developed collaboratively and intelligently through rolling field research, allowing innovative outreach and engagement.",
        outcome=[("p", "We then leveraged our partner networks and contacts to provide additional support and advocacy of project initiatives, enhancing Somali diplomacy and media representation globally."),
                 ("p", "Farsight Africa’s professional expertise, local knowledge and strategic leverage delivered cohesive and effective results at all levels. This project did not just fulfil the client brief, but also enhanced the Farsight reputation with organisations and stakeholders in Somalia.")],
        logo=("african-union.png", 279, 96, "African Union"),
    ),
]

SERVICES = [
    dict(key="public-sector-advisory", name="Public Sector Advisory", path="services/public-sector-advisory/",
         line="Advice for ministries, agencies and funders."),
    dict(key="technology-innovation", name="Technology & Innovation", path="services/technology-innovation/",
         line="Tax, revenue and information systems for government."),
    dict(key="me-research-learning", name="M&E Research and Learning", path="services/me-research-and-learning/",
         line="Research and evidence for policy and planning."),
    dict(key="strategic-communication", name="Strategic Communication", path="services/strategic-communication/",
         line="Campaigns, media and outreach that reach the public."),
]

# ---------------------------------------------------------------- helpers
def rel(depth):
    return "../" * depth


def depth_of(path):
    return len([p for p in path.split("/") if p])


def L(R, path):
    """Internal link from a page with root prefix R to site path ('' = home)."""
    return f"{R}{path}index.html"


def blocks(items, R=""):
    out = []
    for b in items:
        kind = b[0]
        if kind == "p":
            out.append(f"<p>{b[1]}</p>")
        elif kind == "lead":
            out.append(f'<p class="prose-lead">{b[1]}</p>')
        elif kind == "h3":
            out.append(f"<h3>{b[1]}</h3>")
        elif kind == "ul":
            out.append("<ul class=\"bullets\">" + "".join(f"<li>{x}</li>" for x in b[1]) + "</ul>")
        elif kind == "img":
            _, src, alt, w, h, cap = b
            full = src.replace(".webp", "") if False else src
            out.append(f'<figure class="diagram"><a href="{R}assets/img/{src}" aria-label="Open full-size image: {E(cap)}"><img src="{R}assets/img/{src}" width="{w}" height="{h}" loading="lazy" alt="{E(alt)}"></a><figcaption>{cap}</figcaption></figure>')
        elif kind == "links":
            out.append('<ul class="ext-links">' + "".join(f'<li><a class="link-arrow" href="{u}">{t}</a></li>' for t, u in b[1]) + "</ul>")
    return "\n".join(out)


def page_head(R, crumbs, eyebrow, title, lede="", image=None, small=False):
    cr = [f'<li><a href="{L(R, "")}">Home</a></li>'] + [f'<li><a href="{L(R, p)}">{t}</a></li>' for t, p in crumbs] + [f'<li aria-current="page">{title if len(title) < 60 else E(eyebrow)}</li>']
    fig = ""
    if image:
        src, src2, w, h, alt = image
        fig = f'<figure class="page-photo"><img src="{R}assets/img/{src}" srcset="{R}assets/img/{src} 900w, {R}assets/img/{src2} 1600w" sizes="(max-width:1040px) 100vw, 40vw" width="{w}" height="{h}" alt="{E(alt)}" fetchpriority="high"></figure>'
    return f"""
  <section class="page-head{' page-head-small' if small else ''}{' has-photo' if image else ''}">
    <div class="wrap page-head-grid">
      <div class="page-head-copy">
        <nav class="crumbs" aria-label="Breadcrumb"><ol>{''.join(cr)}</ol></nav>
        <h1>{title}</h1>
        {f'<p class="lede">{lede}</p>' if lede else ''}
      </div>
      {fig}
    </div>
  </section>"""


def subnav(R, group, current):
    items = next(c for n, p, c in NAV if n == group)
    lis = "".join(f'<li><a href="{L(R, p)}"{" aria-current=\"page\"" if p == current else ""}>{E(t)}</a></li>' for t, p in items)
    return f'<nav class="subnav" aria-label="{E(group)} pages"><div class="wrap"><ul>{lis}</ul></div></nav>'


def cta_band(R, heading="Discuss a project with us", text=""):
    return f"""
  <section class="cta-band">
    <div class="wrap cta-grid">
      <div><h2>{heading}</h2>{f'<p>{text}</p>' if text else ''}</div>
      <div class="cta-actions">
        <a class="btn btn-primary" href="{L(R, 'contact-us/')}#enquiry">Send an enquiry</a>
        <a class="btn btn-ghost" href="tel:+254711845333">Call Nairobi</a>
      </div>
    </div>
  </section>"""


def case_cards(R, cases, heading_level=3):
    out = []
    for c in cases:
        out.append(f"""<article class="case reveal">
          <p class="case-meta"><span>{c['client']}</span><span>{c['years']}</span></p>
          <h{heading_level}>{c['title'].split(' – ')[0] if c['title'].count(' – ') and not c['title'].startswith('Multidisciplinary') else c['title']}</h{heading_level}>
          <a class="link-arrow" href="{L(R, c['path'])}">Read full case study<span class="sr">: {E(c['short'])}</span></a>
        </article>""")
    return "\n".join(out)


def logo_wall(R):
    logos = [("world-bank-group", 144, 123, "World Bank Group", "seal"), ("unsom", 108, 115, "UNSOM", "seal"), ("unsoa", 100, 120, "UNSOA", "seal"),
             ("unmiss", 103, 111, "UNMISS", "seal"), ("us-embassy", 115, 115, "United States of America Embassy", "seal"), ("iom", 158, 60, "IOM, UN Migration", "mark"),
             ("unicef", 124, 126, "UNICEF", "seal"), ("somalia-fgs", 168, 145, "Federal Republic of Somalia", "seal"), ("lra", 207, 57, "Liberia Revenue Authority", "mark"),
             ("amisom", 340, 73, "AMISOM, African Union Mission in Somalia", "mark"), ("african-union", 279, 96, "African Union", "mark"),
             ("who", 270, 83, "World Health Organization", "mark"), ("hormuud", 234, 66, "Hormuud Telecom", "mark")]
    return '<ul class="logo-wall">' + "".join(f'<li><img class="{k}" src="{R}assets/clients/{f}.png" width="{w}" height="{h}" alt="{E(a)}" loading="lazy"></li>' for f, w, h, a, k in logos) + "</ul>"


QUOTES = [
    ("They are a friendly, economical and efficient local consulting partner in the horn of Africa, one that I would recommend to any business that requires quick and efficient guidance on political, social and economic campaigns", "mc-saatchi.png", "M&amp;C Saatchi"),
    ("There was excitement here with the approval. Perhaps it did not strike you as it did for us here as a major milestone. There are plans to officially launch the KAP report probably this month. Well done, and thanks very much.", "unicef-quote.png", "UNICEF"),
    ("Farsight Africa Group is a professional and client-oriented firm that has delivered on its contractual obligations. I would highly recommend them.", "unsos.png", "UNSOS, United Nations Support Office in Somalia"),
]


def quotes(R):
    return '<div class="quotes">' + "".join(f"""<figure class="quote reveal">
          <blockquote><p>{q}</p></blockquote>
          <figcaption><img src="{R}assets/clients/{img}" width="600" height="228" alt="{alt}" loading="lazy"></figcaption>
        </figure>""" for q, img, alt in QUOTES) + "</div>"


FORM = """
      <form class="form" id="enquiry" novalidate aria-describedby="form-note">
        <p class="form-note" id="form-note">Demo form, no server: it opens your email app with your message. Nothing is sent until you press send.</p>
        <div class="field-row"><div class="field"><label for="f-name">Name</label><input id="f-name" name="name" type="text" autocomplete="name" required aria-describedby="e-name"><p class="error" id="e-name" aria-live="polite"></p></div>
        <div class="field"><label for="f-org">Organisation</label><input id="f-org" name="organisation" type="text" autocomplete="organization" required aria-describedby="e-org"><p class="error" id="e-org" aria-live="polite"></p></div></div>
        <div class="field-row"><div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required aria-describedby="e-email"><p class="error" id="e-email" aria-live="polite"></p></div>
        <div class="field"><label for="f-area">Area of interest</label><select id="f-area" name="area" required aria-describedby="e-area"><option value="">Choose a service</option><option>Public Sector Advisory</option><option>Technology &amp; Innovation</option><option>M&amp;E Research and Learning</option><option>Strategic Communication</option></select><p class="error" id="e-area" aria-live="polite"></p></div></div>
        <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" rows="4" required aria-describedby="e-msg"></textarea><p class="error" id="e-msg" aria-live="polite"></p></div>
        <button class="btn btn-primary" type="submit">Open in email app</button>
        <div class="form-status" id="form-status" role="status" tabindex="-1" hidden></div>
      </form>"""

# ---------------------------------------------------------------- layout
def header(R, section, current):
    items = []
    mobile = []
    for i, (name, path, children) in enumerate(NAV):
        if children is None:
            cur = ' aria-current="page"' if path == current else ""
            if path != "contact-us/":  # desktop uses the "Contact us" button instead
                items.append(f'<li><a class="nav-top" href="{L(R, path)}"{cur}>{name}</a></li>')
            mobile.append(f'<a class="m-top" href="{L(R, path)}"{cur}>{name}</a>')
        else:
            active = " is-active" if section == name else ""
            sub = "".join(f'<li><a href="{L(R, p)}"{" aria-current=\"page\"" if p == current else ""}>{E(t)}</a></li>' for t, p in children)
            items.append(f'<li class="has-sub"><button class="nav-top nav-toggle{active}" type="button" aria-expanded="false" aria-controls="sub-{i}">{E(name)}<span class="chev" aria-hidden="true"></span></button><ul class="sub" id="sub-{i}" hidden>{sub}</ul></li>')
            msub = "".join(f'<a href="{L(R, p)}"{" aria-current=\"page\"" if p == current else ""}>{E(t)}</a>' for t, p in children)
            mobile.append(f'<div class="m-group"><p class="m-label">{E(name)}</p>{msub}</div>')
    return f"""
<a class="skip" href="#main">Skip to content</a>
<div class="concept-bar" role="note"><div class="wrap">Concept by TheCompany.design · Not the official Farsight website</div></div>
<header class="nav" id="top">
  <div class="wrap nav-inner">
    <a class="nav-logo" href="{L(R, '')}" aria-label="Farsight Africa Group home"><img src="{R}assets/farsight-logo-white.png" width="500" height="106" alt="Farsight Africa Group"></a>
    <nav class="nav-links" aria-label="Main"><ul>{''.join(items)}</ul></nav>
    <a class="btn btn-primary nav-cta" href="{L(R, 'contact-us/')}"{' aria-current="page"' if current == 'contact-us/' else ''}>Contact us</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-menu"><span class="menu-icon" aria-hidden="true"></span><span class="menu-label">Menu</span></button>
  </div>
  <div class="mobile-menu" id="mobile-menu" hidden>
    <nav aria-label="Mobile">{''.join(mobile)}</nav>
    <div class="mobile-quick">
      <a class="btn btn-primary" href="tel:+254711845333">Call Nairobi office</a>
      <a class="btn btn-ghost" href="mailto:info@farsightafrica.com">Email info@farsightafrica.com</a>
    </div>
  </div>
</header>"""


def footer(R):
    return f"""
<footer class="footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <img src="{R}assets/farsight-logo-white.png" width="500" height="106" alt="Farsight Africa Group" loading="lazy">
      <p>Careers: <a href="mailto:jobs@farsightafrica.com">jobs@farsightafrica.com</a></p>
      <ul class="socials" aria-label="Social media">
        <li><a href="https://twitter.com/FarsightAfrica">Twitter</a></li>
        <li><a href="https://www.linkedin.com/company/farsight-africa-group-limited/">LinkedIn</a></li>
        <li><a href="https://www.facebook.com/FarsightAfrica/">Facebook</a></li>
      </ul>
    </div>
    <nav aria-label="Footer: About"><h2 class="footer-h">About</h2><ul>{''.join(f'<li><a href="{L(R, p)}">{E(t)}</a></li>' for t, p in NAV[1][2])}</ul></nav>
    <nav aria-label="Footer: Services"><h2 class="footer-h">Services</h2><ul>{''.join(f'<li><a href="{L(R, p)}">{E(t)}</a></li>' for t, p in NAV[2][2])}</ul></nav>
    <div>
      <h2 class="footer-h">Contact</h2>
      <ul class="footer-offices">
        <li>Nairobi · <a href="tel:+254711845333">+254 (0) 711 845 333</a></li>
        <li>Mogadishu · <a href="tel:+252613529999">+252 (0) 61 352 9999</a></li>
        <li>Monrovia · Tubman Boulevard</li>
        <li><a href="mailto:info@farsightafrica.com">info@farsightafrica.com</a></li>
        <li><a href="{L(R, 'clients-case-studies/clients/')}">Clients</a> · <a href="{L(R, 'clients-case-studies/case-studies/')}">Case Studies</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-base">
    <p>© Copyright 2026. Farsight Africa. All Rights Reserved</p>
    <p>Concept by TheCompany.design · not the official Farsight website</p>
  </div>
</footer>"""


def page(path, title, description, section, body, extra_head=""):
    R = rel(depth_of(path))
    doc_title = "Farsight Africa Group | Homepage concept" if path == "" else f"{title} | Farsight Africa Group (concept)"
    out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{E(doc_title)}</title>
<meta name="description" content="{E(description)}">
<link rel="icon" type="image/png" href="{R}assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600&display=swap" rel="stylesheet">
{extra_head}<link rel="stylesheet" href="{R}styles.css?v={VER}">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
{header(R, section, path)}
<main id="main">
{body.replace('{R}', R)}
</main>
{footer(R)}
<script src="{R}main.js?v={VER}" defer></script>
</body>
</html>
"""
    target = os.path.join(ROOT, path, "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(out)
    return target


# ---------------------------------------------------------------- pages
built = []

# Home
home = open(os.path.join(ROOT, "src", "home.html"), encoding="utf-8").read()
built.append(page("", "Home", "Homepage redesign concept for Farsight Africa Group by TheCompany.design. Not approved by Farsight and not their official site.", "Home", home,
                  '<link rel="preload" as="image" href="assets/img/hero-900.webp" imagesrcset="assets/img/hero-900.webp 900w, assets/img/hero-1600.webp 1600w" imagesizes="(max-width:1040px) 100vw, 46vw">\n'))

BANNER = ("inner-banner-900.webp", "inner-banner-1600.webp", 1600, 555, "A team meeting around a conference table")
ABOUT_CRUMB = [("About", "about-us/get-to-know-us/")]

# --- About: Get to Know Us
p = "about-us/get-to-know-us/"
R = "{R}"
body = page_head(R, ABOUT_CRUMB, "About", "Get to Know Us", "An advisory and implementation company, headquartered in Nairobi.", BANNER) + subnav("{R}", "About", p) + f"""
  <section class="section">
    <div class="wrap prose-grid">
      <div class="prose">
        <p class="prose-lead">Farsight Africa Group is an advisory and implementation company that provides services for governments, administrations, development organisations and private companies.</p>
        <p>Since our establishment in 2010, we have gained extensive experience in complex, sensitive and hostile environments, but also work in more secure and democratic regions.</p>
        <p>The Farsight core team comprises experienced international practitioners who manage each project, allocating international and local experts as needed, combining best standards and practice with local knowledge.</p>
        <p>Our deep understanding of the social, cultural and political landscape in our operational territories can be augmented by consultation with decision makers and influencers, to ensure cross-cutting strategic impact as well as behavioural and attitudinal change among key audiences.</p>
        <p>We have a wide portfolio of specialisations, but the first consultation is to understand your needs, discuss the specialities that will best answer them and develop the particular services required to give you the unique and tailored Farsight Service.</p>
      </div>
      <aside class="facts" aria-label="Key facts">
        <dl>
          <div><dt>Established</dt><dd>2010</dd></div>
          <div><dt>Headquarters</dt><dd>Nairobi, Kenya</dd></div>
          <div><dt>Operational offices</dt><dd>Somalia, South Sudan and Liberia</dd></div>
          <div><dt>Network</dt><dd>Representatives throughout Africa and beyond</dd></div>
        </dl>
        <a class="link-arrow" href="{L(R, 'about-us/leadership-team/')}">Meet the leadership team</a>
      </aside>
    </div>
  </section>
  <section class="section section-fill">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">What we do</p><h2>Four service lines</h2></div>
      <div class="svc-cards">{''.join(f'<a class="svc-card reveal" href="{L(R, s["path"])}"><img src="{R}assets/img/service-{s["key"]}.webp" width="480" height="425" alt="" loading="lazy"><span class="svc-card-body"><span class="svc-card-title">{E(s["name"])}</span><span class="svc-card-line">{s["line"]}</span></span></a>' for s in SERVICES)}</div>
    </div>
  </section>""" + cta_band("{R}")
built.append(page(p, "Get to Know Us", "About Farsight Africa Group: an advisory and implementation company established in 2010, headquartered in Nairobi.", "About", body))

# --- About: Mission, Vision & Culture
p = "about-us/mission-vision-culture/"
body = page_head("{R}", ABOUT_CRUMB, "About", "Mission, Vision &amp; Culture", "") + subnav("{R}", "About", p) + """
  <section class="section">
    <div class="wrap">
      <ol class="mvc">
        <li class="reveal"><p class="mvc-label">Mission</p><p class="mvc-text">To promote development and prosperity through concise, consistent and innovative services and products.</p></li>
        <li class="reveal"><p class="mvc-label">Vision</p><p class="mvc-text">We strive to become the go-to advisory services company contributing to a better tomorrow for our clients and communities.</p></li>
        <li class="reveal"><p class="mvc-label">Culture</p><p class="mvc-text">Farsight Africa is a diverse and dynamic organisation, developing relationships through its reliability, innovation and accountability. We seek long term partnerships, with clients returning to us and benefitting from the tailored solutions of the Farsight Africa team.</p></li>
      </ol>
    </div>
  </section>""" + cta_band("{R}")
built.append(page(p, "Mission, Vision & Culture", "Farsight Africa Group's mission, vision and culture.", "About", body))

# --- About: Unique profile
p = "about-us/farsight-unique-profile/"
UP = [("Africa-based,", "globally informed"), ("Developed from local knowledge,", "internationally delivered"),
      ("Selections from our portfolio,", "augmented with special programmes to match your needs"),
      ("Applied with the experience of serving our broad clientele base,", "including public sector, private sector, development organisations, NGOs, and national and regional authorities"),
      ("Complementary in our range of solutions,", "including IT, research and communication"), ("Applied within our global partner ecosystem", "to augment our services")]
body = page_head("{R}", ABOUT_CRUMB, "About", "Farsight Unique Profile", "What shapes every Farsight engagement.") + subnav("{R}", "About", p) + f"""
  <section class="section">
    <div class="wrap">
      <div class="section-head"><h2>Our services and operations are</h2></div>
      <ol class="why why-light">{''.join(f'<li class="reveal"><span class="num">{i:02d}</span><p><strong>{a}</strong> {b}</p></li>' for i, (a, b) in enumerate(UP, 1))}</ol>
    </div>
  </section>""" + cta_band("{R}")
built.append(page(p, "Farsight Unique Profile", "Six statements that define how Farsight Africa Group works.", "About", body))

# --- About: Leadership
p = "about-us/leadership-team/"
SENIOR = [
    ("Abdirisak M Aden", "Founder &amp; Chief Executive Officer", "abdirisak-aden.webp", [
        "Abdirisak has over 15 years experience in strategic public affairs, communications, lobbying and monitoring and evaluation projects. He served as Senior Communication Adviser to the former President of Somalia and was the Permanent Secretary at the Ministry of Information, Somalia. He has also served in the Somali Prime Minister’s Office.",
        "Abdirisak holds a BA in Politics and International Relations from the University of the West of England and Stockholm University. He has a certificate from the Annenberg-Oxford Summer Institute Seminar on Global Media Policy and Comparative Media Law, Strategic Communications, and a School Management Certificate from the Swedish School Agency and School Leadership University."]),
    ("Richard Manduku", "Chief Operating Officer", "richard-manduku.webp", [
        "Richard is a highly experienced manager working on country and regional Farsight projects. With over 20 years experience which has included marketing, media and communication management, he has worked and consulted with global companies applying crucial skills and knowledge to global best practices. Richard has been involved in developing communications strategies, marketing and monitoring, training and strategic management of the media and advertising unit.",
        "He is Farsight team leader for the IOM West Africa project and provides departmental management and cross-cutting support to all initiatives.",
        "Richard holds a Bachelor of Business Administration – Marketing from Kenya Methodist University, an ABE Marketing Diploma (UK) and MSK certification in Marketing."]),
    ("Debbie Maina", "HR Manager Specialist", "debbie-maina.webp", [
        "Debbie is a highly experienced Human Resources professional and a goal-oriented generalist with 4 years of experience in corporate communication and policy implementation. She has a passion for productivity measurement, ensuring that the organisation and its clients get maximum output from their investment.",
        "Debbie has gained experience in the development and implementation of systems and policies, performance management, management of staff through HRMIS, and management of benefits, contracts, payroll, training delivery, recruitment and onboarding programmes, among other corporate tasks. She is passionate about developing strategies which recognise people as the most valuable asset in the organisation, building high employee commitment and client engagement.",
        "Debbie holds a Master of Science degree in Management with Human Resources from Bournemouth University, England, and is currently pursuing her Certified Human Resource Professional course in Nairobi, Kenya."]),
]
BOARD = [
    ("Steve Turner", "ST", "Steve Turner has been engaged in management, development and media and communications for many years, working for commercial companies, global agencies and the international community of development, diplomatic, NGO and UN agencies. Since the early 1990s he has worked on behalf of these agencies and as an independent consultant in many public sector and crisis situations, with projects involving professional missions to more than 60 countries. Since 2010, Steve’s work has included significant initiatives in Somalia, where he has directed numerous projects and consulted with many of the national and international stakeholders, and federal and member state governments."),
    ("Joel Gachomo", "JG", "Joel has more than 16 years experience in international business development, project management, sales and personnel management, across diverse cultures and countries. His work has included the IT sector, where he has fulfilled various roles from software developer to Director of Business across Africa. Having spearheaded the ground-breaking Liberia Revenue Authority Tax and Revenue Automation system on behalf of Farsight Africa, his commitment to the company remains through his active participation on the Advisory Board."),
    ("George Nyabuga", "GN", "Professor George Nyabuga is an Associate Professor of media and journalism at The Aga Khan University’s Graduate School of Media and Communications and the coordinator of the Executive Masters in Media Leadership and Innovation (EMMLI) programme. He is currently on sabbatical from the University of Nairobi, where he has taught for more than 12 years. He has also taught at the University of Worcester and Coventry University in the United Kingdom. He worked as a journalist before joining academia; his last positions in the media were Managing Editor in charge of Weekend Editions, and Managing Editor, Media Convergence, at the Standard Group."),
]
senior_html = "".join(f"""<article class="leader reveal">
          <img class="leader-photo" src="{{R}}assets/img/{img}" width="421" height="456" alt="Portrait of {n}" loading="lazy">
          <div class="leader-body"><h3>{n}</h3><p class="role">{r}</p>{''.join(f'<p>{x}</p>' for x in bio)}</div>
        </article>""" for n, r, img, bio in SENIOR)
board_html = "".join(f"""<article class="board reveal">
          <div class="monogram" aria-hidden="true">{ini}</div>
          <div><h3>{n}</h3><p class="role">Advisory Board</p><p>{bio}</p><p class="confirm">[CONFIRM] Photo</p></div>
        </article>""" for n, ini, bio in BOARD)
body = page_head("{R}", ABOUT_CRUMB, "About", "Leadership Team", "") + subnav("{R}", "About", p) + f"""
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Senior management</p><h2>Management team</h2></div>
      <div class="leaders">{senior_html}</div>
    </div>
  </section>
  <section class="section section-fill">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Advisory board</p><h2>Advisory Board</h2></div>
      <div class="boards">{board_html}</div>
    </div>
  </section>""" + cta_band("{R}")
built.append(page(p, "Leadership Team", "Farsight Africa Group senior management and advisory board.", "About", body))

# --- About: Press release
p = "about-us/press-release/"
body = page_head("{R}", ABOUT_CRUMB, "About", "Press Release", "") + subnav("{R}", "About", p) + f"""
  <section class="section">
    <div class="wrap">
      <article class="press reveal">
        <div class="press-doc" aria-hidden="true"><span>PDF</span></div>
        <div>
          <p class="case-meta"><span>Liberia Revenue Authority</span><span>3 pages · 1.5 MB</span></p>
          <h2 class="press-title">Liberia Revenue Authority Launches Integrated Tax Administrative System (ITAS)</h2>
          <p class="press-note"><span class="confirm">[CONFIRM]</span> Release date</p>
          <div class="press-actions">
            <a class="btn btn-primary" href="{{R}}assets/docs/LRA-ITAS-PRESS-RELEASE.pdf" download>Download press release (PDF)</a>
            <a class="link-arrow" href="{L('{R}', CASES[0]['path'])}">Read the ITAS case study</a>
          </div>
        </div>
      </article>
    </div>
  </section>""" + cta_band("{R}", "Media enquiries")
built.append(page(p, "Press Release", "Farsight Africa Group press releases.", "About", body))

# --- Services overview
SVC_CRUMB = [("Services", "services/service-overview/")]
p = "services/service-overview/"
body = page_head("{R}", SVC_CRUMB, "Services", "Service Overview", "Four complementary services, in fragile and stable environments.") + subnav("{R}", "Services", p) + f"""
  <section class="section">
    <div class="wrap">
      <div class="svc-cards">{''.join(f'<a class="svc-card reveal" href="{L("{R}", s["path"])}"><img src="{{R}}assets/img/service-{s["key"]}.webp" width="480" height="425" alt="" loading="lazy"><span class="svc-card-body"><span class="svc-card-title">{E(s["name"])}</span><span class="svc-card-line">{s["line"]}</span></span></a>' for s in SERVICES)}</div>
    </div>
  </section>
  <section class="section section-fill">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">How it fits together</p><h2>The unique Farsight service</h2></div>
      {blocks([("img", "diagram-service-overview.webp", "Diagram of Farsight Africa Group's four service lines. Public Sector Advisory: public finance, security sector reform, HR advisory services, training and capacity building. Technology and Innovation: data centre solutions, integrated tax administration systems, Hornswitch. M&E Research and Learning: attitudinal analysis, market testing, impact measurement. Strategic Communication: content production and dissemination, mainstream and digital campaigns, training, outreach and live events, media monitoring and analysis, branding and design.", 1600, 1069, "Service overview diagram from the current Farsight website. Select to open full size.")], "{R}")}
    </div>
  </section>""" + cta_band("{R}")
built.append(page(p, "Service Overview", "Farsight Africa Group's four service lines.", "Services", body))


def service_page(path, key, name, lede, sections, related, photo_alt):
    toc = "".join(f'<li><a href="#{sid}">{t}</a></li>' for sid, t, _ in sections)
    secs = "".join(f'<section class="svc-section" id="{sid}" aria-labelledby="{sid}-h"><h2 id="{sid}-h">{t}</h2>{blocks(b, "{R}")}</section>' for sid, t, b in sections)
    rel_cases = [c for c in CASES if any(sp == path for _, sp in c["services"])] if related else []
    rel_html = ""
    if rel_cases:
        rel_html = f"""
  <section class="section section-fill">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Related work</p><h2>Case studies</h2></div>
      <div class="cases">{case_cards('{R}', rel_cases)}</div>
    </div>
  </section>"""
    body = page_head("{R}", SVC_CRUMB, "Services", name, lede, (f"service-{key}-800.webp", f"service-{key}-800.webp", 800, 709, photo_alt)) + subnav("{R}", "Services", path) + f"""
  <section class="section">
    <div class="wrap svc-layout">
      <nav class="toc" aria-label="On this page"><p class="toc-label">On this page</p><ol>{toc}</ol></nav>
      <div class="prose svc-body">{secs}</div>
    </div>
  </section>{rel_html}""" + cta_band("{R}", f"Discuss {E(name)} with us")
    built.append(page(path, name.replace("&amp;", "&"), lede, "Services", body))


service_page("services/public-sector-advisory/", "public-sector-advisory", "Public Sector Advisory",
             "Advice for ministries, agencies and funders.", [
    ("introduction", "Introduction", [
        ("lead", "Farsight Africa’s Public Sector Advisory service has a proven track record in all levels of government institutions, including ministries, agencies and international funding organisations, working in a transparent, accountable and efficient way."),
        ("p", "Our experience in the public sector can also provide advisory services to commercial and non-profit organisations that are planning to work with governments or respond to tenders, where we can provide guidance and up to date status reports essential for successful engagement.")]),
    ("public-finance", "Public Finance", [
        ("p", "Farsight Africa’s Public Finance and Revenue management services provide enhanced automation in tax collection, local revenue mobilisation, collection and accountability. Our solutions assist revenue authorities, ministries of finance and local government authorities to enhance revenue administration and collection.")]),
    ("security-sector-reform", "Security Sector Reforms", [
        ("p", "Farsight Africa Group has been engaged in security sector reform through security and conflict analysis and systematic research in the economic, political and social dynamics of security and conflict. Our team comprises certified security specialists with senior level experience in some of the world’s most acute scenarios, working with national military operations and some of the world’s largest private security organisations."),
        ("p", "We recognise the importance of developing national and regional security and the contribution it makes to social development, humanitarian work and peace building. We can also advise organisations in conflict or post-conflict locations to gain a better understanding of the context in which they work and their regional role in the context of unstable environments.")]),
    ("hr-advisory", "HR Advisory Services", [
        ("p", "We provide a comprehensive range of HR services to public and private commercial organisations alike. With our in-depth understanding of the client’s operating environment, we meet workforce needs with specialists overlaid with Farsight’s years of expertise. We achieve this by:"),
        ("ul", ["Providing appropriate candidates, going the extra mile to transform your HR services", "Providing end-to-end HR solutions to anticipate and meet business needs", "Enhancing workforce experience through training and development solutions", "Building the transformative capabilities of HR professionals so they can contribute to organisational resilience and continue to deliver regardless of the difficulties of the particular environment"])]),
    ("training", "Training and Capacity Building", [
        ("p", "Farsight Africa Group has provided training services to UNOPS, the African Development Bank and the US State Department in our capacity building programmes for the Federal Government of Somalia. Courses have included programmes for Leadership, Governance and Management at senior levels and operational training for senior officers, general staff and new recruits."),
        ("p", "We have additionally delivered policy-building training and advice to significant commercial enterprises in East Africa.")]),
    ("complementary", "Complementary Advisory Services", [
        ("p", "After consultation, our professional team will prepare the advisory services to meet your requirements, selecting from the range above and additional initiatives as needed, such as:"),
        ("ul", ["Financial Management", "Business Development: Analysis, Training and Planning", "Government and Local Authority Relations", "Security and Conflict Analysis and Risk Mitigation"])]),
], True, "A raised hand in a classroom")

service_page("services/technology-innovation/", "technology-innovation", "Technology &amp; Innovation",
             "Tax, revenue and information systems for government.", [
    ("introduction", "Introduction", [
        ("lead", "Our Technology and Innovation services have been developed to complement our Public Sector Advisory sector. They assist government and local authorities as well as provide solutions for private and commercial organisations."),
        ("p", "Our systems include consultative and technology and automation services which can be selected according to need. They include:"),
        ("ul", ["Tax revenue collection and administration", "Financial management", "Information systems and analysis", "Public utility service provision platforms", "Hardware solutions (including supply and installation): CT security, computer accessories, networking implementations", "Software solutions: web applications, ICT maintenance contracts, consultancy services, and training"]),
        ("p", "We have implemented IT projects for the Federal Government of Somalia and an infrastructure and networking solution in the Office of the Prime Minister of Somalia."),
        ("p", "Our Integrated Tax Administration System is transforming the operation of taxation and non-tax revenue management for the Liberia Revenue Authority.")]),
    ("itas", "Liberia Revenue Authority (LRA) &amp; Farsight Africa’s ITAS", [
        ("p", "Significant among Farsight Technologies’ projects is the Integrated Tax Administration System, ITAS. This new approach to public finance management has been adopted by the Government of Liberia, for which we manage the supply, installation, configuration and in-house training and support, transforming the way in which Liberia identifies, collects and manages domestic tax."),
        ("img", "diagram-itas-modules.webp", "ITAS modules: Registration, Return Processing, Payments Processing, Assessments, Protest and Appeals, Tax Payer Revenue Accounting, Risk Analysis, Audit, Investigations, Refunds, Compliance and Enforcement, Workflow Management, Case Management, Document Management, MIS Reports and BI, Tax Analysis and Revenue Forecasting, Tax Payer Online Services, Artificial Intelligence and Robotics, Vehicle Tax Management.", 250, 463, "ITAS modules"),
        ("p", "This substantial Farsight Africa service can be applied to revenue collections for all types of government, from district to federal, assisting the authority and the citizen, who can choose from many user-friendly payment services. ITAS can manage all tax and non-tax revenues.")]),
    ("non-tax-revenue", "Non Tax Revenue Management System", [
        ("p", "Non-tax revenue plays a key role in the national budget, particularly in the regional tier of government where most of the key revenue lies. Cities are a particular key source of non-tax revenue through the wide range of services they provide to citizens."),
        ("p", "Our Non Tax Revenue Management System is geared to address key types of revenue collection, to help cities, districts and municipalities to correctly assess, collect and report on their revenues."),
        ("img", "diagram-non-tax-revenues.webp", "Non-tax revenue types: property rates, land rates, business licensing, building permits, solid waste disposal fees, market fees, wayleaves management and outdoor advertising.", 1000, 953, "Non-tax revenues"),
        ("img", "diagram-payment-solution.webp", "Payment solution offering: citizen multi-payment options (payment gateway or switch, banks, telcos and mobile money, cash), reporting with big data and analytics, and tax and revenue systems (ITAS, customs administration system, non-tax revenue management). Payment partners shown include Visa, Mastercard, MTN, Africell and Airtel.", 1400, 621, "Payment solution offering")]),
    ("hornswitch", "Somalia Non Tax Revenue Management System (Hornswitch)", [
        ("p", "In Somalia our subsidiary, Hornswitch, shows how our current operations, offering a complete payment gateway platform at the national level, can be leveraged to enhance in-country payment options. The solution is designed to facilitate the processing of local and international debit and credit cards, local and international interbank settlements, and to drive POS and ATMs."),
        ("p", '<img class="inline-logo" src="{R}assets/img/hornswitch.jpg" width="236" height="54" alt="Hornswitch Payment Solutions" loading="lazy">'),
        ("p", "As part of its product and service offering, Hornswitch is partnered with various leading technology solutions and service providers to ensure seamless service delivery across all identified channels, ranging from interconnectivity, ATMs and POS terminals to mobile and web applications."),
        ("p", "Our particular experience in Somalia has given us the tools to identify the need and provide the specific solution. The same service can be developed to establish payment services in other nation states and regions.")]),
], True, "A hand holding a phone showing a Pay button")

service_page("services/me-research-and-learning/", "me-research-learning", "M&amp;E Research and Learning",
             "Research and evidence for policy and planning.", [
    ("areas-of-expertise", "Areas of Expertise", [
        ("lead", "Through our Monitoring &amp; Evaluation and Research &amp; Learning (MERL) we apply quantitative and qualitative research towards evidence-based policy formulation and strategic planning."),
        ("p", "Our MERL services provide the eyes and ears in the territories in which you have an interest. Whether you are considering entry to a particular territory or market, or assessing your current programme’s impact, MERL will supply you with information to understand, plan, assess and implement your initiatives, and inform subsequent activities."),
        ("p", "Farsight Africa has provided many coordinated MERL programmes where long-term patterns and trends have been tracked, as well as one-off snapshots that provide information and atmospherics for a given time and territory. Supporting our Public Sector Advisory services, Farsight’s MERL operates in specialised areas that include gender, labour, livelihoods, peace and democratic sectors. We also provide information-specific MERL services to support commercial and business development.")]),
    ("evidence-based-policy", "Evidence-based policy formulation and strategic planning", [
        ("p", "We conduct baseline, midline and endline surveys through a strong network of partners to generate knowledge and ideas for evidence-based decision making and strategic planning."),
        ("p", "These are augmented by our unique consultations with regional influencers and decision makers, focus group discussions, and political and commercial stakeholders, depending on the scope and objectives of our clients. Specialist software including NVivo, STATA and SPSS assists in quantitative analysis and reporting to support qualitative assessments and scrutiny.")]),
    ("recent-activities", "Our Recent Activities", [
        ("p", "Among many past programmes, we have provided MERL services for AMISOM and UNSOM on citizen attitudes, for UNICEF on gender issues, and for The World Bank to inform their Digital ID Inclusion programme in Somalia.")]),
], True, "A pen signing a document")

service_page("services/strategic-communication/", "strategic-communication", "Strategic Communication",
             "Campaigns, media and outreach that reach the public.", [
    ("introduction", "Introduction", [
        ("lead", "Farsight Africa Group offers a comprehensive range of Strategic Communications and all associated disciplines."),
        ("p", "Communication is an essential component for any organisation, as important as management policy, financial control or business development. Consultation with Farsight Africa Strategic Communications will assess the best organisational strategy for all levels of activity and responses, internally and client oriented. For a particular project we can develop best approaches considering the aims, target, implementation and impact assessment."),
        ("p", "In-house communication training will develop professional skills, which we can support with our particular communication services."),
        ("p", "We are very experienced in public outreach addressing awareness and engagement with identified target audiences, ranging from a specialised group by topic or location to a broad campaign aimed at international organisations and populations. We have assisted micro-focused political initiatives, commercial development and global awareness campaigns."),
        ("p", "The more focused the campaign, the more important it is to develop a deep understanding of the environment. This has been the hallmark of our targeted campaigns in Somalia and East Africa, where we work closely with communities, regional authorities and international players to understand atmospherics and local conditions before creating specific campaigns. Our partners in these regions have included the African Union, AMISOM, UNSOM, UNSOS, EU and UNMISS.")]),
    ("media-monitoring", "Media Monitoring, Analysis and Media Management", [
        ("p", "It is essential to understand the media environment in which you are working. Our real-time cross-platform Media Monitoring tailors this research to match your interests, regions and types of media."),
        ("p", "Essential for public, development and commercial organisations, Farsight Media Monitoring tracks social, print, radio and TV media reporting on trends and atmospheres, as well as client-initiated Strategic Communication output and its impact in the public sphere. We provide verifiable information and trends, and assessments on misinformation and fake news."),
        ("p", "Continual tracking will report on specific media reporting, updating searches as a campaign develops, with analysis providing evidence of impact and key lessons from your project. This will inform further planning and reports that support you and other stakeholders."),
        ("img", "diagram-media-watch.webp", "Farsight Media Watch in four steps. Searches: the information that will best inform your initiative, by keywords, terminology, media type, region and dissemination. Analysis: assessment of the data by media, context, location and frequency. Verification: editorial themes and storyline are verified so the media narrative is identified in all languages used. Tracking: the impact of client-generated media coverage and audience perception.", 1600, 691, "Farsight Media Watch")]),
    ("social-media", "Social Media Campaigns", [
        ("p", "Farsight Africa has been at the forefront of making quality social media accessible to our clients, enabling them to reach their targeted audiences across all channels. Matching our mainstream media activities, our social media presence gives us access to the platforms relevant to you. These can range from a single or series of social media publications, cross-linking to maximise awareness, to a digital TV channel such as ADN TV, which provides regular in-depth news and comment from Africa and beyond.")]),
    ("content-production", "Content Production", [
        ("p", "Communication can be directed internally to close networks and communities, or to a wider public audience. Internal communications can enable a smooth and coordinated operational environment that will assist you in all projects and overall management. In the public sphere, it will allow you to join a relevant narrative or discourse with your point of view, preventing opposing ideas from becoming dominant in mainstream and social media."),
        ("p", "Farsight Africa can design campaigns that will give you your place in the discussion, influencing the narrative with information and discussion, and profiling your image, accomplishments and abilities. We can produce and disseminate content that will connect you and your messages with your target audiences.")]),
    ("training-outreach-events", "Training, Outreach and Live Events", [
        ("p", "Farsight Africa provides training for internal communications personnel and capacity building for media professionals."),
        ("p", "Our outreach services complement strategic communication campaigns using appropriate media services, including the planning and production of live events, from venue and content management to public and security supervision. We can also link live events to live broadcast and online dissemination.")]),
    ("branding", "Branding and Design", [
        ("p", "This service develops and strengthens your profile, whether establishing emerging brands or rebranding your organisation. Our creative and research-based service will provide you with the branding that will describe your organisation and place you in your activity area, but make you stand out from other operators. Once your theme is established we will develop it for all forms of presentation and products.")]),
    ("complementary", "Complementary Services", [
        ("p", "In consultation, our professional team will prepare the strategic communication services to meet your requirements, selecting from the range above and adding additional initiatives, such as:"),
        ("ul", ["Crisis Management", "Media Relations", "Media Buying", "Advocacy"])]),
], True, "A person using a tablet with digital network icons")

# --- Clients
CC_CRUMB = [("Clients &amp; Case Studies", "clients-case-studies/clients/")]
p = "clients-case-studies/clients/"
body = page_head("{R}", CC_CRUMB, "Clients &amp; Case Studies", "Clients", "") + subnav("{R}", "Clients & Case Studies", p) + f"""
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Client feedback</p><h2>In our clients’ words</h2></div>
      {quotes('{R}')}
    </div>
  </section>
  <section class="section section-white">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Trusted by</p><h2>Our clients</h2></div>
      {logo_wall('{R}')}
    </div>
  </section>
  <section class="section section-fill">
    <div class="wrap">
      <div class="section-head section-head-row"><div><p class="eyebrow">Selected work</p><h2>Case studies</h2></div><a class="link-arrow" href="{L('{R}', 'clients-case-studies/case-studies/')}">All case studies</a></div>
      <div class="cases">{case_cards('{R}', CASES)}</div>
    </div>
  </section>""" + cta_band("{R}")
built.append(page(p, "Clients", "Farsight Africa Group clients and client feedback.", "Clients & Case Studies", body))

# --- Case studies index
p = "clients-case-studies/case-studies/"
body = page_head("{R}", CC_CRUMB, "Clients &amp; Case Studies", "Case Studies", "") + subnav("{R}", "Clients & Case Studies", p) + f"""
  <section class="section">
    <div class="wrap"><div class="cases cases-index">{case_cards('{R}', CASES, 2)}</div></div>
  </section>""" + cta_band("{R}")
built.append(page(p, "Case Studies", "Farsight Africa Group case studies.", "Clients & Case Studies", body))

# --- Case study pages
for c in CASES:
    others = [o for o in CASES if o is not c]
    svc_links = " · ".join(f'<a href="{L("{R}", sp)}">{n}</a>' for n, sp in c["services"])
    logo_f, lw, lh, lalt = c["logo"]
    body = page_head("{R}", CC_CRUMB + [("Case Studies", "clients-case-studies/case-studies/")], "Case study", c["title"], "", None, small=True) + f"""
  <section class="section section-tight">
    <div class="wrap case-layout">
      <aside class="facts case-facts" aria-label="Project facts">
        <img class="facts-logo" src="{{R}}assets/clients/{logo_f}" width="{lw}" height="{lh}" alt="{E(lalt)}">
        <dl>
          <div><dt>Client</dt><dd>{c['client']}</dd></div>
          <div><dt>Country</dt><dd>{c['country']}</dd></div>
          <div><dt>Project implementation</dt><dd>{c['years']}</dd></div>
          <div><dt>Services</dt><dd>{svc_links}</dd></div>
        </dl>
      </aside>
      <article class="prose case-body">
        <h2>Project summary</h2>
        {blocks(c['summary'], '{R}')}
        <figure class="pull">
          <blockquote><p>{c['comment']}</p></blockquote>
          <figcaption>Farsight project manager’s comment</figcaption>
        </figure>
        {('<h2>Outcome</h2>' + blocks(c['outcome'], '{R}')) if c['outcome'] else ''}
      </article>
    </div>
  </section>
  <section class="section section-fill">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">More case studies</p><h2>Other engagements</h2></div>
      <div class="cases cases-3">{case_cards('{R}', others)}</div>
    </div>
  </section>""" + cta_band("{R}")
    built.append(page(c["path"], c["short"], c["teaser"], "Clients & Case Studies", body))

# --- Contact
p = "contact-us/"
body = page_head("{R}", [], "Contact", "Contact Us", "") + f"""
  <section class="section section-tight">
    <div class="wrap contact-grid">
      <div class="contact-direct">
        <h2 class="h-small">Offices</h2>
        <ul class="offices">
          <li class="office"><h3>Nairobi <span class="tag">Headquarters</span></h3><address>7th Floor, FCB Mihrab Tower, Lenana Road</address><a class="tap" href="tel:+254711845333">+254 (0) 711 845 333</a> · <a class="tap" href="https://www.google.com/maps/search/?api=1&amp;query=FCB+Mihrab+Lenana+Road+Nairobi">Map</a></li>
          <li class="office"><h3>Mogadishu</h3><address>Airport Road, Wadajir District</address><a class="tap" href="tel:+252613529999">+252 (0) 61 352 9999</a></li>
          <li class="office"><h3>Monrovia</h3><address>Tubman Boulevard</address><span class="confirm">[CONFIRM] Phone</span></li>
        </ul>
        <p class="contact-email"><a class="tap tap-lg" href="mailto:info@farsightafrica.com">info@farsightafrica.com</a></p>
        <p class="small-note"><span class="confirm">[CONFIRM]</span> WhatsApp number and response time.</p>
      </div>
      <div>
        <h2 class="h-small" id="enquiry-title">Send an enquiry</h2>
        {FORM}
      </div>
    </div>
  </section>
  <section class="section section-fill">
    <div class="wrap where-grid">
      <div>
        <div class="section-head"><p class="eyebrow">Where we work</p><h2>Countries of practice</h2></div>
        <p class="countries">Kenya · Somalia · South Sudan · Liberia · The Gambia · Morocco · United Arab Emirates</p>
        <div class="careers">
          <h3>Working at Farsight</h3>
          <p>Send your CV and cover letter to <a href="mailto:jobs@farsightafrica.com">jobs@farsightafrica.com</a>.</p>
        </div>
      </div>
      <figure class="map-wrap"><img src="{{R}}assets/map.svg" width="720" height="665" loading="lazy" alt="Map of Africa and the Arabian Peninsula highlighting Farsight's countries of practice: Morocco, The Gambia, Liberia, South Sudan, Somalia, Kenya and the United Arab Emirates, with offices in Nairobi, Mogadishu and Monrovia."></figure>
    </div>
  </section>"""
built.append(page(p, "Contact Us", "Contact Farsight Africa Group in Nairobi, Mogadishu and Monrovia.", "Contact", body))

for b in built:
    print(os.path.relpath(b, ROOT))
print(len(built), "pages")
