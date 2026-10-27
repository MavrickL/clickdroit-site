# Mise en ligne ClickDroit sur Infomaniak

Hébergement web Apache. Dépôt manuel par le gestionnaire de fichiers ou par FTP. Rien n'est déployé depuis git, et le DNS ne change pas.

L'archive `clickdroit-dist.zip` contient le résultat de `npm ci` puis `npm run build` (27 octobre 2026). `npm run build:strict` échoue tant que `src/config/legal.ts` est incomplet : c'est voulu. Les pages mentions légales, confidentialité, CGV et IA et conformité restent en `noindex` et hors du sitemap.

## 1. Sauvegarder le site actuel

Avant d'envoyer le moindre fichier :

1. Dans le Manager Infomaniak, ouvrir l'hébergement web de clickdroit.fr et noter le dossier racine du site (voir ci-dessous).
2. Télécharger **tout** ce dossier (gestionnaire de fichiers ou FTP), y compris les fichiers cachés s'il y en a.
3. Conserver cette copie sous un nom daté, par exemple `clickdroit-backup-2026-10-27.zip`, jusqu'à la fin de la vérification.

Cette copie est le seul retour arrière fiable.

## 2. Où déposer les fichiers

Déposer le contenu de l'archive dans le **dossier racine du site**, celui que le Manager indique pour clickdroit.fr.

L'exemple habituel est `/sites/clickdroit.fr` (chemin FTP souvent préfixé par le dossier du compte, du type `/home/clients/…/sites/clickdroit.fr`). Le chemin exact est affiché dans le Manager, fiche du site, champ « dossier » / « répertoire racine ». C'est ce chemin-là qu'il faut utiliser, pas un sous-dossier `www`, `public` ou `dist` inventé.

À la racine du site, après dépose, on doit voir directement `index.html`, `.htaccess`, `404.html`, `avocats/`, `_astro/`, etc.

Ne pas envoyer `src/`, `node_modules/`, ni `brand/`.

## 3. Décompresser

L'archive n'a pas de dossier englobant : `.htaccess`, `index.html` et les dossiers de pages sont à la racine du zip. Les fichiers cachés sont inclus.

1. Envoyer `clickdroit-dist.zip` dans le dossier racine du site.
2. Décompresser **dans ce dossier**.
3. Si l'outil crée malgré tout un sous-dossier `clickdroit-dist/`, déplacer son contenu d'un niveau vers le dossier racine, puis supprimer le sous-dossier vide.
4. Vérifier que `.htaccess` est bien là. Le gestionnaire de fichiers et certains clients FTP masquent les noms qui commencent par un point : activer l'affichage des fichiers cachés. Sans ce fichier, les URL propres, la 404 et le cache ne s'appliquent pas.
5. `index.html` du site actuel est **remplacé** par celui de l'archive. C'est la page d'accueil.

Les nouveaux dossiers (`avocats/`, `btp/`, `audit/`, etc.) s'ajoutent à côté des anciens fichiers `.html`. C'est le comportement attendu.

## 4. Anciens fichiers `.html`

Copie du site en ligne du 27 octobre 2026. Ces fichiers ne sont plus l'adresse publique de la page : Astro publie un dossier du même nom avec `index.html` dedans.

| Fichier actuel | Devient |
| --- | --- |
| `a-propos.html` | `a-propos/index.html` |
| `audit.html` | `audit/index.html` |
| `automatisation-ia.html` | `automatisation-ia/index.html` |
| `avocats.html` | `avocats/index.html` |
| `btp.html` | `btp/index.html` |
| `cgv.html` | `cgv/index.html` |
| `confidentialite.html` | `confidentialite/index.html` |
| `ia-et-conformite.html` | `ia-et-conformite/index.html` |
| `mentions-legales.html` | `mentions-legales/index.html` |
| `methode.html` | `methode/index.html` |
| `offres.html` | `offres/index.html` |
| `ressources.html` | `ressources/index.html` |

Ne pas les supprimer pendant la mise en ligne. Les laisser ne gêne pas `.htaccess` **tant que le dossier de la page est bien présent** :

- `/avocats.html` répond 301 vers `https://clickdroit.fr/avocats` (la règle regarde la requête du navigateur, pas le fichier réécrit en interne).
- `/avocats` sert `avocats/index.html`. Testé avec MultiViews activé : le dossier gagne sur `avocats.html`. Le fichier ancien n'est pas envoyé.

`index.html` n'est pas dans cette liste : il reste le fichier de l'accueil et doit être celui de l'archive. L'adresse `/index.html` redirige vers `https://clickdroit.fr/`.

Deux points d'attention :

- Si un dossier de page manquait et que l'ancien `.html` était encore là, un Apache avec MultiViews servirait l'ancienne page à l'URL propre (`/avocats` → contenu de `avocats.html`). D'où la sauvegarde, puis la checklist : chaque URL propre doit afficher le nouveau site. `Options -MultiViews` n'est pas dans `.htaccess` : sans autorisation explicite de cette option, Apache renvoie « Option MultiViews not allowed here » et tout le site passe en 500.
- Les anciens fichiers dans `_astro/` (noms hashés différents) peuvent rester. Ils ne sont plus liés. Ne pas effacer le dossier `_astro/` après le dépôt : il contient les fichiers du nouveau site. `favicon.svg`, `robots.txt`, `sitemap-index.xml` et `sitemap-0.xml` sont remplacés par l'archive.

Une fois la checklist verte, les douze `.html` du tableau peuvent être retirés à la main. Ce n'est pas nécessaire au fonctionnement.

## 5. Checklist après mise en ligne

Navigateur en navigation privée, ou cache vidé.

**Pages (200, contenu du nouveau site, URL sans `.html` ni slash final)**

- https://clickdroit.fr/
- https://clickdroit.fr/avocats
- https://clickdroit.fr/btp
- https://clickdroit.fr/audit
- https://clickdroit.fr/a-propos
- https://clickdroit.fr/offres
- https://clickdroit.fr/methode

**Redirections (301)**

- https://clickdroit.fr/avocats.html → https://clickdroit.fr/avocats
- https://clickdroit.fr/index.html → https://clickdroit.fr/
- https://clickdroit.fr/avocats/ → https://clickdroit.fr/avocats
- http://clickdroit.fr/… → https://clickdroit.fr/… (à contrôler en production : le proxy Infomaniak est le seul endroit où `%{HTTPS}` et `X-Forwarded-Proto` sont réellement combinés)
- http://www.clickdroit.fr/ et https://www.clickdroit.fr/ → https://clickdroit.fr/ (même réserve)

Une boucle (ERR_TOO_MANY_REDIRECTS) sur l'accueil en https veut dire que le proxy et la règle HTTPS ne sont pas d'accord. La règle exige les deux conditions ensemble : `%{HTTPS}` différent de on, **et** `X-Forwarded-Proto` différent de `https`. Ne pas la remplacer par une seule des deux.

**404**

- https://clickdroit.fr/page-qui-nexiste-pas → statut 404, titre « Page introuvable | ClickDroit ».

**Réservation**

- Le bouton « Réserver mon audit » ouvre https://calendar.app.google/JHuG9bUeeuBmpLwKA dans un nouvel onglet.

**Favicon**

- L'onglet affiche le symbole bleu ClickDroit. Si l'ancien reste, recharger en forçant le cache.

**Partage LinkedIn**

- Ouvrir l'inspecteur de publication : https://www.linkedin.com/post-inspector/
- Coller `https://clickdroit.fr/`
- L'image attendue est `https://clickdroit.fr/og.png` (1200×630, logo bleu). Le titre et la description sont ceux de l'accueil. Si LinkedIn montre l'ancienne image, lancer une nouvelle inspection : il garde le résultat précédent.

**Légal**

- https://clickdroit.fr/mentions-legales, `/confidentialite`, `/cgv` et `/ia-et-conformite` s'affichent, avec `noindex`. Elles sont absentes du sitemap. Elles le restent tant que `legal.ts` n'est pas complet.

## 6. Retour arrière

1. Remettre dans le dossier racine **tous** les fichiers de la sauvegarde, en écrasant ceux du nouveau site (`index.html`, `favicon.svg`, `robots.txt`, les sitemap, `_astro/`).
2. Supprimer `.htaccess` déposé par l'archive si la sauvegarde n'en avait pas. Tant qu'il est en place, `/avocats.html` redirige vers `/avocats` et `/avocats` cherche le dossier.
3. Supprimer les dossiers de pages ajoutés par l'archive : `a-propos/`, `audit/`, `automatisation-ia/`, `avocats/`, `btp/`, `cgv/`, `confidentialite/`, `ia-et-conformite/`, `mentions-legales/`, `methode/`, `offres/`, `ressources/`.
4. Supprimer les fichiers nouveaux absents de la sauvegarde, en particulier `404.html`, `favicon.ico`, `favicon-32.png`, `apple-touch-icon-180.png`, `icon-192.png`, `icon-512.png`, `site.webmanifest`, `logo.png`, `logo-horizontal.svg`, `logo-horizontal-inverse.svg`, `og.png`.
5. Vérifier que l'accueil et une page métier (`avocats.html` ou l'URL qui marchait avant) réaffichent le site sauvegardé.

Décompresser la sauvegarde par-dessus le nouveau site, sans les étapes 2 à 4, laisse `.htaccess` et les dossiers en place : les URL continuent de suivre les nouvelles règles.
