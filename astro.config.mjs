import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";
import { legalIsComplete } from "./src/config/legal.ts";
import { legalGuard } from "./src/integrations/legal-guard.ts";

/** Pages volontairement hors de l'index, donc hors du sitemap. */
const alwaysHidden = ["/automatisation-ia", "/ressources", "/404"];
const hiddenUntilLegal = ["/mentions-legales", "/confidentialite", "/cgv", "/ia-et-conformite"];

function isHidden(page) {
  const path = new URL(page).pathname.replace(/\/$/, "") || "/";
  if (alwaysHidden.includes(path)) return true;
  if (!legalIsComplete() && hiddenUntilLegal.includes(path)) return true;
  return false;
}

export default defineConfig({
  site: "https://clickdroit.fr",
  trailingSlash: "never",
  integrations: [
    legalGuard(),
    sitemap({
      filter: (page) => !isHidden(page),
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
  build: {
    format: "directory",
    inlineStylesheets: "always",
  },
});
