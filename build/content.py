# Contenuti del sito Unica Labs — tratti dalla presentazione commerciale (13 slide).
SITE = "https://unicalabs.it"
NAME = "Unica Labs"
TAGLINE = "One Partner. Every Solution."
EMAIL = "info@unicalabs.it"
DESCRIPTION = ("Unica Labs è il partner tecnologico unico per le imprese: connettività, reti, cloud, "
               "telefonia, sicurezza, business continuity, workplace, gestione IT, consulenza, "
               "intelligenza artificiale, smart building ed efficienza energetica.")

CHALLENGE = {
    "title": "La tecnologia dovrebbe semplificare il business.",
    "accent": "Non complicarlo.",
    "intro": "Le imprese devono gestire un numero crescente di tecnologie, operatori, fornitori e contratti.",
    "items": [
        ("Fornitori frammentati", "Molteplici interlocutori da coordinare."),
        ("Complessità contrattuale", "Contratti, scadenze e condizioni differenti."),
        ("Tecnologie non integrate", "Sistemi e infrastrutture spesso indipendenti."),
        ("Tempo e risorse", "Un crescente impegno nella gestione operativa."),
    ],
    "closing": "È il momento di cambiare prospettiva.",
}

VISION = {
    "title": "Molte competenze.",
    "accent": "Un unico interlocutore.",
    "text": ("Un partner tecnologico che integra competenze, soluzioni e servizi, affiancando "
             "l’impresa e il suo reparto IT in ogni fase del percorso."),
}

METHOD = {
    "title": "Dall’esigenza",
    "accent": "alla soluzione.",
    "text": ("Un metodo strutturato per trasformare le esigenze dell’impresa in soluzioni concrete, "
             "integrate e sostenibili."),
    "steps": [
        ("Understand", "search", "Analizziamo le esigenze, le infrastrutture esistenti e gli obiettivi aziendali."),
        ("Design", "layers", "Progettiamo soluzioni coerenti con le necessità operative ed economiche."),
        ("Implement", "gear", "Coordiniamo tecnologie, fornitori e competenze specialistiche."),
        ("Manage", "headset", "Accompagniamo il cliente nel tempo, attraverso servizi di gestione e assistenza."),
    ],
}

AREAS = [
    {
        "slug": "infrastruttura-connettivita",
        "en": "Infrastructure & Connectivity",
        "it": "Infrastruttura e connettività",
        "icon": "server",
        "img": "datacenter", "img_alt": "Data center con rack di server illuminati",
        "kicker": "Infrastructure & Connectivity",
        "h1": "Le fondamenta digitali", "h1_accent": "dell’impresa.",
        "intro": "Connettività, reti, cloud e comunicazioni per un’infrastruttura solida, sicura e sempre operativa.",
        "meta_title": "Connettività, reti aziendali, cloud e telefonia VoIP | Unica Labs",
        "meta_desc": ("Fibra, mobile, SD-WAN e collegamenti multisede; reti LAN e Wi-Fi; server, virtualizzazione "
                      "e cloud pubblico, privato e ibrido; telefonia aziendale VoIP e unified communications."),
        "modules": [
            ("Connect", "globe", "Connettività, fibra, mobile, SD-WAN e collegamenti multisede."),
            ("Network", "network", "Infrastrutture LAN, Wi-Fi, switching e reti aziendali."),
            ("Cloud", "cloud", "Server, virtualizzazione e infrastrutture cloud pubbliche, private e ibride."),
            ("Voice", "phone", "Telefonia aziendale, VoIP e unified communications."),
        ],
    },
    {
        "slug": "sicurezza-business-continuity",
        "en": "Security & Business Continuity",
        "it": "Sicurezza e business continuity",
        "icon": "shield",
        "img": "security", "img_alt": "Telecamera di videosorveglianza a cupola su un edificio",
        "kicker": "Security & Business Continuity",
        "h1": "Sicurezza, continuità", "h1_accent": "e protezione.",
        "intro": ("Soluzioni integrate per proteggere persone, dati e infrastrutture, assicurando la continuità "
                  "operativa del business."),
        "meta_title": "Videosorveglianza, backup, disaster recovery e protezione dati | Unica Labs",
        "meta_desc": ("Videosorveglianza, controllo accessi e sicurezza degli ambienti; infrastrutture resilienti, "
                      "backup e piani di ripristino; protezione di dati, accessi e sistemi con monitoraggio continuo."),
        "modules": [
            ("Security", "shield", "Videosorveglianza, controllo accessi e sicurezza degli ambienti."),
            ("Continuity", "sync", "Infrastrutture resilienti, backup e piani di ripristino per la continuità operativa."),
            ("Protect", "dblock", "Protezione dei dati, accessi e sistemi, con gestione centralizzata e monitoraggio continuo."),
        ],
    },
    {
        "slug": "workplace-collaboration",
        "en": "Workplace & Collaboration",
        "it": "Workplace e collaborazione",
        "icon": "people",
        "img": "workplace", "img_alt": "Sala riunioni con display per videoconferenza",
        "kicker": "Workplace & Collaboration",
        "h1": "Ambienti di lavoro più efficienti,", "h1_accent": "connessi e flessibili.",
        "intro": "Tecnologie e servizi che migliorano la collaborazione, la produttività e l’esperienza delle persone.",
        "meta_title": "Sale riunioni, videoconferenza, stampa e digital signage | Unica Labs",
        "meta_desc": ("Sale riunioni, videoconferenza e ambienti ibridi; collaborazione in tempo reale anche da remoto; "
                      "stampa sicura e document management; comunicazione visiva e digital signage."),
        "modules": [
            ("Work", "video", "Sale riunioni, videoconferenza e ambienti ibridi."),
            ("Meet", "people", "Collaborazione in tempo reale, anche da remoto."),
            ("Print", "printer", "Stampa sicura e servizi di document management."),
            ("Display", "monitor", "Comunicazione visiva, informazioni e digital signage."),
        ],
    },
    {
        "slug": "gestione-consulenza-innovazione",
        "en": "Management & Innovation",
        "it": "Gestione, consulenza e innovazione",
        "icon": "chip",
        "img": "management", "img_alt": "Laptop con dashboard di monitoraggio in un ufficio",
        "kicker": "Management & Innovation",
        "h1": "Gestione, consulenza", "h1_accent": "e innovazione.",
        "intro": ("Competenze e strumenti per governare i sistemi, sviluppare i progetti e introdurre tecnologie "
                  "ad alto valore, come l’intelligenza artificiale."),
        "meta_title": "Managed services, consulenza IT, progetti chiavi in mano e AI | Unica Labs",
        "meta_desc": ("Gestione integrata degli impianti e monitoraggio; consulenza tecnologica e assessment; "
                      "progettazione e realizzazione di soluzioni complesse chiavi in mano; soluzioni di intelligenza artificiale."),
        "modules": [
            ("Manage", "gear", "Gestione integrata degli impianti, monitoraggio e operation continuativa."),
            ("Advisory", "people", "Consulenza tecnologica, assessment e strategie di evoluzione."),
            ("Project", "layers", "Progettazione, coordinamento e realizzazione di soluzioni complesse, chiavi in mano."),
            ("AI", "ai", "Soluzioni di intelligenza artificiale per sicurezza, efficienza operativa e nuovi servizi digitali."),
        ],
    },
    {
        "slug": "smart-building-energia",
        "en": "Smart Building & Energy",
        "it": "Smart building ed energia",
        "icon": "building",
        "img": "building", "img_alt": "Edificio moderno con facciata vetrata illuminata",
        "kicker": "Smart Building & Energy",
        "h1": "Edifici intelligenti.", "h1_accent": "Risorse ottimizzate.",
        "intro": ("Automazione degli edifici e gestione intelligente dell’energia per spazi più efficienti "
                  "e sostenibili."),
        "meta_title": "Building automation, BMS ed efficienza energetica | Unica Labs",
        "meta_desc": ("Automazione degli edifici, BMS, illuminazione intelligente e integrazione degli impianti; "
                      "analisi dei consumi, efficientamento energetico e soluzioni per la sostenibilità."),
        "modules": [
            ("Building", "building", "Automazione degli edifici, BMS, illuminazione intelligente e integrazione degli impianti."),
            ("Energy", "leafbars", "Analisi dei consumi, efficientamento energetico e soluzioni per la sostenibilità attraverso partner specialistici."),
        ],
    },
]

BUSINESS = {
    "title": "La tecnologia,", "accent": "alle tue condizioni.",
    "text": "Un modello commerciale flessibile, che si adatta alle esigenze del tuo business.",
    "items": [
        ("Purchase", "cart", "Acquisto diretto delle soluzioni tecnologiche."),
        ("Rental", "calendar", "Formule di noleggio, ove disponibili."),
        ("Managed Services", "handgear", "Servizi continuativi con canoni e livelli di assistenza concordati."),
    ],
}

VALUE = {
    "title": "Perché scegliere", "accent": "Unica Labs.",
    "text": "Un partner unico per trasformare la tecnologia in valore concreto, nel tempo.",
    "items": [
        ("Visione integrata", "target", "Tecnologie, spazi e servizi in un’unica strategia."),
        ("Competenze multidisciplinari", "people", "Un team con esperienza, metodo e continuità."),
        ("Soluzioni scalabili", "bars", "Dalla singola sede a progetti complessi, con la massima flessibilità."),
        ("Affidabilità nel tempo", "shield", "Servizi, assistenza e supporto costante per la massima continuità operativa."),
    ],
}

CTA = {
    "title": "Parliamo del", "accent": "tuo prossimo progetto.",
    "text": ("Siamo al tuo fianco per analizzare le esigenze, definire le soluzioni e trasformarle "
             "in risultati concreti."),
    "pillars": [("Spazi", "building"), ("Persone", "people"), ("Servizi", "gear"), ("Sostenibilità", "leaf")],
}

FAQ = [
    ("Che cosa fa Unica Labs?",
     "Unica Labs è un partner tecnologico per le imprese che integra competenze, soluzioni e servizi in un unico "
     "interlocutore. Affianca l’azienda e il suo reparto IT in ogni fase: analisi, progettazione, realizzazione "
     "e gestione nel tempo."),
    ("Quali servizi offre Unica Labs?",
     "L’offerta è organizzata in 5 aree di competenza e 17 moduli: Infrastructure & Connectivity (Connect, Network, "
     "Cloud, Voice), Security & Business Continuity (Security, Continuity, Protect), Workplace & Collaboration "
     "(Work, Meet, Print, Display), Management & Innovation (Manage, Advisory, Project, AI) e Smart Building & "
     "Energy (Building, Energy)."),
    ("Come lavora Unica Labs?",
     "Con un metodo in quattro fasi: Understand (analisi di esigenze, infrastrutture esistenti e obiettivi), "
     "Design (progettazione di soluzioni coerenti con le necessità operative ed economiche), Implement "
     "(coordinamento di tecnologie, fornitori e competenze specialistiche) e Manage (gestione e assistenza nel tempo)."),
    ("Quali formule commerciali sono disponibili?",
     "Tre modelli: acquisto diretto delle soluzioni (Purchase), formule di noleggio ove disponibili (Rental) e "
     "servizi gestiti continuativi con canoni e livelli di assistenza concordati (Managed Services)."),
    ("Unica Labs si occupa di intelligenza artificiale?",
     "Sì. Il modulo Unica AI propone soluzioni di intelligenza artificiale per la sicurezza, l’efficienza "
     "operativa e lo sviluppo di nuovi servizi digitali."),
    ("Come posso contattare Unica Labs?",
     "Scrivendo a info@unicalabs.it per raccontare il progetto: il team analizza le esigenze e propone la soluzione."),
]
