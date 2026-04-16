import type { AbilityType, Alignment, CreatureAbility, CreatureSpeed, Language, PlayerState, Size, Skill, SkillProficiency, SpeedType } from '../states/player.svelte.ts';


function randInt(min: number, max: number): number {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

function choice<T>(arr: T[]): T {
	return arr[Math.floor(Math.random() * arr.length)];
}

function sample<T>(arr: T[], k: number): T[] {
	const shuffled = [...arr].sort(() => Math.random() - 0.5);
	return shuffled.slice(0, k);
}

function abilityModifier(score: number): number {
	return Math.floor((score - 10) / 2);
}

const ALL_ABILITY_TYPES: AbilityType[] = [
	'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma',
];

const ALL_SIZES: Size[] = ['Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan'];

const ALL_ALIGNMENTS: Alignment[] = [
	'Unaligned',
	'Lawful Good', 'Neutral Good', 'Chaotic Good',
	'Lawful Neutral', 'Neutral', 'Chaotic Neutral',
	'Lawful Evil', 'Neutral Evil', 'Chaotic Evil',
];

const ALL_SKILLS: Skill[] = [
	'Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception',
	'History', 'Insight', 'Intimidation', 'Investigation', 'Medicine',
	'Nature', 'Perception', 'Performance', 'Persuasion', 'Religion',
	'Sleight of Hand', 'Stealth', 'Survival',
];

const ALL_LANGUAGES: Language[] = [
	'Common', 'Common (Sign Language)', 'Draconic', 'Dwarvish', 'Elvish',
	'Giant', 'Gnomish', 'Goblin', 'Halfling', 'Orc',
	'Abyssal', 'Celestial', 'Deep Speech', 'Infernal', 'Primordial', 'Sylvan', 'Undercommon',
];

const OPTIONAL_SPEEDS: SpeedType[] = ['Climbing', 'Swimming', 'Flying', 'Burrowing'];

export function createRandomPlayer(): PlayerState {
	const abilities: Partial<Record<AbilityType, CreatureAbility>> = {};
	for (const abilityType of ALL_ABILITY_TYPES) {
		const score = randInt(3, 18);
		const modifier = abilityModifier(score);
		abilities[abilityType] = {
			ability: abilityType,
			value: score,
			modifier,
			save_modifier: modifier,
		};
	}

	const speed: Partial<Record<SpeedType, CreatureSpeed>> = {
		Walk: {
			speed_type: 'Walk',
			speed: randInt(25, 40),
			conditions: '',
		},
	};
	const extraSpeeds = sample(OPTIONAL_SPEEDS, randInt(0, 2));
	for (const speedType of extraSpeeds) {
		speed[speedType] = {
			speed_type: speedType,
			speed: randInt(10, 40),
			conditions: speedType === 'Flying' ? 'Hover' : '',
		};
	}

	const skill_proficiencies: SkillProficiency[] = sample(ALL_SKILLS, randInt(0, 4)).map(
		(skill) => ({ skill, bonus: null }),
	);

	const languages = sample(ALL_LANGUAGES, randInt(1, 3)) as Language[];

	return $state({
		id: null,
		name: `Player-${Math.random().toString(16).slice(2, 10)}`,
		level: randInt(1, 5),
		size: choice(ALL_SIZES),
		alignment: choice(ALL_ALIGNMENTS),
		armor_class: randInt(10, 20),
		hit_points: randInt(6, 40),
		abilities,
		speed,
		skill_proficiencies,
		languages,
		traits: [],
	});
}
