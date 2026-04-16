export type AbilityType = 'Strength' | 'Dexterity' | 'Constitution' | 'Intelligence' | 'Wisdom' | 'Charisma';

export type Size = 'Tiny' | 'Small' | 'Medium' | 'Large' | 'Huge' | 'Gargantuan';

export type Alignment =
	| 'Unaligned'
	| 'Lawful Good' | 'Neutral Good' | 'Chaotic Good'
	| 'Lawful Neutral' | 'Neutral' | 'Chaotic Neutral'
	| 'Lawful Evil' | 'Neutral Evil' | 'Chaotic Evil';

export type SpeedType = 'Walk' | 'Climbing' | 'Crawling' | 'Flying' | 'Jumping' | 'Swimming' | 'Burrowing';

export type Skill =
	| 'Acrobatics' | 'Animal Handling' | 'Arcana' | 'Athletics' | 'Deception'
	| 'History' | 'Insight' | 'Intimidation' | 'Investigation' | 'Medicine'
	| 'Nature' | 'Perception' | 'Performance' | 'Persuasion' | 'Religion'
	| 'Sleight of Hand' | 'Stealth' | 'Survival';

export type Language =
	| 'Common' | 'Common (Sign Language)' | 'Draconic' | 'Dwarvish' | 'Elvish'
	| 'Giant' | 'Gnomish' | 'Goblin' | 'Halfling' | 'Orc'
	| 'Abyssal' | 'Celestial' | 'Deep Speech' | 'Infernal' | 'Primordial' | 'Sylvan' | 'Undercommon';

export interface CreatureAbility {
	ability: AbilityType;
	value: number;
	modifier: number;
	save_modifier: number;
}

export interface CreatureSpeed {
	speed_type: SpeedType;
	speed: number;
	conditions: string;
}

export interface SkillProficiency {
	skill: Skill;
	bonus: number | null;
}

export interface CreatureTrait {
	name: string;
	description: string;
}

export interface PlayerState {
	id: number | null;
	name: string;
	level: number;
	size: Size;
	alignment: Alignment;
	armor_class: number;
	hit_points: number;
	abilities: Partial<Record<AbilityType, CreatureAbility>>;
	speed: Partial<Record<SpeedType, CreatureSpeed>>;
	skill_proficiencies: SkillProficiency[];
	languages: Language[];
	traits: CreatureTrait[];
}

const playerState: PlayerState = $state({
	id: null,
	name: '',
	level: 1,
	size: 'Medium',
	alignment: 'Neutral',
	armor_class: 10,
	hit_points: 10,
	abilities: {},
	speed: {},
	skill_proficiencies: [],
	languages: [],
	traits: [],
});

export default playerState;
