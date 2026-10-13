## Refonte de clickdroit.fr : offre IA + automatisation (cabinets comptables et BTP) — design inspiré de leftclick.ai

Remplace entièrement l'ancien site (rédaction de contenu SEO) par 8 pages statiques, reprises mot pour mot de la copie marketing (`/workspace/marketing/site-clickdroit/`).

### Contenu
- Pages : `/`, `/experts-comptables`, `/btp-assistant-vocal`, `/offres-tarifs`, `/audit-gratuit`, `/a-propos`, `/contact`, `/mentions-legales` (ancre `#donnees`).
- HTML statique + Tailwind CDN, police DM Sans. Pages générées par `tools/build.py` (chaque page = `dossier/index.html`, URL propres sans réécriture).
- CTA « Réserver mon audit gratuit » partout vers `/audit-gratuit` ; bouton « Choisir un créneau » vers https://calendar.app.google/JHuG9bUeeuBmpLwKA.
- Section données/RGPD/hébergement (accueil, experts-comptables, mentions légales).
- SEO : title et meta description du brief, canonical, Open Graph, JSON-LD `Organization`, `robots.txt`, `sitemap.xml` (mentions légales exclue).
- `.htaccess` **proposé** : HTTPS forcé, `Redirect 301 /index.html /`. L'ancien site ne comporte qu'une page (liens = ancres `#`), aucune autre ancienne URL trouvée ; à compléter si vous en connaissez (Search Console, liens externes).

### Direction visuelle (inspirée de leftclick.ai)
Repris : le **langage visuel uniquement** — palette monochrome (#111113 / #0a0a0c / #f0f0f2 / #f7f7f8), police DM Sans avec interlettrage serré, grands titres, hero centré, boutons pilules noirs avec pastille flèche, cartes grises arrondies (1em), section sombre arrondie (2em) pour « Vos données restent sous contrôle », bandeau défilant (outils cités dans notre copie, pas de logos), étapes numérotées en 4 cartes, bandeau CTA final sombre, pied de page sombre en colonnes, apparition douce des sections au défilement (désactivée si `prefers-reduced-motion`).
Non repris : aucun texte, logo, image, logo client, chiffre ni témoignage de leftclick.ai. Aucun chiffre ajouté (pas de bandeau de statistiques).

### Supprimé
Offre de rédaction SEO, tarification au mot, les 3 témoignages, mentions « top 1 % ». Aucun chiffre ajouté hors ceux sourcés dans la copie ; les gains sont marqués « estimation à valider ».

### Éléments [need] masqués (commentaires HTML `TODO`, non visibles) — à fournir avant mise en ligne
1. Lien du questionnaire préalable (`/audit-gratuit`)
2. Ligne « Hébergement géré par CLICKDROIT — 50 EUR/mois » : masquée tant que la licence n8n n'est pas confirmée (`/offres-tarifs`)
3. Nom, parcours et photo du fondateur (`/a-propos`)
4. Contact : e-mail, téléphone, interlocuteur (nom et rôle), horaires de réponse (`/contact`)
5. Destination technique du formulaire de contact (bouton « Envoyer » désactivé en attendant) et délai de réponse du message de confirmation
6. Mentions légales : raison sociale, forme juridique, capital, siège, SIREN/RCS, TVA, directeur de la publication, contact
7. Hébergeur (DNS observé : Infomaniak, à confirmer)
8. RGPD : responsable du traitement, base légale, sous-traitants (agenda, formulaire, hébergeur), durée de conservation, contact droits, transferts hors UE
9. Cookies / mesure d'audience / bandeau de consentement
10. Validation juridique de la page mentions légales

Le lien d'agenda du brief est résolu (lien fourni par Mavrick).

### Captures avant / après
Avant = production actuelle. Après = rendu local (`python3 -m http.server`). Référence : `docs/screenshots/ref-leftclick-*.png` (étude de design, non publiée sur le site).

| | 1280 px | 390 px |
|---|---|---|
| Avant (accueil, production) | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/before-home-1280.png?raw=true) | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/before-home-390.png?raw=true) |
| Après : home | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-home-1280.png?raw=true) | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-home-390.png?raw=true) |
| Après : experts-comptables | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-experts-comptables-1280.png?raw=true) | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-experts-comptables-390.png?raw=true) |
| Après : btp-assistant-vocal | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-btp-assistant-vocal-1280.png?raw=true) | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-btp-assistant-vocal-390.png?raw=true) |
| Après : offres-tarifs | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-offres-tarifs-1280.png?raw=true) | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-offres-tarifs-390.png?raw=true) |
| Après : audit-gratuit | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-audit-gratuit-1280.png?raw=true) | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-audit-gratuit-390.png?raw=true) |
| Après : a-propos | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-a-propos-1280.png?raw=true) | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-a-propos-390.png?raw=true) |
| Après : contact | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-contact-1280.png?raw=true) | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-contact-390.png?raw=true) |
| Après : mentions-legales | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-mentions-legales-1280.png?raw=true) | ![](https://github.com/MavrickL/clickdroit-site/blob/feat/refonte-leftclick/docs/screenshots/after-leftclick-mentions-legales-390.png?raw=true) |

### Déploiement
**Aucune mise en ligne par cette PR.** Le déploiement sur l'hébergement Infomaniak est manuel (dépôt des fichiers par FTP/gestionnaire) et relève uniquement de la décision de Mavrick, après remplissage des éléments [need]. Ne pas fusionner sans son accord.
