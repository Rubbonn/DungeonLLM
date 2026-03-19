from app.types.actions import AbilityCheckAction
from pydantic import BaseModel, Field

class Plan(BaseModel):
	actions: list[AbilityCheckAction] = Field(description='A list of actions to execute.', default_factory=list)

	def __str__(self) -> str:
		if len(self.actions) == 0:
			return 'No actions in the plan.'
		
		plan_str = 'Actions executed:\n|Action|Reason|Result|\n|-|-|-|\n'
		return plan_str + '\n'.join([f'|{action.action}|{action.reason}|{action.result}|' for action in self.actions])