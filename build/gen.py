import json, os, html, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import *
from icons import icon

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TODAY = datetime.date.today().isoformat()
e = html.escape

def logo_html():
    return 'UNIC<span class="a">A</span> <span class="l">LABS</span>'

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + '</script>'

ORG = {
    "@type": "Organization", "@id": SITE + "/#organization", "name": NAME, "url": SITE + "/",
    "logo": SITE + "/logo.png", "image": SITE + "/og-image.jpg", "email": EMAIL,
    "slogan": TAGLINE, "description": DESCRIPTION,
    "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "email": EMAIL, "availableLanguage": ["it", "en"]},
    "knowsAbout": ["Connettività aziendale", "SD-WAN", "Reti LAN e Wi-Fi", "Cloud ibrido", "Virtualizzazione",
                   "Telefonia VoIP", "Unified communications", "Videosorveglianza", "Controllo accessi",
                   "Backup e disaster recovery", "Business continuity", "Protezione dei dati", "Videoconferenza",
                   "Sale riunioni", "Document management", "Digital signage", "Managed services",
                   "Consulenza IT", "Intelligenza artificiale", "Building automation", "BMS",
                   "Efficienza energetica"],
}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": NAME,
           "inLanguage": "it-IT", "publisher": {"@id": SITE + "/#organization"}}

def head(title, desc, path, extra_ld):
    url = SITE + path
    graph = {"@context": "https://schema.org", "@graph": [ORG, WEBSITE] + extra_ld}
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#050f0b">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:locale" content="it_IT">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Unica Labs — One Partner. Every Solution.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/og-image.jpg">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="text/markdown" href="/llms.txt" title="Sintesi per agenti AI">
<link rel="preload" href="/fonts/montserrat-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/montserrat-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
{ld(graph)}
</head>
<body>
<a class="skip" href="#main">Vai al contenuto</a>
'''

def header(current):
    dd = "".join(f'<a href="/{a["slug"]}/"{" aria-current=\"page\"" if current==a["slug"] else ""}>{icon(a["icon"])}{e(a["en"])}</a>' for a in AREAS)
    return f'''<header class="site-header">
  <div class="wrap">
    <a class="logo" href="/" aria-label="Unica Labs — home">{logo_html()}</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Navigazione principale">
      <div class="dd"><a href="/#soluzioni">Soluzioni</a><div class="dd-panel">{dd}</div></div>
      <a href="/#metodo">Metodo</a>
      <a href="/#modello">Modello</a>
      <a href="/#perche">Perché noi</a>
      <a href="/#faq">FAQ</a>
      <a class="btn" href="/#contatti">Contattaci</a>
    </nav>
  </div>
</header>
'''

def cta_section():
    pill = "".join(f'<div class="pillar">{icon(i)}{e(n)}</div>' for n, i in CTA["pillars"])
    return f'''<section id="contatti" aria-labelledby="cta-t">
  <div class="wrap">
    <div class="cta-box">
      <div>
        <span class="kicker">Let’s talk</span>
        <h2 id="cta-t" style="margin:22px 0 18px">{e(CTA["title"])} <span class="accent">{e(CTA["accent"])}</span></h2>
        <p class="lead">{e(CTA["text"])}</p>
        <p style="margin-top:28px"><a class="btn" href="mailto:{EMAIL}?subject=Richiesta%20informazioni%20dal%20sito">{icon("mail")}{EMAIL}</a></p>
      </div>
      <div class="pillars" aria-label="I nostri ambiti">{pill}</div>
    </div>
  </div>
</section>
'''

def footer():
    areas = "".join(f'<li><a href="/{a["slug"]}/">{e(a["en"])}</a></li>' for a in AREAS)
    return f'''</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot">
      <div>
        <a class="logo" href="/">{logo_html()}</a>
        <p style="margin-top:12px;letter-spacing:.18em;font-size:13px">{TAGLINE}</p>
        <p style="margin-top:16px;max-width:42ch">Un unico partner tecnologico per connettività, sicurezza, workplace, gestione IT, intelligenza artificiale e smart building.</p>
      </div>
      <nav aria-label="Aree di competenza"><h2>Soluzioni</h2><ul>{areas}</ul></nav>
      <div><h2>Contatti</h2><ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{SITE}/">unicalabs.it</a></li>
      </ul></div>
    </div>
    <div class="legal"><span>© {datetime.date.today().year} Unica Labs. Tutti i diritti riservati.</span><span>Questo sito non usa cookie né sistemi di tracciamento.</span></div>
  </div>
</footer>
<script>
(function(){{var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');if(!b)return;
b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)}});
n.addEventListener('click',function(ev){{if(ev.target.tagName==='A'){{n.classList.remove('open');b.setAttribute('aria-expanded','false')}}}});}})();
</script>
</body>
</html>
'''

def area_card(a):
    chips = "".join(f'<span class="chip">{e(m[0])}</span>' for m in a["modules"])
    return f'''<a class="card" href="/{a["slug"]}/">{icon(a["icon"])}<h3>{e(a["en"])}</h3><p>{e(a["intro"])}</p><div class="mods">{chips}</div><span class="more">Scopri {icon("arrow")}</span></a>'''

def write(path, content):
    full = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    if path.endswith(".html"): full = os.path.join(OUT, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

def service_ld(a, path):
    return {
        "@type": "Service", "@id": SITE + path + "#service", "name": f"{a['en']} — {a['it']}",
        "serviceType": a["it"], "description": a["intro"], "url": SITE + path,
        "provider": {"@id": SITE + "/#organization"}, "inLanguage": "it-IT",
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": a["en"], "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"Unica {m[0]}", "description": m[2]}}
            for m in a["modules"]]},
    }

# ---------------- HOME ----------------
def home():
    catalog = {"@type": "OfferCatalog", "@id": SITE + "/#catalog", "name": "Soluzioni Unica Labs",
               "itemListElement": [{"@type": "OfferCatalog", "name": a["en"], "url": f"{SITE}/{a['slug']}/",
                   "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"Unica {m[0]}", "description": m[2]}} for m in a["modules"]]}
                   for a in AREAS]}
    faq = {"@type": "FAQPage", "@id": SITE + "/#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in FAQ]}
    webpage = {"@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": "Unica Labs — One Partner. Every Solution.",
               "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#organization"}, "inLanguage": "it-IT", "dateModified": TODAY}
    ORG_home = dict(ORG); ORG_home["hasOfferCatalog"] = {"@id": SITE + "/#catalog"}
    ORG.update(ORG_home)
    h = head("Unica Labs | Partner tecnologico unico per le imprese — One Partner. Every Solution.",
             "Unica Labs integra connettività, reti, cloud, sicurezza, business continuity, workplace, gestione IT, "
             "intelligenza artificiale e smart building in un unico interlocutore per la tua impresa.",
             "/", [webpage, catalog, faq])
    ch = "".join(f'<div class="card"><span class="num">0{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(CHALLENGE["items"], 1))
    areas = "".join(area_card(a) for a in AREAS)
    steps = "".join(f'<li class="step"><div class="n">{i}</div><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, ic, d) in enumerate(METHOD["steps"], 1))
    biz = "".join(f'<div class="card">{icon(ic)}<h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, ic, d in BUSINESS["items"])
    val = "".join(f'<div class="card">{icon(ic)}<h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, ic, d in VALUE["items"])
    faqh = "".join(f'<details><summary>{e(q)}</summary><p>{e(r)}</p></details>' for q, r in FAQ)
    body = f'''{header("home")}
<main id="main">
<section class="hero" aria-labelledby="hero-t">
  <div class="wrap hero-grid">
    <div>
      <span class="kicker">Partner tecnologico per le imprese</span>
      <h1 id="hero-t">{e(VISION["title"])} <span class="accent">{e(VISION["accent"])}</span></h1>
      <p class="lead">{e(VISION["text"])}</p>
      <div class="actions"><a class="btn" href="#soluzioni">Scopri le soluzioni {icon("arrow")}</a><a class="btn ghost" href="#contatti">Parliamo del tuo progetto</a></div>
    </div>
    <div class="hero-mark" role="img" aria-label="Unica Labs — One Partner. Every Solution. 5 aree di competenza, 17 moduli commerciali">
      <div class="big">{logo_html()}</div>
      <div class="tag">{TAGLINE}</div>
      <div class="stats"><div class="stat"><b>05</b><span>Aree di competenza</span></div><div class="stat"><b>17</b><span>Moduli commerciali</span></div></div>
    </div>
  </div>
  <div class="skyline" role="img" aria-label="Skyline di Milano al tramonto"></div>
</section>

<section id="sfida" aria-labelledby="sfida-t">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">La sfida</span><h2 id="sfida-t">{e(CHALLENGE["title"])} <span class="accent">{e(CHALLENGE["accent"])}</span></h2><p class="lead">{e(CHALLENGE["intro"])}</p></div>
    <div class="grid g2">{ch}</div>
    <p class="closing">{e(CHALLENGE["closing"])}</p>
  </div>
</section>

<section id="soluzioni" aria-labelledby="sol-t">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">Il nostro ecosistema</span><h2 id="sol-t">Un ecosistema <span class="accent">integrato.</span></h2><p class="lead">Soluzioni, servizi e competenze per supportare l’impresa in ogni ambito tecnologico: 5 aree di competenza, 17 moduli commerciali.</p></div>
    <div class="grid areas">{areas}</div>
  </div>
</section>

<section id="metodo" aria-labelledby="met-t">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">Il nostro metodo</span><h2 id="met-t">{e(METHOD["title"])} <span class="accent">{e(METHOD["accent"])}</span></h2><p class="lead">{e(METHOD["text"])}</p></div>
    <ol class="steps" style="list-style:none">{steps}</ol>
  </div>
</section>

<section id="modello" aria-labelledby="mod-t">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">Business model</span><h2 id="mod-t">{e(BUSINESS["title"])} <span class="accent">{e(BUSINESS["accent"])}</span></h2><p class="lead">{e(BUSINESS["text"])}</p></div>
    <div class="grid g3">{biz}</div>
  </div>
</section>

<section id="perche" aria-labelledby="per-t">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">Il nostro valore</span><h2 id="per-t">{e(VALUE["title"])} <span class="accent">{e(VALUE["accent"])}</span></h2><p class="lead">{e(VALUE["text"])}</p></div>
    <div class="grid g4">{val}</div>
  </div>
</section>

<section id="faq" class="faq" aria-labelledby="faq-t">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">Domande frequenti</span><h2 id="faq-t">Unica Labs <span class="accent">in breve.</span></h2></div>
    {faqh}
  </div>
</section>
{cta_section()}
{footer()}'''
    write("/", h + body)

# ---------------- AREA PAGES ----------------
def area_page(a):
    path = f"/{a['slug']}/"
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Soluzioni", "item": SITE + "/#soluzioni"},
        {"@type": "ListItem", "position": 3, "name": a["en"], "item": SITE + path}]}
    webpage = {"@type": "WebPage", "@id": SITE + path + "#webpage", "url": SITE + path, "name": a["meta_title"],
               "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + path + "#service"},
               "breadcrumb": crumbs, "inLanguage": "it-IT", "dateModified": TODAY,
               "primaryImageOfPage": SITE + f"/img/{a['img']}.webp"}
    h = head(a["meta_title"], a["meta_desc"], path, [webpage, service_ld(a, path)])
    mods = "".join(f'''<article class="module" id="{m[0].lower().replace(" ", "-")}">{icon(m[1])}<div><h2><span class="u">UNICA</span> <span class="m">{e(m[0].upper())}</span></h2><p>{e(m[2])}</p></div></article>''' for m in a["modules"])
    others = "".join(area_card(o) for o in AREAS if o is not a)
    steps = "".join(f'<li class="step"><div class="n">{i}</div><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, ic, d) in enumerate(METHOD["steps"], 1))
    body = f'''{header(a["slug"])}
<main id="main">
<section class="hero" aria-labelledby="h1">
  <div class="wrap">
    <nav class="crumbs" aria-label="Percorso"><ol><li><a href="/">Home</a></li><li><a href="/#soluzioni">Soluzioni</a></li><li aria-current="page">{e(a["en"])}</li></ol></nav>
    <div class="split">
      <div>
        <span class="kicker">{e(a["kicker"])}</span>
        <h1 id="h1" style="margin:26px 0 22px">{e(a["h1"])} <span class="accent">{e(a["h1_accent"])}</span></h1>
        <p class="lead">{e(a["intro"])}</p>
        <div style="margin-top:30px"><a class="btn" href="#contatti">Richiedi una consulenza {icon("arrow")}</a></div>
      </div>
      <figure class="photo"><img src="/img/{a["img"]}.webp" alt="{e(a["img_alt"])}" width="720" height="450" fetchpriority="high"></figure>
    </div>
  </div>
</section>
<section aria-label="Moduli {e(a["en"])}" style="padding-top:40px">
  <div class="wrap grid">{mods}</div>
</section>
<section aria-labelledby="met-t">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">Come lavoriamo</span><h2 id="met-t">{e(METHOD["title"])} <span class="accent">{e(METHOD["accent"])}</span></h2></div>
    <ol class="steps" style="list-style:none">{steps}</ol>
  </div>
</section>
{cta_section()}
<section aria-labelledby="alt-t" style="padding-top:20px">
  <div class="wrap">
    <div class="sec-head"><span class="kicker">Ecosistema</span><h2 id="alt-t">Le altre aree di competenza</h2></div>
    <div class="grid g2">{others}</div>
  </div>
</section>
{footer()}'''
    write(path, h + body)

def page404():
    h = head("Pagina non trovata | Unica Labs", "La pagina richiesta non esiste.", "/404.html", [])
    h = h.replace('content="index, follow, max-image-preview:large, max-snippet:-1"', 'content="noindex"')
    body = f'''{header("")}
<main id="main"><section class="hero"><div class="wrap"><span class="kicker">Errore 404</span>
<h1 style="margin:26px 0 22px">Pagina <span class="accent">non trovata.</span></h1>
<p class="lead">L’indirizzo richiesto non esiste o è stato spostato.</p>
<p style="margin-top:30px"><a class="btn" href="/">Torna alla home {icon("arrow")}</a></p></div></section>
{footer()}'''
    write("/404.html", h + body)

# ---------------- AI / SEO FILES ----------------
def text_files():
    pages = ["/"] + [f"/{a['slug']}/" for a in AREAS]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in pages:
        sm.append(f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{'1.0' if p=='/' else '0.8'}</priority></url>")
    sm.append("</urlset>")
    open(f"{OUT}/sitemap.xml", "w").write("\n".join(sm) + "\n")

    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot",
            "anthropic-ai", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended",
            "Bingbot", "CCBot", "meta-externalagent", "MistralAI-User", "DuckAssistBot"]
    rb = "# Unica Labs — tutti i crawler, inclusi motori di ricerca e agenti AI, sono benvenuti.\n\nUser-agent: *\nAllow: /\n\n"
    rb += "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots)
    rb += f"Sitemap: {SITE}/sitemap.xml\n"
    open(f"{OUT}/robots.txt", "w").write(rb)

    # llms.txt (standard llmstxt.org)
    L = [f"# {NAME}", "", f"> {DESCRIPTION} Slogan: “{TAGLINE}”", "",
         "Unica Labs è un unico interlocutore che integra competenze, soluzioni e servizi tecnologici, affiancando "
         "l’impresa e il suo reparto IT in ogni fase: analisi, progettazione, realizzazione e gestione nel tempo. "
         "L’offerta comprende 5 aree di competenza e 17 moduli commerciali, disponibili in acquisto, noleggio "
         "(ove disponibile) o come servizi gestiti.", "",
         f"- Contatto commerciale: {EMAIL}", f"- Sito: {SITE}/", "", "## Aree di competenza", ""]
    for a in AREAS:
        mods = ", ".join("Unica " + m[0] for m in a["modules"])
        L.append(f"- [{a['en']}]({SITE}/{a['slug']}/): {a['intro']} Moduli: {mods}.")
    L += ["", "## Pagine principali", "",
          f"- [Home]({SITE}/): panoramica, metodo, modello commerciale, valore, FAQ e contatti",
          f"- [Contenuto completo in Markdown]({SITE}/llms-full.txt): tutte le informazioni del sito in un unico file", "",
          "## Optional", "", f"- [Sitemap]({SITE}/sitemap.xml)"]
    open(f"{OUT}/llms.txt", "w").write("\n".join(L) + "\n")

    F = [f"# {NAME} — {TAGLINE}", "", DESCRIPTION, "", f"Contatto: {EMAIL} · {SITE}/", "",
         "## La sfida", "", f"{CHALLENGE['title']} {CHALLENGE['accent']} {CHALLENGE['intro']}", ""]
    F += [f"- **{t}**: {d}" for t, d in CHALLENGE["items"]]
    F += ["", "## Visione", "", f"{VISION['title']} {VISION['accent']} {VISION['text']}", "",
          "## Metodo", "", METHOD["text"], ""]
    F += [f"{i}. **{t}** — {d}" for i, (t, _, d) in enumerate(METHOD["steps"], 1)]
    F += ["", "## Soluzioni (5 aree, 17 moduli)", ""]
    for a in AREAS:
        F += [f"### {a['en']} ({a['it']})", "", a["intro"], f"Pagina: {SITE}/{a['slug']}/", ""]
        F += [f"- **Unica {m[0]}**: {m[2]}" for m in a["modules"]]
        F.append("")
    F += ["## Modello commerciale", "", BUSINESS["text"], ""]
    F += [f"- **{t}**: {d}" for t, _, d in BUSINESS["items"]]
    F += ["", "## Perché scegliere Unica Labs", "", VALUE["text"], ""]
    F += [f"- **{t}**: {d}" for t, _, d in VALUE["items"]]
    F += ["", "## Domande frequenti", ""]
    for q, r in FAQ: F += [f"### {q}", "", r, ""]
    F += ["## Contatti", "", f"{CTA['title']} {CTA['accent']} {CTA['text']}", f"Email: {EMAIL}"]
    open(f"{OUT}/llms-full.txt", "w").write("\n".join(F) + "\n")

    open(f"{OUT}/site.webmanifest", "w").write(json.dumps({
        "name": NAME, "short_name": NAME, "start_url": "/", "display": "standalone",
        "background_color": "#050f0b", "theme_color": "#050f0b",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1))


home()
for a in AREAS: area_page(a)
page404()
text_files()
print("ok")
