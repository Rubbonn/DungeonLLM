from app.database import Base
import app.entities.features as features
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
	
	def get_bio(self) -> str:
		return f'Name: {self.name}\nSize: {self.size.value}'
	
	def get_abilities(self) -> str:
		return '\n'.join([f'{ability}: {value.value}' for ability, value in self.abilities.items()])

	def get_ability_modifier(self, ability: features.AbilityType) -> int:
		match self.abilities[ability].value:
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