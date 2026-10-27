/// <reference types="astro/client" />

interface ClickDroitApi {
  contextMenu: (el: Element, opts?: { onSelect?: (item: Element) => void }) => void;
  tabs: (root: Element, onSelect?: (id: string) => void) => { select: (el: Element, focus?: boolean) => void };
  mockup: (host: Element, spec: unknown, opts?: { still?: boolean; gap?: number; hold?: number }) => { stop: () => void; restart: () => void };
  heroScene: (host: Element, spec: unknown) => { stop: () => void };
  calculator: (form: Element, onUse?: () => void) => void;
  icons: Record<string, string>;
}

declare global {
  interface Window {
    ClickDroit: ClickDroitApi;
    plausible?: (event: string, options?: { props?: Record<string, string | undefined> }) => void;
  }
}

export {};
