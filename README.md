# ClickDroit

Site statique de [clickdroit.fr](https://clickdroit.fr), reconstruit en Astro à partir du site en ligne (copie du 27 octobre 2026).

Astro, Tailwind CSS 4, polices Fontsource (Bricolage Grotesque, Atkinson Hyperlegible Next, Atkinson Hyperlegible Mono). Les textes et les prix viennent de `src/config/site.ts` et `src/config/legal.ts`.

```bash
npm install
npm run dev
npm run build
npm run preview
```

Le build produit `dist/`. La mise en ligne se fait à la main sur Infomaniak (pas de déploiement automatique). Avant d'envoyer les fichiers, lancer `npm run build:strict` : il échoue tant qu'une information légale obligatoire est vide.
