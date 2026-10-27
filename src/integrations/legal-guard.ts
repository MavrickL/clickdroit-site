import type { AstroIntegration } from "astro";
import { legalGaps } from "../config/legal";

function report(): string {
  const gaps = legalGaps();
  if (gaps.length === 0) return "";
  const lines = gaps.map((gap) => `  - ${gap.field} — ${gap.label}`).join("\n");
  return [
    `ClickDroit : ${gaps.length} champ(s) légal(aux) obligatoire(s) encore vide(s).`,
    "Les pages mentions légales, confidentialité, CGV et IA et conformité restent en noindex et hors du sitemap.",
    lines,
    "Renseignez src/config/legal.ts. La commande npm run build:strict échoue tant qu'un champ obligatoire est vide.",
  ].join("\n");
}

function guard() {
  const message = report();
  if (!message) {
    console.log("Pages légales : tous les champs obligatoires sont remplis.");
    return;
  }
  if (process.env.CLICKDROIT_STRICT_LEGAL === "1") {
    throw new Error(message);
  }
  console.warn(`\n${message}\n`);
}

/** Avertit au build (et fait échouer `build:strict`) tant que legal.ts est incomplet. */
export function legalGuard(): AstroIntegration {
  return {
    name: "clickdroit-legal-guard",
    hooks: {
      "astro:build:start": guard,
      "astro:server:start": guard,
    },
  };
}
