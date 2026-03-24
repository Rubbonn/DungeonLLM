// ─── Router ───────────────────────────────────────────────────────────────────

export type PageName =
  | 'home'
  | 'character-creation'
  | 'load-campaign'
  | 'new-campaign'
  | 'game'
  | 'battle';

// ─── Campaign ─────────────────────────────────────────────────────────────────

/** A saved / running campaign (used in LoadCampaign, App, GameScreen, BattleView) */
export interface Campaign {
  id: number | string;
  title: string;
  thumbnailUrl?: string;
  charName: string;
  charClass: string;
  charLevel: number;
  lastSave: string;
}

/** A campaign template or draft shown on the NewCampaign page */
export interface TemplateCampaign {
  id: string;
  title: string;
  desc: string;
  players: string | null;
  level: string | null;
  badge: string | null;
  badgeColor: 'gold' | 'muted' | null;
  thumbColor: string;
  draft: boolean;
}

/**
 * Minimal context passed to game screens.
 * Both `Campaign` and `TemplateCampaign` are structurally assignable to this.
 */
export interface GameSession {
  title?: string;
  charName?: string;
  charClass?: string;
  charLevel?: number;
}

// ─── Character ────────────────────────────────────────────────────────────────

export type AttrKey =
  | 'forza'
  | 'destrezza'
  | 'costituzione'
  | 'intelligenza'
  | 'saggezza'
  | 'carisma';

export type AttrMap = Record<AttrKey, number>;

export type AttrMode = 'standard' | 'random';

/** A single core-attribute entry shown in the attribute grid (GameScreen / BattleView) */
export interface AttrEntry {
  key: string;
  value: number;
  icon: string;
}

/** Character data snapshot used inside GameScreen and BattleView */
export interface CharData {
  name: string;
  cls: string;
  level: number;
  hp: number;
  maxHp: number;
  mana: number;
  maxMana: number;
  attrs: AttrEntry[];
}

// ─── Inventory / equipment ────────────────────────────────────────────────────

export interface EquipmentItem {
  id: number;
  icon: string;
  name: string;
  slot: string;
  badge: string;
  badgeColor: 'green' | 'blue';
}

export interface AbilityItem {
  id: number;
  name: string;
  type: 'PASSIVE' | 'COMBAT';
  desc: string;
}

export interface InventoryItem {
  id: number;
  count: number | null;
  icon: string;
}

// ─── Chat ─────────────────────────────────────────────────────────────────────

export interface ChatMessage {
  id: number;
  role: 'master' | 'player';
  text: string;
  note?: string;
  check?: string;
}

// ─── Battle map ───────────────────────────────────────────────────────────────

export type ToolId = 'hand' | 'pen' | 'ruler';

export interface MapTool {
  id: ToolId;
  icon: string;
}

export interface MapToken {
  x: number;
  y: number;
  label: string;
}

export interface EnemyToken extends MapToken {
  hp: number;
  maxHp: number;
}

// ─── UI components ────────────────────────────────────────────────────────────

export type ConfirmVariant = 'danger' | 'warning' | 'info';

export type SelectOption = string | { value: string; label: string };

export interface SettingsValues {
  voiceEnabled: boolean;
  subtitlesEnabled: boolean;
}
