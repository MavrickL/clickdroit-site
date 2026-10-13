# Génère les pages statiques. Usage : python3 tools/build.py
# Langage visuel inspiré de leftclick.ai (monochrome, DM Sans, pilules noires, cartes grises arrondies,
# section sombre, bandeau défilant, étapes numérotées). Aucun texte, logo ou image repris.
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://clickdroit.fr"
CAL = "https://calendar.app.google/JHuG9bUeeuBmpLwKA"
BTN = 'inline-flex items-center gap-2 bg-ink text-white pl-6 pr-2 py-2 rounded-full font-medium hover:bg-black transition group'
ARROW = '<span class="w-8 h-8 rounded-full bg-white text-ink flex items-center justify-center group-hover:translate-x-0.5 transition">→</span>'
BTN2 = 'inline-flex items-center bg-white text-ink border border-line px-6 py-3 rounded-full font-medium hover:bg-soft transition'
def cta(t="Réserver mon audit gratuit", h="/audit-gratuit", ext=False):
    x = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a href="{h}"{x} class="{BTN}">{t}{ARROW}</a>'
def H1(t, sub="", center=False):
    c = 'text-center mx-auto' if center else ''
    return f'<section class="pt-20 md:pt-28 pb-10 reveal {c}"><h1 class="text-[2.6rem] leading-[1.05] md:text-7xl font-semibold tracking-tight text-ink max-w-4xl {c}">{t}</h1>' + (f'<p class="mt-6 text-lg text-mute max-w-2xl {c}">{sub}</p>' if sub else '') + '</section>'
def S(t, body, dark=False):
    if dark:
        return f'<section class="my-16 -mx-6 md:mx-0 bg-night text-white md:rounded-[2em] px-6 md:px-14 py-16 reveal"><h2 class="text-3xl md:text-5xl font-semibold tracking-tight mb-8 text-center">{t}</h2><div class="text-white/70 space-y-4 dark">{body}</div></section>'
    return f'<section class="py-14 md:py-20 reveal"><h2 class="text-3xl md:text-5xl font-semibold tracking-tight text-ink mb-8 max-w-3xl">{t}</h2><div class="text-mute text-[1.05rem] leading-relaxed space-y-4">{body}</div></section>'
def UL(items): return '<ul class="grid md:grid-cols-2 gap-3">' + ''.join(f'<li class="bg-soft rounded-[1em] p-5 text-ink/80">{i}</li>' for i in items) + '</ul>'
def TABLE(head, rows): return '<div class="overflow-x-auto rounded-[1em] bg-soft p-2"><table class="w-full text-left text-sm"><thead><tr>' + ''.join(f'<th class="p-4 font-semibold text-ink">{h}</th>' for h in head) + '</tr></thead><tbody>' + ''.join('<tr class="border-t border-line">' + ''.join(f'<td class="p-4 align-top">{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>'
def P(t): return f'<p class="max-w-3xl">{t}</p>'
def TODO(t): return f'<!-- TODO [need: {t}] -->'
def FINAL(t): return f'<section class="my-20 -mx-6 md:mx-0 bg-night text-white md:rounded-[2em] px-6 py-20 text-center reveal"><p class="text-3xl md:text-5xl font-semibold tracking-tight max-w-3xl mx-auto">{t}</p><a href="/audit-gratuit" class="mt-10 inline-flex items-center gap-2 bg-white text-ink pl-6 pr-2 py-2 rounded-full font-medium group">Réserver mon audit gratuit<span class="w-8 h-8 rounded-full bg-ink text-white flex items-center justify-center">→</span></a></section>'
def STEPS(items): return '<div class="grid md:grid-cols-4 gap-4">' + ''.join(f'<div class="bg-soft rounded-[1em] p-6 flex flex-col gap-3"><span class="w-9 h-9 rounded-full bg-ink text-white text-sm flex items-center justify-center">{i+1}</span><h3 class="font-semibold text-ink">{a}</h3><p class="text-sm text-mute">{b}</p></div>' for i,(a,b) in enumerate(items)) + '</div>'
def MARQUEE(words): 
    row = ''.join(f'<span class="mx-8 text-mute whitespace-nowrap">{w}</span>' for w in words)
    return f'<div class="overflow-hidden border-y border-line py-5 my-6 -mx-6 md:mx-0"><div class="marquee flex w-max">{row}{row}</div></div>'

NAV = [("/experts-comptables","Experts-comptables"),("/btp-assistant-vocal","BTP"),("/offres-tarifs","Offres &amp; tarifs"),("/a-propos","À propos"),("/contact","Contact")]
ORG = {"@context":"https://schema.org","@type":"Organization","name":"CLICKDROIT","url":SITE+"/","description":"Intégrateur IA et automatisation pour cabinets d'expertise comptable et entreprises du BTP."}
def page(path, title, desc, body):
    nav = ''.join(f'<a href="{h}" class="hover:text-ink transition">{t}</a>' for h,t in NAV)
    fnav = ''.join(f'<li><a href="{h}" class="hover:text-white">{t}</a></li>' for h,t in NAV)
    url = SITE + path
    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="CLICKDROIT">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>tailwind.config={{theme:{{extend:{{fontFamily:{{sans:['"DM Sans"','Arial','sans-serif']}},colors:{{ink:'#111113',night:'#0a0a0c',soft:'#f0f0f2',paper:'#f7f7f8',line:'#e8e8e8',mute:'#5f5f66'}}}}}}}}</script>
<style>
body{{letter-spacing:-.01em}}
@keyframes marqueeScroll{{from{{transform:translateX(0)}}to{{transform:translateX(-50%)}}}}
.marquee{{animation:marqueeScroll 30s linear infinite}}
.reveal{{opacity:1;transform:none;transition:opacity .7s ease,transform .7s ease}}
.js .reveal:not(.in){{opacity:0;transform:translateY(24px)}}
.dark li{{background:#141420;color:rgba(255,255,255,.8)}}
@media (prefers-reduced-motion:reduce){{.marquee{{animation:none}}.js .reveal:not(.in){{opacity:1;transform:none}}}}
</style>
<script>document.documentElement.classList.add('js');addEventListener('DOMContentLoaded',()=>{{const o=new IntersectionObserver(e=>e.forEach(x=>{{if(x.isIntersecting){{x.target.classList.add('in');o.unobserve(x.target)}}}}),{{threshold:.08}});document.querySelectorAll('.reveal').forEach(el=>o.observe(el));setTimeout(()=>document.querySelectorAll('.reveal').forEach(el=>el.classList.add('in')),2500)}})</script>
<script type="application/ld+json">{json.dumps(ORG, ensure_ascii=False)}</script>
</head>
<body class="bg-white text-ink antialiased font-sans">
<header class="sticky top-0 z-20 bg-white/80 backdrop-blur border-b border-line/70">
<div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between gap-4">
<a href="/" class="text-lg font-bold tracking-tight">CLICKDROIT</a>
<nav class="hidden md:flex gap-7 text-sm text-mute">{nav}</nav>
<a href="/audit-gratuit" class="bg-ink text-white px-5 py-2 rounded-full text-sm font-medium hover:bg-black transition">Audit gratuit</a>
</div>
<nav class="md:hidden max-w-6xl mx-auto px-6 pb-3 flex gap-5 overflow-x-auto text-sm text-mute whitespace-nowrap">{nav}</nav>
</header>
<main class="max-w-6xl mx-auto px-6">
{body}
</main>
<footer class="bg-night text-white/60 mt-10">
<div class="max-w-6xl mx-auto px-6 py-16 grid md:grid-cols-3 gap-10 text-sm">
<div><p class="text-white text-lg font-bold tracking-tight">CLICKDROIT</p><a href="/audit-gratuit" class="mt-6 inline-flex bg-white text-ink px-5 py-2 rounded-full font-medium">Audit gratuit</a></div>
<ul class="space-y-2">{fnav}</ul>
<ul class="space-y-2"><li><a href="/mentions-legales" class="hover:text-white">Mentions légales et données personnelles</a></li><li><a href="/contact" class="hover:text-white">Contact</a></li></ul>
</div>
<div class="max-w-6xl mx-auto px-6 pb-8 text-xs text-white/40">© 2026 CLICKDROIT</div>
</footer>
</body>
</html>
'''
    d = os.path.join(ROOT, path.strip('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(html)
    return path

pages = []

# ---------- Accueil
pages.append(page("/", "CLICKDROIT : automatisation IA pour cabinets et BTP",
 "Nous relions vos outils et automatisons relances, tri des mails et devis. Audit gratuit de 45 min, puis projet à prix fixe sur un périmètre écrit.",
 H1("Vos outils, reliés. Vos tâches répétitives, automatisées.", center=True, sub=
    "CLICKDROIT automatise ce qui se passe entre vos logiciels, pour les cabinets d'expertise comptable et les entreprises du BTP. En 45 minutes, nous identifions avec vous 3 à 5 automatisations et le temps qu'elles peuvent faire gagner. Si vous avancez, c'est à prix fixe, sur un périmètre écrit.")
 + f'<div class="flex flex-wrap justify-center gap-3 -mt-2">{cta()}{cta("Voir les offres et tarifs","/offres-tarifs").replace(BTN,BTN2)}</div>'
 + '<p class="mt-8 mb-10 text-sm text-mute max-w-2xl mx-auto text-center">Depuis le 1er septembre 2026, la réception des factures électroniques est obligatoire (CNOEC, enquête flash, septembre 2026). Ces flux structurés peuvent désormais être traités automatiquement.</p>'
 + MARQUEE(["Logiciel de production","Messagerie","GED","Outil de devis","Tableur","Agenda","Signature électronique","Portail client","n8n","Make"])
 + S("Le temps se perd entre vos logiciels", P("Vous avez déjà un logiciel de production, une messagerie, un outil de devis, un tableur. Le temps part ailleurs : relancer des pièces, trier des mails, recopier un devis, rédiger un compte rendu. Nous ne remplaçons aucun de vos logiciels. Nous les relions, et nous retirons les étapes manuelles entre eux."))
 + S("Deux secteurs, pas plus", '<div class="grid md:grid-cols-2 gap-6">'
   '<a href="/experts-comptables" class="block p-6 rounded-[1em] bg-soft hover:bg-line transition"><h3 class="text-xl font-semibold text-ink">Cabinets d\'expertise comptable</h3><p class="mt-2">Relances de pièces, tri des mails, onboarding client, flux de factures électroniques, reporting, cadre d\'usage de l\'IA.</p><p class="mt-4 text-ink underline underline-offset-4 font-semibold">Pour les experts-comptables →</p></a>'
   '<a href="/btp-assistant-vocal" class="block p-6 rounded-[1em] bg-soft hover:bg-line transition"><h3 class="text-xl font-semibold text-ink">Entreprises du BTP</h3><p class="mt-2">Un assistant vocal : vous dictez un devis ou un compte rendu de chantier depuis votre téléphone, vous recevez un brouillon, vous le validez.</p><p class="mt-4 text-ink underline underline-offset-4 font-semibold">Pour le BTP →</p></a></div>')
 + S("Comment ça se passe", STEPS([("Audit gratuit (45 min)","Vos outils, vos tâches répétitives, vos volumes."),("Rapport sous 72 heures ouvrées","3 à 5 automatisations, le gain estimé et son calcul, avec vos chiffres. Ce sont des estimations à valider, pas des promesses."),("Projet à prix fixe","4 à 6 semaines, un flux en production à la fois, une personne de votre équipe qui valide."),("Bilan à 30 jours","Le temps réellement gagné, mesuré et comparé à l'estimation.")]))
 + S("Vos données restent sous contrôle", UL(["n8n peut être installé sur un compte à votre nom : vos données restent dans votre infrastructure.","Un accord de traitement des données (DPA, article 28 du RGPD) est signé avant tout démarrage.","Pour tout ce qui vous engage (devis, réponse fiscale, relance d'impayé), l'IA prépare et un humain valide, au moins pendant les 3 premiers mois.","Les assistants vocaux se présentent toujours comme des assistants automatisés.","Vous pouvez récupérer l'export complet de vos workflows à tout moment."]), dark=True)
 + S("Des prix affichés", P("Déploiement Express : 5 000 EUR HT pour 3 automatisations, livrées en 4 à 6 semaines, avec 30 jours de garantie. Ou Déploiement Progressif : 1 400 EUR HT par mois pendant 4 mois.") + '<p><a href="/offres-tarifs" class="text-ink underline underline-offset-4 font-semibold">Voir le détail →</a></p>')
 + S("Pourquoi vous ne verrez pas de témoignages ici", P("CLICKDROIT démarre. Il n'y a pas encore de clients à citer, et nous n'en inventerons pas. C'est pour cela que l'audit est gratuit, que le prix est fixe et que la garantie de 30 jours est incluse : vous jugez sur pièces avant de signer."))
 + FINAL("Commencez par 45 minutes. Vous repartez avec 3 à 5 automatisations chiffrées, que vous travailliez avec nous ou non.")))

# ---------- Experts-comptables
pages.append(page("/experts-comptables", "Automatisation pour cabinets d'expertise comptable",
 "Relances de pièces, tri des mails, onboarding, factures électroniques : des flux automatisés et un usage de l'IA encadré. Audit gratuit de 45 min.",
 H1("Automatisez ce qui se passe autour de votre logiciel de production.","Relances de pièces, tri des mails, onboarding, factures électroniques. Nous relions vos outils, nous encadrons l'usage de l'IA, et vos données peuvent rester chez vous.") + f'<div class="mb-10">{cta()}</div>'
 + S("Où en sont les cabinets", UL(["62 % des cabinets utilisent des logiciels intégrant de l'IA (OMECA, baromètre des métiers, 301 cabinets, publié en juillet 2025).","Dans 54 % des cabinets qui utilisent l'IA, les usages sont des initiatives individuelles non encadrées (Groupe SVP, baromètre IA et experts-comptables, 18 septembre 2026 ; échantillon de 80 répondants).","La réception des factures électroniques est obligatoire depuis le 1er septembre 2026 (CNOEC, enquête flash, septembre 2026)."]) + P("La question n'est plus de savoir s'il faut y aller, mais comment relier ces outils et cadrer ces usages."))
 + S("Ce que nous automatisons", TABLE(["Module","Ce qu'il fait"],[["Relances pièces","Relances programmées par client et par échéance, suivi des pièces reçues"],["Tri des mails","Classement, étiquetage, extraction des pièces jointes vers la GED"],["Onboarding client","Formulaire, génération de la lettre de mission, collecte des documents, création du dossier"],["Agent FAQ client","Réponses de premier niveau sur une base documentaire validée par le cabinet, avec escalade vers un collaborateur"],["Flux factures électroniques","Tri, rapprochement, alertes, tableau de bord"],["Reporting client","Tableau de bord mensuel généré et envoyé"],["Cadre IA","Charte d'usage, liste d'outils validés, formation"]]) + P("Le gain de chaque module se calcule pendant l'audit, avec vos volumes : nombre de relances par mois × temps par relance, par exemple. C'est une estimation à valider, mesurée ensuite au bilan à 30 jours."))
 + S("Vos outils", P("Messagerie (Microsoft 365, Google Workspace), GED, logiciel de production comptable et plateforme de facturation électronique <strong>selon les API ou exports disponibles</strong>, signature électronique, formulaires, portail client. Si un logiciel n'a ni API ni export exploitable, nous vous le disons dès l'audit et nous proposons une alternative."))
 + S("Secret professionnel", UL(["Hébergement de n8n sur un compte au nom du cabinet possible.","Aucun document client envoyé vers un outil IA que le cabinet n'a pas validé.","DPA signé avant le démarrage, sous-traitants listés.","CLICKDROIT n'est jamais l'auteur d'une écriture ni d'un conseil comptable : l'IA prépare, le collaborateur valide."]))
 + S("Prix", P("Déploiement Express : 5 000 EUR HT, 3 automatisations, 4 à 6 semaines. Charte d'usage de l'IA + atelier de 2 h : 900 EUR HT en option.") + '<p><a href="/offres-tarifs" class="text-ink underline underline-offset-4 font-semibold">Offres et tarifs →</a></p>')
 + FINAL("45 minutes pour chiffrer 3 à 5 automatisations dans votre cabinet.")))

# ---------- BTP
pages.append(page("/btp-assistant-vocal", "Assistant vocal BTP : devis et comptes rendus dictés",
 "Dictez vos devis et comptes rendus de chantier depuis votre téléphone, recevez un brouillon à valider. Sans nouveau logiciel. Audit gratuit.",
 H1("Vous dictez depuis le chantier. Le devis vous attend, prêt à vérifier.","Un assistant vocal pour les artisans structurés et les PME du BTP. Pas de nouveau logiciel : votre téléphone suffit. Vous dictez, vous recevez, vous validez.") + f'<div class="mb-10">{cta()}</div>'
 + S("Ce que fait l'assistant", '<div class="grid md:grid-cols-2 gap-6">' + ''.join(f'<div class="p-6 rounded-[1em] bg-soft"><h3 class="text-lg font-semibold text-ink">{a}</h3><p class="mt-2">{b}</p></div>' for a,b in [("Devis dicté","Vous laissez un message vocal en sortant du chantier. L'assistant le transcrit et prépare un brouillon de devis dans votre logiciel ou votre modèle existant. Vous le relisez avant tout envoi."),("Compte rendu de chantier dicté","Une dictée et quelques photos. Le compte rendu est rédigé, envoyé au client et archivé."),("Relances","Devis, acomptes, factures : un agent vocal passe les appels de relance en se présentant comme un assistant automatisé, ou vous prépare une liste d'appels. Tout est tracé."),("Appels manqués","Pendant que vous êtes sur le toit, l'assistant prend le message, qualifie la demande et planifie le rappel.")]) + '</div>')
 + S("Avec ce que vous utilisez déjà", P("Téléphone, messagerie vocale, SMS ou messagerie instantanée, logiciel de devis et facturation (ou modèle de devis si vous n'en avez pas), agenda, stockage photos. La prise en main se fait sur le terrain ou par téléphone, en 15 minutes, avec un mode d'emploi d'une page."))
 + S("Repère", P("L'IA est utilisée par 3 % des entreprises de la construction de 10 salariés ou plus (INSEE, données 2024, publiées en 2025)."))
 + S("Ce que nous vérifions avant de nous engager", UL(["La compréhension en conditions réelles (bruit de chantier, accents) : test sur 10 enregistrements réels avant engagement.","Les personnes appelées sont informées qu'elles parlent à un assistant automatisé, et en cas d'enregistrement.","Les coûts de minutes téléphoniques sont payés au réel, sans marge cachée.","Aucun devis ne part sans votre validation."]))
 + S("Exemple de calcul (fait pendant l'audit, avec vos chiffres)", P("Si vous déclarez 8 devis par semaine et 20 à 30 minutes gagnées par devis, le gain estimé est de 2 à 4 heures par semaine. C'est une estimation à valider, pas un résultat constaté."))
 + S("Prix", P("Déploiement Express : 5 000 EUR HT. Module vocal supplémentaire : 2 000 EUR HT, hors minutes téléphoniques.") + '<p><a href="/offres-tarifs" class="text-ink underline underline-offset-4 font-semibold">Offres et tarifs →</a></p>')
 + FINAL("45 minutes au téléphone pour voir ce que vous pourriez arrêter de taper le soir.")))

# ---------- Offres & tarifs
card = lambda inner: f'<div class="p-8 rounded-[1em] bg-soft space-y-4">{inner}</div>'
pages.append(page("/offres-tarifs", "Tarifs CLICKDROIT : projets à prix fixe dès 5 000 € HT",
 "Audit gratuit, Déploiement Express à 5 000 € HT, Progressif à 1 400 € HT/mois, maintenance dès 150 € HT/mois. Tous les prix affichés.",
 H1("Des prix fixes, un périmètre écrit.","Tous les prix sont hors taxes (HT). Pas de régie au jour : vous savez ce que vous payez et ce que vous recevez avant de signer.")
 + S("1. Audit Flash Automatisation — Gratuit", P("Phase de lancement, 10 audits par semaine au maximum.") + UL(["45 minutes en visio ou au téléphone.","Rapport de 3 à 5 pages sous 72 heures ouvrées : 3 à 5 automatisations, gain estimé et calcul, priorisation, proposition de prix."]) + f'<div>{cta()}</div>')
 + S("2. Projet de déploiement", '<div class="grid md:grid-cols-2 gap-6">' + card('<h3 class="text-xl font-semibold text-ink">Déploiement Express — 5 000 EUR HT</h3>' + UL(["3 automatisations, ou 2 automatisations + 1 agent IA, choisies dans l'audit.","4 à 6 semaines.","Inclus : cadrage, conception, développement, tests, mise en production, documentation, 2 sessions de formation, 30 jours de garantie après mise en production.","Paiement : 50 % à la signature, 50 % à la mise en production."])) + card('<h3 class="text-xl font-semibold text-ink">Déploiement Progressif — 1 400 EUR HT par mois pendant 4 mois (5 600 EUR HT)</h3>' + UL(["Mois 1 : cadrage et première automatisation en production.","Mois 2 et 3 : une nouvelle automatisation par mois.","Mois 4 : agent IA ou automatisation avancée, bilan.","Point mensuel avec le dirigeant, formation au fil de l'eau, documentation."])) + '</div>')
 + S("3. Après la mise en production", TABLE(["Offre","Prix HT","Contenu","Engagement"],[["Maintenance","150 EUR / mois","Supervision, corrections, mises à jour des connecteurs, sauvegardes, support mail sous 2 jours ouvrés","3 mois minimum"],["Accompagnement Essentiel","500 EUR / mois","Maintenance + 1 automatisation simple par trimestre + point trimestriel","12 mois"],["Accompagnement Pilotage","900 EUR / mois","Maintenance + 1 automatisation avancée par trimestre (agent IA, multi-outils, voix) + point mensuel + support sous 1 jour ouvré","12 mois"]]) + P("Accompagnements résiliables après 12 mois avec 1 mois de préavis."))
 + S("4. Options", TABLE(["Option","Prix HT"],[["Automatisation supplémentaire (flux simple)","1 500 EUR"],["Agent IA supplémentaire (base documentaire fournie par vous)","2 500 EUR"],["Module vocal BTP supplémentaire (hors minutes téléphoniques)","2 000 EUR"],["Charte d'usage de l'IA + atelier de 2 h (cabinets)","900 EUR"],["Formation supplémentaire (2 h, à distance)","300 EUR"]]).replace('<tr class="border-t border-line"><td class="p-4 align-top">Formation', TODO("confirmation licence n8n avant d'afficher la ligne « Hébergement géré par CLICKDROIT (prix de lancement) — 50 EUR / mois »") + '<tr class="border-t border-line"><td class="p-4 align-top">Formation',1))
 + S("Coûts tiers", P("Les coûts d'usage des API d'IA et de voix sont payés directement sur vos comptes (recommandé) ou refacturés au réel, sans marge."))
 + S("Pour comparer", UL(["Projets complets d'agences d'automatisation : 3 000 à 10 000 EUR HT (prix publics de plusieurs agences, consultés le 13 octobre 2026).","TJM moyen d'un freelance n8n : environ 450 EUR (Malt Tech Trends 2026, relayé par Programmez)."]) + P("Les propositions sont valables 30 jours. Nous ajustons le périmètre, pas le prix."))))

# ---------- Audit gratuit
pages.append(page("/audit-gratuit", "Audit gratuit : 3 à 5 automatisations chiffrées",
 "45 minutes en visio ou au téléphone, puis un rapport de 3 à 5 pages sous 72 h ouvrées, avec le gain estimé et son calcul. Réservez un créneau.",
 H1("45 minutes pour chiffrer 3 à 5 automatisations.","Gratuit pendant la phase de lancement, 10 audits par semaine au maximum. Vous repartez avec un rapport écrit, que vous travailliez avec nous ou non.")
 + f'<div class="mb-10"><a href="{CAL}" target="_blank" rel="noopener" class="{BTN}">Choisir un créneau{ARROW}</a></div>'
 + S("Pour qui", UL(["Cabinets d'expertise comptable et entreprises du BTP.","Chiffre d'affaires annuel à partir de 200 000 EUR.","Le dirigeant ou un associé participe à l'appel.","Au moins une tâche répétitive identifiée (relances, saisie, tri, comptes rendus)."]))
 + S("Avant l'appel", P("Un questionnaire de 5 minutes : secteur, chiffre d'affaires, effectif, logiciels utilisés, vos 3 tâches les plus chronophages, usage actuel de l'IA.") + TODO("lien du formulaire (questionnaire préalable)"))
 + S("Pendant l'appel (45 min, visio ou téléphone)", UL(["5 min : ce que contiendra le rapport.","15 min : vos outils et vos tâches répétitives.","15 min : les volumes et le temps passé, tâche par tâche. Ce sont vos chiffres qui servent au calcul.","5 min : données sensibles, hébergement, API disponibles, calendrier.","5 min : une courte démonstration (un flux cabinet, ou un devis dicté pour le BTP) et la suite."]))
 + S("Sous 72 heures ouvrées : votre rapport (3 à 5 pages)", UL(["Une cartographie simple de vos outils et flux.","3 à 5 automatisations, chacune avec sa faisabilité, sa complexité, ses points de vigilance et son calcul de gain (volume × temps unitaire), marqué « estimation à valider ».","Un ordre de déploiement recommandé.","Une recommandation d'hébergement.","Une proposition à prix fixe, valable 30 jours."]))
 + S("Ce que l'audit n'est pas", P("Pas de développement, pas d'accès à vos données réelles, pas d'engagement de résultat. Les gains sont des estimations fondées sur ce que vous nous dites."))
 + f'<div class="my-12"><a href="{CAL}" target="_blank" rel="noopener" class="{BTN}">Choisir un créneau{ARROW}</a></div>'))

# ---------- À propos
pages.append(page("/a-propos", "À propos de CLICKDROIT, intégrateur IA et automatisation",
 "Un intégrateur spécialisé sur deux secteurs : cabinets comptables et BTP. Prix fixes, données sous contrôle, aucun témoignage inventé.",
 H1("Un intégrateur, deux secteurs.","CLICKDROIT conçoit, déploie et maintient des automatisations et des assistants IA pour les cabinets d'expertise comptable et les entreprises du BTP.") + TODO("nom, parcours et photo du fondateur — 3 à 4 phrases factuelles, sans titre inventé")
 + S("Ce que nous sommes, et ce que nous ne sommes pas", TABLE(["Nous sommes","Nous ne sommes pas"],[["Un intégrateur qui relie vos logiciels existants","Un éditeur qui veut remplacer vos outils métier"],["Spécialisés sur deux secteurs","Une agence qui automatise tout pour tout le monde"],["À prix fixe, avec un gain estimé avant signature","Une régie facturée au jour"],["Attentifs au cadre d'usage de l'IA","Des vendeurs de « ChatGPT pour tous »"]]))
 + S("Comment nous travaillons", P("Découvrir, chiffrer, cadrer, construire, déployer, améliorer. Un flux en production avant d'en commencer un autre. Une démonstration de 30 minutes chaque semaine pendant le projet. Une documentation d'une page par flux. Le temps gagné est mesuré au bilan à 30 jours et comparé à l'estimation de l'audit."))
 + S("Nos outils", P("n8n comme outil principal, Make s'il est déjà en place chez vous, des modèles d'IA choisis selon la sensibilité de vos données, et des projets open source éprouvés quand ils évitent de tout redévelopper."))
 + S("Où nous en sommes", P("CLICKDROIT démarre. Nous n'avons pas encore de clients à citer. Les premières études de cas seront publiées uniquement avec l'accord écrit des clients concernés.") + f'<div>{cta()}</div>')))

# ---------- Contact
inp = 'mt-1 w-full bg-soft border border-line rounded-[1em] px-4 py-3'
pages.append(page("/contact", "Contacter CLICKDROIT",
 "Une question sur l'automatisation de votre cabinet ou de votre entreprise du BTP ? Écrivez-nous ou réservez directement un audit gratuit.",
 H1("Nous écrire ou nous appeler.") + P('Le plus simple pour commencer est l\'audit gratuit de 45 minutes.') + f'<div class="mt-4 mb-10">{cta()}</div>'
 + TODO("adresse de contact (e-mail)") + TODO("numéro de téléphone") + TODO("interlocuteur : nom et rôle") + TODO("horaires de réponse")
 + S("Formulaire", TODO("destination technique du formulaire — formulaire désactivé tant qu'elle n'est pas définie") + TODO("délai de réponse pour le message de confirmation « Merci. Nous vous répondons sous … »")
   + f'<form class="grid gap-4 max-w-xl" onsubmit="return false"><label>Nom<input class="{inp}" name="nom" required></label><label>Société<input class="{inp}" name="societe"></label><label>Secteur<select class="{inp}" name="secteur"><option>Cabinet d\'expertise comptable</option><option>BTP</option><option>Autre</option></select></label><label>E-mail<input type="email" class="{inp}" name="email" required></label><label>Téléphone (facultatif)<input type="tel" class="{inp}" name="tel"></label><label>Votre message<textarea class="{inp}" rows="5" name="message" required></textarea></label><label class="flex gap-2 items-start text-sm"><input type="checkbox" required class="mt-1"> <span>J\'accepte que CLICKDROIT utilise ces informations pour me répondre. <a href="/mentions-legales#donnees" class="text-ink underline underline-offset-4 underline">Données personnelles</a></span></label><button type="submit" disabled class="bg-ink text-white px-6 py-3 rounded-full font-medium opacity-60 cursor-not-allowed">Envoyer</button></form>')))

# ---------- Mentions légales
pages.append(page("/mentions-legales", "Mentions légales et données personnelles | CLICKDROIT",
 "Éditeur, hébergeur, traitement des données personnelles et cookies du site clickdroit.fr.",
 TODO("page entière à compléter et faire valider (juriste ou modèle officiel) avant mise en ligne") +
 H1("Mentions légales et données personnelles")
 + S("Éditeur du site", TODO("raison sociale ou nom de l'entrepreneur") + TODO("forme juridique") + TODO("capital social, si société") + TODO("siège : adresse") + TODO("SIREN / RCS") + TODO("n° TVA intracommunautaire, si applicable") + TODO("directeur de la publication") + TODO("contact : e-mail, téléphone") + P("Informations en cours de complétion."))
 + S("Hébergeur", TODO("nom, adresse et téléphone de l'hébergeur du site (DNS observé : Infomaniak, à confirmer)") + P("Informations en cours de complétion."))
 + S("Propriété intellectuelle", TODO("éditeur (titulaire des droits)") + P("Les contenus de ce site sont la propriété de leur éditeur, sauf mention contraire."))
 + '<div id="donnees"></div>' + S("Données personnelles", UL(["Données collectées : formulaire de contact, questionnaire et prise de rendez-vous d'audit (nom, société, coordonnées, informations sur l'activité).","Finalités : répondre à vos demandes, organiser et réaliser l'audit.","Vos droits : accès, rectification, effacement, opposition, limitation, portabilité. Vous pouvez saisir la CNIL (cnil.fr)."]) + TODO("responsable du traitement") + TODO("base légale à valider — mesures précontractuelles / intérêt légitime") + TODO("destinataires et sous-traitants : outil d'agenda, hébergeur, outil de formulaire") + TODO("durée de conservation") + TODO("contact pour l'exercice des droits") + TODO("transferts hors UE selon les outils retenus"))
 + S("Cookies", TODO("liste des cookies et traceurs, outil de mesure d'audience, bandeau de consentement si nécessaire") + P("Informations en cours de complétion."))
 + S("Clients", P("Pour les projets, CLICKDROIT agit comme sous-traitant (article 28 du RGPD) ; un accord de traitement des données est annexé à chaque contrat."))))

# robots + sitemap
open(os.path.join(ROOT,'robots.txt'),'w').write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
sm = ''.join(f'  <url><loc>{SITE}{p if p=="/" else p}</loc><lastmod>2026-10-13</lastmod></url>\n' for p in pages if p!="/mentions-legales")
open(os.path.join(ROOT,'sitemap.xml'),'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}</urlset>\n')
print("ok", pages)
