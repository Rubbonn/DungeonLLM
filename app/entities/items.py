from app.database import Base
from app.entities.features import AbilityType
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

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