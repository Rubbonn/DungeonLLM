from app.database import Base
from app.entities.features import AbilityType
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

class Item:
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	weight: Mapped[float]
	cost: Mapped[float]

class Gear(Base, Item):
	__tablename__ = 'gear'
	description: Mapped[str]

class Tool(Base, Item):
	__tablename__ = 'tools'
	ability: Mapped[AbilityType]
	utilize: Mapped[str]
	craft: Mapped[list[Gear]] = relationship(secondary=Table(
		'tool_craft',
		Base.metadata,
		Column('tool_id', ForeignKey('tools.id'), primary_key=True),
		Column('gear_id', ForeignKey('gear.id'), primary_key=True)
	))

class DamageType(Base):
	__tablename__ = 'damage_types'
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	examples: Mapped[str]

class WeaponProperty(Base):
	__tablename__ = 'weapon_properties'
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	description: Mapped[str]

class WeaponMasteryProperty(Base):
	__tablename__ = 'weapon_mastery_properties'
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	description: Mapped[str]

class Weapon(Base, Item):
	__tablename__ = 'weapons'
	damage: Mapped[str]
	_damage_type_id: Mapped[int] = mapped_column('damage_type_id', ForeignKey('damage_types.id'))
	damage_type: Mapped[DamageType] = relationship()
	properties: Mapped[list[WeaponProperty]] = relationship(secondary=Table(
		'weapons_properties',
		Base.metadata,
		Column('weapon_id', ForeignKey('weapons.id'), primary_key=True),
		Column('property_id', ForeignKey('weapon_properties.id'), primary_key=True)
	))
	_mastery_property_id: Mapped[int] = mapped_column('mastery_property_id', ForeignKey('weapon_mastery_properties.id'))
	mastery_property: Mapped[WeaponMasteryProperty] = relationship()

class Armor(Base, Item):
	__tablename__ = 'armors'
	minutes_to_equip: Mapped[int]
	minutes_to_unequip: Mapped[int]
	armor_class: Mapped[int]
	ability_modifier: Mapped[AbilityType]
	minimum_strength: Mapped[Optional[int]]
	has_stealth_disadvantage: Mapped[bool]