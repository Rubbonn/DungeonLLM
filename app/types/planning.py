from pydantic import BaseModel, Field
from typing import Literal

class ThrowDiceAction(BaseModel):
	action: Literal['throw_dice'] = Field(description='Action to throw a dice', default='throw_dice')
	dice: Literal[4, 6, 8, 10, 12, 20, 100] = Field(description='The dice to throw')
	reason: str = Field(description='The reason why this action is necessary')

class Plan(BaseModel):
	actions: list[ThrowDiceAction] = Field(description='A list of actions to execute.', default_factory=list)