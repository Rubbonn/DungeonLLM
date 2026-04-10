from __future__ import annotations
from abc import abstractmethod
from app.entities.features import AbilityType, Skill
from pydantic import BaseModel, Field
from typing import Literal, Optional, TypeVar, Generic, TYPE_CHECKING
if TYPE_CHECKING:
	from app.types.state import GameplayState

ActionT = TypeVar('ActionT', bound=str)

class BaseAction(BaseModel, Generic[ActionT]):
	action: ActionT = Field(description='The action to perform')
	reason: str = Field(description='The reason why this action is necessary')
	result: str = Field(description='The result of the action', default='')

	def execute(self, state: GameplayState):
		pass

class AbilityCheckAction(BaseAction[Literal['ability_check']]):
	action: Literal['ability_check'] = Field(description='''Action to perform an ability check.
EXAMPLES OF CHECKS:
Strength: Lift, push, pull, or break something
Dexterity: Move nimbly, quickly, or quietly
Constitution: Push your body beyond normal limits
Intelligence: Reason or remember
Wisdom: Notice things in the environment or in creatures' behavior
Charisma: Influence, entertain, or deceive''', default='ability_check')
	ability: AbilityType = Field(description='The ability to check against')
	skill: Optional[Skill] = Field(description='The skill associated with the ability, if any')
	difficulty_class: int = Field(description='The difficulty class to equal or exceed to succeed')

	def execute(self, state: GameplayState):
		if self.skill and self.ability != self.skill.ability_type:
			raise Exception('Ability check action must have the same ability type as the skill')

		if state['player'].creature.ability_check(self.ability, self.difficulty_class, self.skill):
			self.result = f'Ability check {self.ability.value} (Skill: {self.skill.value if self.skill else "None"}) succeeded. Difficulty class: {self.difficulty_class}.'
		else:
			self.result = f'Ability check {self.ability.value} (Skill: {self.skill.value if self.skill else "None"}) failed. Difficulty class: {self.difficulty_class}.'