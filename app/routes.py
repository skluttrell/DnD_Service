from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app, db
from app.forms import FilterForm, NewCharacterForm
from app.models import Class, DiscreetLevelFeatures, Feature, Spell, Origin
from app.__convert import __convert
from app.__get_data import __get_data

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title = 'Home')

@app.route('/class/<classname>')
def get_class(classname):
	c = Class.query.filter_by(name=classname).first()
	return render_template('class.html', title='Class: '+c.name, c=c)

@app.route('/spells', methods=[ 'GET', 'POST' ])
def spells():
	spells = []
	form = FilterForm()
	sort = request.args.get('sort')
	sortFilters = { 'class': None, 'origin': None, 'school': None }
	if not sort or url_parse(sort).netloc != '': sort = 'alpha'

	if sort == 'alpha':
		spellQuery = Spell.query
	else:
		spellQuery = Spell.query

		for f in sort.split('|'):
			if f.split('=')[0] == 'class': sortFilters['class'] = f.split('=')[1]
			elif f.split('=')[0] == 'origin': sortFilters['origin'] = f.split('=')[1]
			elif f.split('=')[0] == 'school': sortFilters['school'] = f.split('=')[1]

		if sortFilters['class']: spellQuery.filter(Spell.classes.any(id=Class.query.filter_by(name=sortFilters['class']).first().id))
		if sortFilters['origin']: spellQuery = spellQuery.filter_by(origin_id=Feature.query.filter_by(name=sortFilters['origin']).first().id)
		if sortFilters['school']: spellQuery = spellQuery.filter_by(school=Feature.query.filter_by(name=sortFilters['school'],type='school').first().id)

	for s in spellQuery.all():
		spells.append(s.name)

	sorted(spells)

	return render_template('list_of_spells.html', title='Spells', spells=spells, sort=sort, form=form)

@app.route('/spell/<name>')
def get_spell(name):
	spell = Spell.query.filter_by(name=name.replace('_', '/')).first()
	features = Feature.query.filter(Feature.category.in_([ 'spell effect', 'spell save' ]))
	name = spell.name
	school = Feature.query.filter_by(id=spell.school).first().name
	level = spell.level
	ritual = spell.ritual
	castingtime = spell.castingtime
	range = spell.range
	area_of_effect = spell.area_of_effect
	verbal = spell.verbal
	somatic = spell.somatic
	materials = spell.materials
	duration = spell.duration
	concentration = spell.concentration
	description = __convert(spell.description)
	return render_template('_spell.html', title=spell.name, name=name, school=school, level=level, ritual=ritual, castingtime=castingtime, range=range, area_of_effect=area_of_effect, verbal=verbal, somatic=somatic, materials=materials, duration=duration, concentration=concentration, description=description)

@app.route('/new_character', methods=[ 'GET', 'POST' ])
def NewCharacter():
	form = NewCharacterForm()
	form.subrace.choices = [ (form.subrace.data, form.subrace.data) ]
	if form.validate_on_submit():
		'''
		print(name:',form.name.data)
		print(race:',form.race.data)
		print(subrace:',form.subrace.data)
		print(class:',form.character_class.data)
		print(strength:',form.strength.data)
		print(dexterity:',form.dexterity.data)
		print(constitution:',form.constitution.data)
		print(intelligence:',form.intelligence.data)
		print(wisdom:',form.wisdom.data)
		print(charisma:',form.charisma.data)
		'''
		return redirect(url_for('index'))
	return render_template('new_character_form.html', title='Creating a new character', form=form)

@app.route('/_get_data', methods=[ 'GET', 'POST' ])
def GetData():
	print(request.form['name'])
	data = __get_data(request.form['name'], request.form['type'])
	returnData = ""
	if request.form['data_request'] == 'subrace_names' and not data == None:
		returnData = ""
		count = 0
		for sr in data.subraces:
			returnData += sr.name
			if count < data.subraces.count() - 1: returnData += '|'
			count += 1

	return returnData

@app.route('/test')
def TEST():
	return render_template('test.html', title="test page")