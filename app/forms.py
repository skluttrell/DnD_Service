from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app import app, db
from app.models import Class, Feature, Origin, Race

class FilterForm(FlaskForm):
	classes = [ (None, 'filter by class') ]
	origins = [ (None, 'filter by origin') ]
	schools = [ (None, 'filter by school') ]
	for c in Class.query.all(): classes.append((c.name, c.name))
	for o in Origin.query.all(): origins.append((o.name, o.name))
	for s in Feature.query.filter_by(type='school').all(): schools.append((s.name, s.name))
	class_filter = SelectField('origin', choices=classes)
	origin_filter = SelectField('origin', choices=origins)
	school_filter = SelectField('school', choices=schools)
	submit = SubmitField('Apply')

class NewCharacterForm(FlaskForm):
	races = [ (None, '--select--') ]
	for entry in Race.query.all():
		races.append((entry.name, entry.name))
	classes = [ (None, '--select--') ]
	for entry in Class.query.all():
		classes.append((entry.name, entry.name))
	name = StringField('Character name', validators=[DataRequired()])
	race = SelectField('race', choices=races)
	subrace = SelectField("subrace", choices=[ (None, '--select--') ])
	character_class = SelectField('class', choices=classes)
	strength = IntegerField('strength', validators=[DataRequired()])
	dexterity = IntegerField('dexterity', validators=[DataRequired()])
	constitution = IntegerField('constitution', validators=[DataRequired()])
	intelligence = IntegerField('intelligence', validators=[DataRequired()])
	wisdom = IntegerField('wisdom', validators=[DataRequired()])
	charisma = IntegerField('charisma', validators=[DataRequired()])
	submit = SubmitField('Create character')