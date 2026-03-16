from app.entities.features import AbilityType
from pydantic import BaseModel, Field
from typing import Literal


class BaseAction(BaseModel):
	action: str = Field(description='The action to perform')
	reason: str = Field(description='The reason why this action is necessary')
	result: str = Field(description='The result of the action', default='')

class AbilityCheckAction(BaseAction):
	action: Literal['ability_check'] = Field(description='''Action to perform an ability check.
EXAMPLES OF CHECKS:
Strength: Lift, push, pull, or break something
Dexterity: Move nimbly, quickly, or quietly
Constitution: Push your body beyond normal limits
Intelligence: Reason or remember
Wisdom: Notice things in the environment or in creatures’ behavior
Charisma: Influence, entertain, or deceive''', default='ability_check')
	ability: AbilityType = Field(description='The ability to check against')
	difficulty_class: int = Field(description='The difficulty class to equal or exceed to succeed')


class Plan(BaseModel):
	actions: list[AbilityCheckAction] = Field(description='A list of actions to execute.', default_factory=list)