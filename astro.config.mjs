import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";

// Étape 1 : même sortie que le live (fichiers .html). Les URL propres arrivent ensuite.
export default defineConfig({
  site: "https://clickdroit.fr",
  trailingSlash: "ignore",
  integrations: [
    sitemap({
      filter: (page) => !page.includes("/automatisation-ia"),
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
  build: {
    format: "file",
    inlineStylesheets: "always",
  },
});
