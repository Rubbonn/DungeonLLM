from pathlib import Path
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

from app.entities.items import AbilityName

_database_engine: Engine | None = None
_database_session: Session | None = None

class Base(DeclarativeBase):
	@classmethod
	def is_empty(cls):
		from sqlalchemy import select
		session = get_database_session()
		return not session.scalars(select(cls)).first()

def database_exists() -> bool:
	return Path('data/databases/entities.sqlite').exists()

def get_database_engine() -> Engine:
	global _database_engine
	if _database_engine is None:
		_database_engine = create_engine('sqlite:///data/databases/entities.sqlite')
	return _database_engine

def get_database_session() -> Session:
	global _database_session
	if _database_session is None:
		_database_session = Session(get_database_engine())
	return _database_session

def initialize_database():
	from app.entities import items, creatures, features
	engine = get_database_engine()
	Base.metadata.create_all(engine)
	if AbilityName.is_empty():
		session = get_database_session()
		for ability in features.AbilityType:
			session.add(items.AbilityName(name=ability.value))
		session.commit()