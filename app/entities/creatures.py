from app.database import Base
from app.engine.hooks.registry import HOOK_LIST, HookRegistry
import app.entities.features as features
from random import randint
from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship, attribute_mapped_collection
from typing import Optional

class CreatureAbility(Base):
	__tablename__ = 'creature_abilities'
	creature_id: Mapped[int] = mapped_column(ForeignKey('creatures.id'), primary_key=True)
	ability: Mapped[features.AbilityType] = mapped_column(primary_key=True)
	value: Mapped[int]
	modifier: Mapped[Optional[int]]
	save_modifier: Mapped[Optional[int]]

class SkillProficiencies(Base):
	__tablename__ = 'skill_proficiencies'
	id: Mapped[int] = mapped_column(primary_key=True)
	skill: Mapped[features.Skill]
	bonus: Mapped[Optional[int]]

	@classmethod
	def get_base_bonus(cls, level: int) -> int:
		match level:
			case 1 | 2 | 3 | 4:
				return 2
			case 5 | 6 | 7 | 8:
				return 3
			case 9 | 10 | 11 | 12:
				return 4
			case 13 | 14 | 15 | 16:
				return 5
			case 17 | 18 | 19 | 20:
				return 6
			case 21 | 22 | 23 | 24:
				return 7
			case 25 | 26 | 27 | 28:
				return 8
			case 29 | 30:
				return 9
			case _:
				raise ValueError('Invalid level or challenge rate')

	def register_hooks(self, registry: HookRegistry):
		from app.engine.hooks.states import AbilityCheckState

		@registry.register_hook(HOOK_LIST.ABILITY_CHECK_POST_ROLL)
		def apply_bonus(state: AbilityCheckState) -> None:
			pass

class Language(Base):
	__tablename__ = 'languages'
	id: Mapped[int] = mapped_column(primary_key=True)
	language: Mapped[features.Language]

class CreatureSpeed(Base):
	__tablename__ = 'creature_speeds'
	creature_id: Mapped[int] = mapped_column(ForeignKey('creatures.id'), primary_key=True)
	speed_type: Mapped[features.Speed] = mapped_column(primary_key=True)
	speed: Mapped[int]
	conditions: Mapped[str]

class CreatureTrait(Base):
	__tablename__ = 'creature_traits'
	creature_id: Mapped[int] = mapped_column(ForeignKey('creatures.id'), primary_key=True)
	name: Mapped[str] = mapped_column(primary_key=True)
	description: Mapped[str]

class Creature(Base):
	__tablename__ = 'creatures'
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	size: Mapped[features.Size]
	abilities: Mapped[dict[features.AbilityType, CreatureAbility]] = relationship(collection_class=attribute_mapped_collection('ability'))
	armor_class: Mapped[int]
	hit_points: Mapped[int]
	skill_proficiencies: Mapped[list[SkillProficiencies]] = relationship(secondary=Table('creature_skill_proficiencies', Base.metadata, Column('creature_id', ForeignKey('creatures.id'), primary_key=True), Column('skill_id', ForeignKey('skill_proficiencies.id'), primary_key=True)))
	languages: Mapped[list[Language]] = relationship(secondary=Table('creature_languages', Base.metadata, Column('creature_id', ForeignKey('creatures.id'), primary_key=True), Column('language_id', ForeignKey('languages.id'), primary_key=True)))
	alignment: Mapped[features.Alignment]
	speed: Mapped[dict[features.Speed, CreatureSpeed]] = relationship(collection_class=attribute_mapped_collection('speed_type'))
	traits: Mapped[list[CreatureTrait]] = relationship()

	def _on_load(self) -> None:
		self.hook_registry = HookRegistry()
	
	def get_bio(self) -> str:
		lines = [f'# {self.name}', '', f'*{self.size.value}, {self.alignment.value}*', '']
		lines += [f'**AC** {self.armor_class}', '', f'**HP** {self.hit_points}', '']

		speed_labels = {
			features.Speed.Walk: '',
			features.Speed.Swimming: 'Swim',
			features.Speed.Flying: 'Fly',
			features.Speed.Climbing: 'Climb',
			features.Speed.Burrowing: 'Burrow',
			features.Speed.Crawling: 'Crawl',
			features.Speed.Jumping: 'Jump',
		}
		speed_order = [features.Speed.Walk, features.Speed.Flying, features.Speed.Swimming,
					   features.Speed.Climbing, features.Speed.Burrowing, features.Speed.Crawling, features.Speed.Jumping]
		speed_parts = []
		for speed_type in speed_order:
			if speed_type not in self.speed:
				continue
			speed_data = self.speed[speed_type]
			label = speed_labels.get(speed_type, speed_type.value)
			cond = f' ({speed_data.conditions})' if speed_data.conditions else ''
			if label:
				speed_parts.append(f'{label} {speed_data.speed} ft.{cond}')
			else:
				speed_parts.append(f'{speed_data.speed} ft.{cond}')
		lines.append(f'**Speed** {", ".join(speed_parts)}')

		lines += ['\n', self.get_abilities()]

		if self.skill_proficiencies:
			def _fmt_bonus(b: Optional[int]) -> str:
				return f'+{b}' if b is not None and b >= 0 else (str(b) if b is not None else '')
			skills_str = ', '.join(f'{sp.skill.value} {_fmt_bonus(sp.bonus)}' for sp in self.skill_proficiencies)
			lines += ['', f'**Skills** {skills_str}']

		if self.languages:
			langs_str = ', '.join(lang.language.value for lang in self.languages)
			lines += ['', f'**Languages** {langs_str}']

		return '\n'.join(lines)

	def get_abilities(self) -> str:
		abbr_map = {
			features.AbilityType.STRENGTH: 'STR',
			features.AbilityType.DEXTERITY: 'DEX',
			features.AbilityType.CONSTITUTION: 'CON',
			features.AbilityType.INTELLIGENCE: 'INT',
			features.AbilityType.WISDOM: 'WIS',
			features.AbilityType.CHARISMA: 'CHA',
		}
		order = [
			features.AbilityType.STRENGTH, features.AbilityType.DEXTERITY, features.AbilityType.CONSTITUTION,
			features.AbilityType.INTELLIGENCE, features.AbilityType.WISDOM, features.AbilityType.CHARISMA,
		]

		def _fmt_mod(val: int) -> str:
			return f'+{val}' if val >= 0 else str(val)

		def _make_cell(ability: features.AbilityType) -> tuple[str, str, str, str]:
			abbr = abbr_map[ability]
			ca = self.abilities.get(ability)
			if ca is None:
				return abbr, '-', '-', '-'
			mod = ca.modifier if ca.modifier is not None else self.get_ability_modifier(ability)
			save = ca.save_modifier if ca.save_modifier is not None else mod
			return abbr, str(ca.value), _fmt_mod(mod), _fmt_mod(save)

		cells = [_make_cell(a) for a in order]

		def _row(trio: list[tuple[str, str, str, str]]) -> str:
			parts = [f'| {c[0]} | {c[1]:<3} | {c[2]:<3} | {c[3]:<4}' for c in trio]
			return ' '.join(parts) + ' |'

		header = '|     |     | MOD | SAVE |     |     | MOD | SAVE |     |     | MOD | SAVE |'
		sep    = '|-----|-----|-----|------|-----|-----|-----|------|-----|-----|-----|------|'
		return '\n'.join([header, sep, _row(cells[:3]), _row(cells[3:])])

	@classmethod
	def get_base_ability_modifier(cls, score: int) -> int:
		match score:
			case 1:
				return -5
			case 2 | 3:
				return -4
			case 4 | 5:
				return -3
			case 6 | 7:
				return -2
			case 8 | 9:
				return -1
			case 10 | 11:
				return 0
			case 12 | 13:
				return 1
			case 14 | 15:
				return 2
			case 16 | 17:
				return 3
			case 18 | 19:
				return 4
			case 20 | 21:
				return 5
			case 22 | 23:
				return 6
			case 24 | 25:
				return 7
			case 26 | 27:
				return 8
			case 28 | 29:
				return 9
			case 30:
				return 10
			case _:
				raise ValueError('Invalid ability value')

	def get_ability_modifier(self, ability: features.AbilityType) -> int:
		from app.engine.hooks.states import AbilityModifierState
		state: AbilityModifierState = {
			'ability': ability,
			'score': self.abilities[ability].value,
			'modifier': Creature.get_base_ability_modifier(self.abilities[ability].value)
		}
		self.hook_registry.execute_hooks(HOOK_LIST.ABILITY_MODIFIER_CALCULATION, state)
		return state['modifier']

	def ability_check(self, ability: features.AbilityType, dc: int, skill: Optional[features.Skill] = None) -> bool:
		if dc < 0:
			raise ValueError('DC must be positive')

		from app.engine.hooks.states import AbilityCheckState
		state: AbilityCheckState = {
			'num_dices': 1,
			'num_sides': 20,
			'creature': self,
			'operation': 'nothing',
			'ability': ability,
			'skill': skill,
			'dc': dc,
			'ability_mod': self.get_ability_modifier(ability),
			'result': 0,
		}
		self.hook_registry.execute_hooks(HOOK_LIST.ABILITY_CHECK_PRE_ROLL, state)

		result = 0
		for _ in range(state['num_dices']):
			throw = randint(1, state['num_sides'])
			match state['operation']:
				case 'add':
					result += throw
				case 'nothing' | _:
					result = throw
		state['result'] = result
		self.hook_registry.execute_hooks(HOOK_LIST.ABILITY_CHECK_POST_ROLL, state)

		state['result'] += state['ability_mod']
		self.hook_registry.execute_hooks(HOOK_LIST.ABILITY_CHECK_POST_CALCULATION, state)

		return state['result'] >= dc


class Animal(Base):
	__tablename__ = 'animals'
	_id_creature: Mapped[int] = mapped_column('id_creature', ForeignKey('creatures.id'), primary_key=True)
	creature: Mapped[Creature] = relationship()
	creature_type: Mapped[features.CreatureType]
	creature_sub_type: Mapped[str]
	hit_points_formula: Mapped[str]
	experience_points: Mapped[int]
	initiative_bonus: Mapped[int]
	challenge_rating: Mapped[float]

class Player(Base):
	__tablename__ = 'players'
	_id_creature: Mapped[int] = mapped_column('id_creature', ForeignKey('creatures.id'), primary_key=True)
	creature: Mapped[Creature] = relationship()