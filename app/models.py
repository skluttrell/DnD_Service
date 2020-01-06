from app import app, db

race_feature_list = db.Table('race_feature_list',
	db.Column('race_id', db.Integer, db.ForeignKey('race.id'), primary_key=True),
	db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True)
)

subrace_feature_list = db.Table('subrace_feature_list',
	db.Column('subrace_id', db.Integer, db.ForeignKey('subrace.id'), primary_key=True),
	db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True)
)

class_feature_list = db.Table('class_feature_list',
	db.Column('class_id', db.Integer, db.ForeignKey('class.id'), primary_key=True),
	db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True)
)

class_specialty_feature_list = db.Table('specialty_feature_list',
	db.Column('class_specialty_id', db.Integer, db.ForeignKey('class_specialty.id'), primary_key=True),
	db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True)
)

class_specialty_list = db.Table('class_specialty_list',
	db.Column('class_id', db.Integer, db.ForeignKey('class.id'), primary_key=True),
	db.Column('class_specialty_id', db.Integer, db.ForeignKey('class_specialty.id'), primary_key=True)
)

class_discreet_list = db.Table('class_discreet_list',
	db.Column('class_id', db.Integer, db.ForeignKey('class.id'), primary_key=True),
	db.Column('discreet_level_features_id', db.Integer, db.ForeignKey('discreet_level_features.id'), primary_key=True)
)

class_specialty_discreet_list = db.Table('class_specialty_discreet_list',
	db.Column('class_specialty_id', db.Integer, db.ForeignKey('class_specialty.id'), primary_key=True),
	db.Column('discreet_level_features_id', db.Integer, db.ForeignKey('discreet_level_features.id'), primary_key=True)
)

spells_by_effect_type_list = db.Table('spells_by_effect_type_list',
	db.Column('spell_id', db.Integer, db.ForeignKey('spell.id'), primary_key=True),
	db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True)
)

spells_by_attack_or_save_list = db.Table('spells_by_attack_or_save_list',
	db.Column('spell_id', db.Integer, db.ForeignKey('spell.id'), primary_key=True),
	db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True)
)

spells_by_class_list = db.Table('spells_by_class_list',
	db.Column('spell_id', db.Integer, db.ForeignKey('spell.id'), primary_key=True),
	db.Column('class_id', db.Integer, db.ForeignKey('class.id'), primary_key=True)
)

feature_skills_list = db.Table('feature_skills_list',
	db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True),
	db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
)

feature_items_list = db.Table('feature_items_list',
	db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True),
	db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True)
)

items_in_inventory_by_character = db.Table('items_in_inventory_by_character',
	db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True),
	db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True)
)

available_spells_by_character = db.Table('available_spells_by_character',
	db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True),
	db.Column('spell_id', db.Integer, db.ForeignKey('spell.id'), primary_key=True)
)

class Character(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32), nullable=False) # The character's name
	race_id = db.Column(db.Integer, db.ForeignKey('race.id'))
	subrace_id = db.Column(db.Integer, db.ForeignKey('subrace.id'))
	character_class = db.relationship('CharacterClass', backref='character', lazy='dynamic')
	strength = db.Column(db.Integer, nullable=False) # The ability scores of this character
	dexterity = db.Column(db.Integer, nullable=False)
	constitution = db.Column(db.Integer, nullable=False)
	intelligence = db.Column(db.Integer, nullable=False)
	wisdom = db.Column(db.Integer, nullable=False)
	charisma = db.Column(db.Integer, nullable=False)
	hit_points = db.Column(db.Integer)
	current_hit_points = db.Column(db.Integer)
	eye_color = db.Column(db.String(16))
	hair_color = db.Column(db.String(16))
	height = db.Column(db.String(15))
	weight = db.Column(db.Integer)
	age = db.Column(db.Integer)
	alignment = db.Column(db.String(15))
	appearance = db.Column(db.text)
	background = db.Column(db.text)
	personality = db.Column(db.String(1000))
	ideals = db.Column(db.String(1000))
	bonds = db.Column(db.String(1000))
	flaws = db.Column(db.String(1000))
	languages = db.Column(db.String(192))
	inventory = db.relationship('Item', secondary=items_in_inventory_by_character, lazy='subquery', backref=db.backref('item', lazy=True))
	spells = db.relationship('Spell', secondary=available_spells_by_character, lazy='subquery', backref=db.backref('item', lazy=True))
	#notes = db.relationship

class CharacterClass(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
	class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
	specialty_id = db.Column(db.Integer, db.ForeignKey('class_specialty.id'))
	level = db.Column(db.Integer, nullable=False)

class Origin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

class Race(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32), unique=True, nullable=False)
	origin_id = db.Column(db.Integer)
	description = db.Column(db.String(10000))
	traits_description = db.Column(db.String(120))
	improved_strength = db.Column(db.Integer)
	improved_dexterity = db.Column(db.Integer)
	improved_constitution = db.Column(db.Integer)
	improved_intelligence = db.Column(db.Integer)
	improved_wisdom = db.Column(db.Integer)
	improved_charisma = db.Column(db.Integer)
	age = db.Column(db.String(280))
	alignment = db.Column(db.String(360))
	build = db.Column(db.String(120))
	size_type = db.Column(db.String(15))
	base_speed = db.Column(db.String(120))
	subrace_description = db.Column(db.String(360))
	subraces = db.relationship('Subrace', backref='race', lazy='dynamic')
	race_features = db.relationship('Feature', secondary=race_feature_list, lazy='subquery', backref=db.backref('race', lazy=True))
	extra_information = db.Column(db.String(2500))

class Subrace(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	race_id = db.Column(db.Integer, db.ForeignKey('race.id'))
	name = db.Column(db.String(32), unique=True, nullable=False)
	origin_id = db.Column(db.Integer)
	description = db.Column(db.String(2500))
	subrace_features = db.relationship('Feature', secondary=subrace_feature_list, lazy='subquery', backref=db.backref('subrace', lazy=True))

class BreathWeapon(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	race_id = db.Column(db.Integer, db.ForeignKey('race.id'))
	dragon = db.Column(db.String(8))
	damage_type = db.Column(db.String(12))
	breath_weapon = db.Column(db.String(16))
	save = db.Column(db.String(3))

class Class(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32), unique=True, nullable=False)
	origin_id = db.Column(db.Integer)
	description = db.Column(db.String(5000))
	creating_this_class = db.Column(db.String(2500))
	hit_dice = db.Column(db.String(7))
	alt_hit_points_at_higher_levels = db.Column(db.Integer)
	discreet_level_features = db.relationship('DiscreetLevelFeatures', secondary=class_discreet_list, lazy='subquery', backref=db.backref('class', lazy=True))
	specialty_header = db.Column(db.String(30))
	specialty_description = db.Column(db.String(2000))
	specialties = db.relationship('ClassSpecialty', secondary=class_specialty_list, lazy='subquery', backref=db.backref('class', lazy=True))
	class_features = db.relationship('Feature', secondary=class_feature_list, lazy='subquery', backref=db.backref('class', lazy=True))
	extra_information = db.Column(db.String(2500))

	def __repr__(self): return self.id

class ClassSpecialty(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32), unique=True, nullable=False)
	description = db.Column(db.String(3000))
	discreet_level_features = db.relationship('DiscreetLevelFeatures', secondary=class_specialty_discreet_list, lazy='subquery', backref=db.backref('class_specialty', lazy=True))
	class_specialty_features = db.relationship('Feature', secondary=class_specialty_feature_list, lazy='subquery', backref=db.backref('class_specialty', lazy=True))

class DiscreetLevelFeatures(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(20))
	level = db.Column(db.Integer)
	features = db.Column(db.String(50))
	rages = db.Column(db.Integer)
	rage_damage = db.Column(db.Integer)
	martial_arts = db.Column(db.String(7))
	ki_points = db.Column(db.Integer)
	unarmored_movement = db.Column(db.Integer)
	sneak_attack = db.Column(db.String(7))
	cantrips_known = db.Column(db.Integer)
	spells_known = db.Column(db.Integer)
	sorcerer_points = db.Column(db.Integer)
	spell_slots = db.Column(db.Integer)
	slot_level = db.Column(db.Integer)
	invocations_known = db.Column(db.Integer)
	slots_for_1st = db.Column(db.Integer)
	slots_for_2nd = db.Column(db.Integer)
	slots_for_3rd = db.Column(db.Integer)
	slots_for_4th = db.Column(db.Integer)
	slots_for_5th = db.Column(db.Integer)
	slots_for_6th = db.Column(db.Integer)
	slots_for_7th = db.Column(db.Integer)
	slots_for_8th = db.Column(db.Integer)
	slots_for_9th = db.Column(db.Integer)

class EldritchInvocation(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))
	origin_id = db.Column(db.Integer)
	prerequisite_level = db.Column(db.Integer)
	prerequisite_spell = db.Column(db.Integer)
	prerequisite_specialty = db.Column(db.Integer)
	prerequisite_pact = db.Column(db.String(25))
	description = db.Column(db.String(1000))

class Spell(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32), unique=True)
	origin_id = db.Column(db.Integer)
	page = db.Column(db.Integer)
	description = db.Column(db.String(4000))
	level = db.Column(db.Integer, index=True)
	school = db.Column(db.Integer)
	classes = db.relationship('Class', secondary=spells_by_class_list, lazy='subquery', backref=db.backref('class', lazy=True))
	castingtime = db.Column(db.String(95))
	ritual = db.Column(db.Boolean)
	concentration = db.Column(db.Boolean)
	range = db.Column(db.Integer)
	area_of_effect = db.Column(db.String(30))
	verbal = db.Column(db.Boolean)
	somatic = db.Column(db.Boolean)
	materials = db.Column(db.String(350))
	duration = db.Column(db.String(30))
	notes = db.Column(db.String(140))
	attack_or_save = db.relationship('Feature', secondary=spells_by_attack_or_save_list, lazy='subquery', backref=db.backref('attack_or_save', lazy=True))
	effect_type = db.relationship('Feature', secondary=spells_by_effect_type_list, lazy='subquery', backref=db.backref('effect_type', lazy=True))

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32), unique=True, nullable=False)
	origin_id = db.Column(db.Integer)
	cost = db.Column(db.Integer)
	type = db.Column(db.String(16))
	category = db.Column(db.String(16))
	hit_modifier = db.Column(db.Integer)
	damage_type = db.Column(db.String(24))
	damage_dice = db.Column(db.String(7))
	range = db.Column(db.String(32))
	properties = db.Column(db.String(192))

class Feature(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(20))
	origin_id = db.Column(db.Integer, db.ForeignKey('origin.id'))
	level = db.Column(db.Integer)
	name = db.Column(db.String(64))
	prerequisite = db.Column(db.String(120))
	description = db.Column(db.String(10000))
	type = db.Column(db.String(32))
	category = db.Column(db.String(32))
	list_by_category = db.Column(db.String(64))
	improved_strength = db.Column(db.Integer)
	improved_dexterity = db.Column(db.Integer)
	improved_constitution = db.Column(db.Integer)
	improved_intelligence = db.Column(db.Integer)
	improved_wisdom = db.Column(db.Integer)
	improved_charisma = db.Column(db.Integer)
	improved_ability_choice = db.Column(db.Boolean)
	ability_improvement_acceptions = db.Column(db.String(19))
	number_of = db.Column(db.Integer)
	dragon_ancestry = db.Column(db.Boolean)
	items = db.relationship('Item', secondary=feature_items_list, lazy='subquery', backref=db.backref('feature', lazy=True))
	skills = db.relationship('Skill', secondary=feature_skills_list, lazy='subquery', backref=db.backref('feature', lazy=True))	

class Skill(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	ability = db.Column(db.String(3))