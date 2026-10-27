/**
 * Configuration du site, retrouvée dans le bundle KitForm du live (27/10/2026).
 * Les textes affichés lisent ce fichier. Un champ vide masque le bloc correspondant
 * dès que la correction « honnêteté » est en place (voir les commentaires).
 */
export interface Availability {
  places: number;
  month: string;
}

export const site = {
  name: "ClickDroit",
  url: "https://clickdroit.fr",
  locale: "fr_FR",
  city: "Rouen",
  region: "Normandie",
  email: "mavrick@clickdroit.fr",
  /** Numéro public. Tant qu'il est vide, on ne promet pas un appel téléphonique. */
  phone: null as string | null,
  /**
   * Pastille « N nouveaux projets en {mois} ».
   * null = la pastille et la ligne du menu mobile sont masquées.
   */
  availability: null as Availability | null,
  founder: {
    name: "Mavrick",
    /** Nom complet. Masqué tant qu'il est vide : on affiche `name`. */
    fullName: null as string | null,
    yearsAsDev: 7,
    /** Chemin public de la photo (ex. "/fondateur.jpg"). Masquée tant qu'elle est vide. */
    photo: null as string | null,
    photoAlt: "Portrait de Mavrick, fondateur de ClickDroit",
    anecdote: null as string | null,
    mavrickMediaYear: "2019",
    clickdroitYear: "2026",
    travel: "Et je me déplace partout en France quand votre projet le demande.",
    linkedin: "https://www.linkedin.com/in/mavricklintanf/",
  },
  /**
   * Réservation. null = le bloc « La réservation en ligne ouvre très bientôt ».
   * Une URL Cal.com intègre l'agenda. Toute autre URL (agenda Google) affiche
   * le bouton `bookingLabel`, sans charger le script Cal.com.
   */
  calLink: "https://calendar.app.google/JHuG9bUeeuBmpLwKA",
  bookingLabel: "Réserver mon audit",
  kitsReady: false,
  kitWebhook: null as string | null,
  /** Domaine Plausible, sans cookie. null = pas de script d'audience. */
  plausible: null as string | null,
  social: {
    youtube: "https://www.youtube.com/@mavricklintanf",
    linkedin: "https://www.linkedin.com/in/mavricklintanf/",
    instagram: "https://www.instagram.com/mavricklintanf/",
    tiktok: "https://www.tiktok.com/@mavricklintanf",
    skool: null as string | null,
  },
  audience: null as string | null,
  prices: {
    validated: true,
    premierRobot: { setup: 1490, monthly: 149 },
    pilote: { setup: 3900, monthly: 390 },
    surMesure: { setup: 8000 },
  },
  integrations: [
    { group: "Messageries", tools: ["WhatsApp", "Gmail", "Outlook"] },
    { group: "Agendas", tools: ["Google Agenda", "Outlook"] },
    { group: "Logiciels BTP", tools: [] as string[] },
    { group: "Logiciels cabinet", tools: [] as string[] },
    { group: "Compta", tools: [] as string[] },
  ],
  engagement: "un mois minimum, puis résiliable à tout moment, sans préavis",
  offers: {
    premierRobotImprovement: true,
    support: "sur Discord, Slack ou WhatsApp, selon ce que vous utilisez déjà",
    aiUsageExcluded: null as string | null,
    payment: null as string | null,
    exit: "Vous récupérez toutes vos automatisations : elles vous appartiennent.",
  },
};

export type Site = typeof site;

export function founderDisplayName(): string {
  return site.founder.fullName?.trim() || site.founder.name;
}
