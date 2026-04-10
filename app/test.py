from __future__ import annotations

from random import choice, randint, sample
from uuid import uuid4

from sqlalchemy.orm import Session

import app.entities.features as features
from app.database import get_database_session
from app.entities.creatures import Creature, CreatureAbility, CreatureSpeed, Player, SkillProficiencies


def _ability_modifier(score: int) -> int:
	return (score - 10) // 2


def create_random_player(*, persist: bool = True, session: Session | None = None) -> Player:
	"""
	Create a random Player entity for development and manual testing.

	Args:
		persist: When True, the player is inserted and committed into the database.
		session: Optional SQLAlchemy session. If omitted and persist=True, the default database session is used.

	Returns:
		The generated Player entity.
	"""
	abilities: dict[features.AbilityType, CreatureAbility] = {}
	for ability_type in features.AbilityType:
		score = randint(3, 18)
		modifier = _ability_modifier(score)
		abilities[ability_type] = CreatureAbility(
			ability=ability_type,
			value=score,
			modifier=modifier,
			save_modifier=modifier,
		)

	speeds: dict[features.Speed, CreatureSpeed] = {
		features.Speed.Walk: CreatureSpeed(
			speed_type=features.Speed.Walk,
			speed=randint(25, 40),
			conditions='',
		)
	}

	optional_speeds = [
		features.Speed.Climbing,
		features.Speed.Swimming,
		features.Speed.Flying,
		features.Speed.Burrowing,
	]
	for speed_type in sample(optional_speeds, k=randint(0, 2)):
		speeds[speed_type] = CreatureSpeed(
			speed_type=speed_type,
			speed=randint(10, 40),
			conditions='Hover' if speed_type == features.Speed.Flying else '',
		)

	creature = Creature(
		level=randint(1, 5),
		name=f'Player-{uuid4().hex[:8]}',
		size=choice(list(features.Size)),
		abilities=abilities,
		armor_class=randint(10, 20),
		hit_points=randint(6, 40),
		skill_proficiencies=[SkillProficiencies(skill=skill) for skill in sample(list(features.Skill), randint(0, 4))],
		languages=[],
		alignment=choice(list(features.Alignment)),
		speed=speeds,
		traits=[],
	)
	creature.recalculate_all_params()

	player = Player(creature=creature)

	if persist:
		db_session = session or get_database_session()
		db_session.add(player)
		db_session.commit()
		db_session.refresh(player)

	return player
