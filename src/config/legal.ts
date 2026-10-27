import { site } from "./site";

/**
 * Informations légales. Un champ `null` est une information encore à fournir :
 * elle ne doit pas être inventée. L'étape « juridique » décide de l'affichage
 * (plus aucun « À fournir » en public) et du contrôle au build.
 */
export const legal = {
  /** Date affichée, au format « 27 octobre 2026 ». */
  updated: null as string | null,
  editorName: null as string | null,
  legalForm: null as string | null,
  address: "30 N Gould St, Ste N, Sheridan, WY 82801, États-Unis",
  siret: null as string | null,
  registration: null as string | null,
  vat: null as string | null,
  /** Téléphone de l'éditeur. Distinct de site.phone : les deux peuvent être remplis ensemble. */
  phone: null as string | null,
  publicationDirector: null as string | null,
  privacyEmail: null as string | null,
  /**
   * Hébergeur du site. Coordonnées relevées le 27 octobre 2026 sur
   * https://www.infomaniak.com/fr/cgv/mentions-legales (nom, adresse,
   * registre du commerce, IDE). Le formulaire de contact public
   * https://contact.infomaniak.com redirige vers https://www.infomaniak.com/fr/aide.
   * Leur page de mentions ne publie pas de numéro de téléphone.
   */
  host: {
    name: "Infomaniak Network SA",
    address:
      "Rue Eugène Marziano 25, 1227 Les Acacias (GE), Suisse. Registre du commerce de Genève : CH-660.0.059.996-1. IDE : CHE-103.167.648.",
    contact: "https://www.infomaniak.com/fr/aide",
  },
  processors: null as string | null,
  prospectRetention: null as string | null,
  /** Note interne : cookies du module de réservation. Non affichée telle quelle. */
  calendarCookiesNote: null as string | null,
  cgvReviewedByLawyer: false,
  paymentSchedule: null as string | null,
  paymentDelay: null as string | null,
  lateInterest: null as string | null,
  guaranteeWording: null as string | null,
  liabilityCap: null as string | null,
  court: null as string | null,
  complianceReviewedByLawyer: false,
  automationHost: null as string | null,
  serviceTable: null as string | null,
  securityMeasures: null as string | null,
};

export type Legal = typeof legal;

export interface LegalGap {
  field: string;
  label: string;
}

/** Champs sans lesquels les pages légales ne sont pas publiables. */
export function legalGaps(): LegalGap[] {
  const gaps: LegalGap[] = [];
  const need = (field: string, label: string, value: string | null | undefined) => {
    if (!value || !value.trim()) gaps.push({ field, label });
  };
  need("legal.updated", "date de mise à jour", legal.updated);
  need("legal.editorName", "dénomination ou nom", legal.editorName);
  need("legal.legalForm", "forme juridique", legal.legalForm);
  need("legal.address", "adresse de l'éditeur", legal.address);
  need("legal.siret", "numéro SIRET", legal.siret);
  need("legal.registration", "immatriculation", legal.registration);
  need("legal.vat", "numéro de TVA ou mention de franchise", legal.vat);
  need("legal.phone", "téléphone de l'éditeur", legal.phone);
  need("legal.publicationDirector", "directeur de la publication", legal.publicationDirector);
  need("legal.privacyEmail", "adresse e-mail pour les demandes RGPD", legal.privacyEmail);
  need("legal.host.name", "nom de l'hébergeur", legal.host.name);
  need("legal.host.address", "adresse de l'hébergeur", legal.host.address);
  need("legal.host.contact", "contact de l'hébergeur", legal.host.contact);
  need("legal.processors", "liste des sous-traitants", legal.processors);
  need("legal.prospectRetention", "durée de conservation des données de prospects", legal.prospectRetention);
  need("legal.paymentSchedule", "échéancier de paiement de l'installation", legal.paymentSchedule);
  need("legal.paymentDelay", "délai de paiement", legal.paymentDelay);
  need("legal.lateInterest", "taux des pénalités de retard", legal.lateInterest);
  need("legal.guaranteeWording", "formulation de la garantie", legal.guaranteeWording);
  need("legal.liabilityCap", "plafond de responsabilité", legal.liabilityCap);
  need("legal.court", "tribunal compétent", legal.court);
  need("legal.automationHost", "hébergeur des automatisations et pays", legal.automationHost);
  need("legal.serviceTable", "tableau des services", legal.serviceTable);
  need("legal.securityMeasures", "mesures de sécurité", legal.securityMeasures);
  if (!legal.cgvReviewedByLawyer) {
    gaps.push({ field: "legal.cgvReviewedByLawyer", label: "relecture des CGV par un juriste" });
  }
  if (!legal.complianceReviewedByLawyer) {
    gaps.push({
      field: "legal.complianceReviewedByLawyer",
      label: "relecture de la page IA et conformité par un juriste",
    });
  }
  return gaps;
}

export function legalIsComplete(): boolean {
  return legalGaps().length === 0;
}

/** E-mail public déjà connu, repris du site. */
export const publisherEmail = site.email;
