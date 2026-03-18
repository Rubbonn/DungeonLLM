from __future__ import annotations
from abc import abstractmethod
from app.entities.features import AbilityType
from app.utilities.functions import throw_dice
from pydantic import BaseModel, Field
from typing import Literal, TypeVar, Generic, TYPE_CHECKING
if TYPE_CHECKING:
	from app.types.state import State

ActionT = TypeVar('ActionT', bound=str)

class BaseAction(BaseModel, Generic[ActionT]):
	action: ActionT = Field(description='The action to perform')
	reason: str = Field(description='The reason why this action is necessary')
	result: str = Field(description='The result of the action', default='')

	@abstractmethod
	def execute(self, state: State):
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
	difficulty_class: int = Field(description='The difficulty class to equal or exceed to succeed')

	def execute(self, state: State):
		dice_result = throw_dice(20)
		player_modifier = state['player'].get_ability_modifier(self.ability)
		if dice_result == 1 or dice_result + player_modifier < self.difficulty_class:
			self.result = f'Ability check {self.ability.value} failed. Rolled: {dice_result}, Player modifier: {player_modifier}, Difficulty class: {self.difficulty_class}.'
		elif dice_result == 20 or dice_result + player_modifier >= self.difficulty_class:
			self.result = f'Ability check {self.ability.value} succeeded. Rolled: {dice_result}, Player modifier: {player_modifier}, Difficulty class: {self.difficulty_class}.'
		else:
			raise Exception(f'Invalid dice roll result: {dice_result}.')


class Plan(BaseModel):
	actions: list[AbilityCheckAction] = Field(description='A list of actions to execute.', default_factory=list)

	def __str__(self) -> str:
		if len(self.actions) == 0:
			return 'No actions in the plan.'
		
		plan_str = 'Actions executed:\n|Action|Reason|Result|\n|-|-|-|\n'
		return plan_str + '\n'.join([f'|{action.action}|{action.reason}|{action.result}|' for action in self.actions])