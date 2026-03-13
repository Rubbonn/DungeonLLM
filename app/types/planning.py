class Plan:
	@classmethod
	def get_json_schema(cls) -> dict:
		return {
			'title': 'Execution plan',
			'description': 'A plan of actions to execute based on the current state of the game.',
			'type': 'array',
			'items': {
				'oneOf': [
					{
						'description': 'No action to be taken',
						'type': 'object',
						'properties': {
							'action': {'const': 'no_action'}
						}
					}
				]
			}
		}

	@classmethod
	def from_results(cls, plan: list[dict], results: list[dict]) -> list[dict]:
		if len(plan) != len(results):
			raise ValueError('Plan and results must have the same length')

		return [{**action, 'result': result} for action, result in zip(plan, results)]