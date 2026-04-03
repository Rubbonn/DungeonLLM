from app.database import get_database_session
from app.types.models import GearItems, WeaponMasteryProperties, Weapons, Tools
from app.types.state import SrdParserState
from app.utilities.functions import retry_exception, get_chat_model
import re

def gear_parser(state: SrdParserState) -> dict:
	print(f"Parsing gear items...")
	from app.entities.items import Gear
	if not 'Equipment' in state['sections'] or not Gear.is_empty():
		return {}

	print(f"Extracting gear items...")
	extraction_regex = re.compile(r'^##(?!#)\s*Adventuring Gear\s*\n([\s\S]*?)(?=\n##(?!#)\s*|\Z)', re.MULTILINE)
	with open('data/temp/Equipment.md', 'r', encoding='utf-8') as source:
		match = extraction_regex.search(source.read())
	if not match:
		return {}

	llm = get_chat_model().with_structured_output(GearItems)
	response: GearItems = retry_exception(func=llm.invoke, input=f'''Extract the gear items from the following text, providing their name, weight, cost and description:
	{match.group(1)}
	''')
	if len(response.items) == 0:
		raise Exception('No gear items found in the text')

	session = get_database_session()
	for item in response.items:
		gear_item = Gear(name=item.name, weight=item.weight, cost=item.cost, description=item.description)
		session.add(gear_item)
	session.commit()
	print("Gear items parsing completed successfully.")
	return {}

def weapon_mastery_properties_parser(state: SrdParserState) -> dict:
	if not 'Equipment' in state['sections']:
		return {}

	print(f"Parsing weapon mastery properties...")
	llm = get_chat_model()
	session = get_database_session()

	extraction_regex = re.compile(r'^##(?!#)\s*Weapons\s*\n([\s\S]*?)(?=\n##(?!#)\s*|\Z)', re.MULTILINE)
	with open('data/temp/Equipment.md', 'r', encoding='utf-8') as source:
		match = extraction_regex.search(source.read())
	if not match:
		return {}

	# Weapon mastery properties extraction
	from app.entities.items import WeaponMasteryProperty
	if WeaponMasteryProperty.is_empty():
		print("Extracting weapon mastery properties...")
		llm_with_structured_output = llm.with_structured_output(WeaponMasteryProperties)
		response: WeaponMasteryProperties = retry_exception(func=llm_with_structured_output.invoke, input=f'''Extract the weapon mastery properties (excluding the normal properties) from the following text, providing their name and description:
		{match.group(1)}
		''')
		if len(response.items) == 0:
			raise Exception('No weapon mastery properties found in the text')

		for item in response.items:
			weapon_mastery_property = WeaponMasteryProperty(name=item.name, description=item.description)
			session.add(weapon_mastery_property)
		session.commit()

	print('Weapon mastery properties parsing completed successfully.')
	return {}

def weapons_parser(state: SrdParserState) -> dict:
	if not 'Equipment' in state['sections']:
		return {}

	print(f"Parsing weapons...")
	llm = get_chat_model()
	session = get_database_session()

	extraction_regex = re.compile(r'^##(?!#)\s*Weapons\s*\n([\s\S]*?)(?=\n##(?!#)\s*|\Z)', re.MULTILINE)
	with open('data/temp/Equipment.md', 'r', encoding='utf-8') as source:
		match = extraction_regex.search(source.read())
	if not match:
		return {}

	# Weapons extraction
	from app.entities.items import Weapon, WeaponProperty, WeaponMasteryProperty
	if Weapon.is_empty():
		print("Extracting weapons...")
		llm_with_structured_output = llm.with_structured_output(Weapons)
		response: Weapons = retry_exception(func=llm_with_structured_output.invoke, input=f'''Extract the weapons from the following text, providing their name, description, damage, damage type, properties, mastery property, weight, and cost:
			{match.group(1)}
			''')
		if len(response.items) == 0:
			raise Exception('No weapons found in the text')

		from sqlalchemy import select
		for item in response.items:
			weapon_mastery_property = session.scalar(
				select(WeaponMasteryProperty).filter_by(name=item.mastery_property))
			weapon = Weapon(name=item.name, damage=item.damage, damage_type=item.damage_type,
			                properties={WeaponProperty(property=property) for property in item.properties}, mastery_property=weapon_mastery_property,
			                weight=item.weight, cost=item.cost)
			session.add(weapon)
		session.commit()

	print("Weapons parsing completed successfully.")
	return {}

def tools_parser(state: SrdParserState) -> dict:
	if not 'Equipment' in state['sections']:
		return {}

	print('Parsing tools...')

	from app.entities.items import Tool
	if not Tool.is_empty():
		return {}

	print('Extracting tools...')
	extraction_regex = re.compile(r'^##(?!#)\s*Tools\s*\n([\s\S]*?)(?=\n##(?!#)\s*|\Z)', re.MULTILINE)
	with open('data/temp/Equipment.md', 'r', encoding='utf-8') as source:
		match = extraction_regex.search(source.read())
	if not match:
		return {}

	llm = get_chat_model().with_structured_output(Tools)
	response: Tools = retry_exception(func=llm.invoke, input=f'''Extract the tools from the following text, providing their properties (extract any variant as a separate tool):
	{match.group(1)}
	''')
	if len(response.items) == 0:
		raise Exception('No tools found in the text')

	session = get_database_session()
	from app.entities.items import Gear
	from sqlalchemy import select
	for item in response.items:
		gear_crafted = session.scalars(select(Gear).where(Gear.name.in_([gear.name for gear in item.craft]))).all()
		tool = Tool(name=item.name, weight=item.weight, cost=item.cost, ability=item.ability, utilize=item.utilize, craft=gear_crafted)
		session.add(tool)
	session.commit()
	print("Tools parsing completed successfully.")
	return {}

def animals_parser(state: SrdParserState) -> dict:
	if not 'Animals' in state['sections']:
		return {}

	print('Parsing animals...')
	from app.entities.creatures import Animal
	if not Animal.is_empty():
		return {}

	print('Extracting animals...')
	from app.types.models import Animals
	llm = get_chat_model().with_structured_output(Animals)
	with open('data/temp/Animals.md', 'r', encoding='utf-8') as source:
		content = source.read()
	response: Animals = retry_exception(func=llm.invoke, input=f'''Extract all animals from the following text and populate each animal's fields according to these rules:

- name: the heading name (e.g. "Allosaurus")
- size: one of Tiny, Small, Medium, Large, Huge, Gargantuan — from the italic line (e.g. "*Large Beast (Dinosaur), Unaligned*")
- creature_type: the creature type from the italic line (e.g. Beast, Monstrosity)
- creature_sub_type: the subtype in parentheses, if present (e.g. "Dinosaur"); empty string if absent
- alignment: from the italic line (e.g. Unaligned, Lawful Good)
- armor_class: integer value after "**AC**"
- hit_points: the average value after "**HP**" (the integer before the parenthesis, e.g. 51 from "51 (6d10 + 18)")
- hit_points_formula: the dice formula in parentheses after "**HP**" (e.g. "6d10+18")
- speed: a dict mapping each movement type (Walk, Climbing, Flying, Swimming, Burrowing) to an object with:
  - speed: integer value in feet
  - conditions: any condition string in parentheses, e.g. "(GM\'s choice)"; empty string if none
  Parse "**Speed** 60 ft." as Walk=60; "**Speed** 20 ft., Climb 30 ft." as Walk=20, Climbing=30.
  If a line has two options like "Climb or Fly 20 ft. (GM\'s choice)", assign the same speed and condition to both movement types.
- abilities: a dict mapping each ability (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma) to a tuple containing (score, modifier, save_modifier) from the stat table
- skill_proficiencies: list of skills listed under "**Skills**" (e.g. Perception, Athletics) with their associated bonuses (e.g. "+3 Perception" → {{"Perception": 3}})
- languages: list of languages under "**Languages**"; empty list if "None"
- challenge_rating: the CR value after "**CR**" (e.g. 2, 1/2 → 0.5)
- experience_points: the XP value after "XP" in the CR line (e.g. 450)
- initiative_bonus: the signed integer in parentheses after "**Initiative**" (e.g. "+1 (11)" → 1)

Text:
{content}
''')
	if len(response.items) == 0:
		raise Exception('No animals found in the text')

	session = get_database_session()
	from app.entities.creatures import Creature, CreatureAbility, SkillProficiencies, Language, CreatureSpeed
	for animal in response.items:
		a = Animal(
			creature=Creature(
				name=animal.name,
			    size=animal.size,
			    abilities={ability: CreatureAbility(ability=ability, value=value, modifier=modifier, save_modifier=save_modifier) for ability, (value, modifier, save_modifier) in animal.abilities.items()},
				armor_class=animal.armor_class,
				hit_points=animal.hit_points,
				skill_proficiencies=[SkillProficiencies(skill=skill, bonus=bonus) for skill, bonus in animal.skill_proficiencies.items()],
				languages=[Language(language=language) for language in animal.languages],
				alignment=animal.alignment,
				speed={speed_type: CreatureSpeed(speed_type=speed_type, speed=speed.speed, conditions=speed.conditions) for speed_type, speed in animal.speed.items()}
			),
			creature_type=animal.creature_type,
			creature_sub_type=animal.creature_sub_type,
			hit_points_formula=animal.hit_points_formula,
			experience_points=animal.experience_points,
			initiative_bonus=animal.initiative_bonus,
			challenge_rating=animal.challenge_rating,
		)
		session.add(a)
	session.commit()
	print('Animals parsing completed successfully.')
	return {}