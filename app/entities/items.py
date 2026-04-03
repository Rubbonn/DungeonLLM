from app.database import Base
import app.entities.features as features
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
	ability: Mapped[features.AbilityType]
	utilize: Mapped[str]
	craft: Mapped[list[Gear]] = relationship(secondary=Table(
		'tool_craft',
		Base.metadata,
		Column('tool_id', ForeignKey('tools.id'), primary_key=True),
		Column('gear_id', ForeignKey('gear.id'), primary_key=True)
	))

class WeaponProperty(Base):
	__tablename__ = 'weapon_properties'
	_id_weapon: Mapped[int] = mapped_column('id_weapon', ForeignKey('weapons.id'), primary_key=True)
	property: Mapped[features.WeaponProperty] = mapped_column(primary_key=True)

class Weapon(Base, Item):
	__tablename__ = 'weapons'
	damage: Mapped[str]
	damage_type: Mapped[features.DamageType]
	properties: Mapped[set[WeaponProperty]] = relationship()
	mastery_property: Mapped[features.WeaponMasteryProperty]
	range: Mapped[Optional[int]]
	long_range: Mapped[Optional[int]]
	ammunition: Mapped[Optional[str]]

class Armor(Base, Item):
	__tablename__ = 'armors'
	minutes_to_equip: Mapped[int]
	minutes_to_unequip: Mapped[int]
	armor_class: Mapped[int]
	ability_modifier: Mapped[features.AbilityType]
	minimum_strength: Mapped[Optional[int]]
	has_stealth_disadvantage: Mapped[bool]