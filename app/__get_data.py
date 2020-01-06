from app import app, db
from app.models import Class, Race

def __get_data(name, type=None):
	if type == 'class':
		return Class.query.filter_by(name=name).first()
	elif type == 'race':
		return Race.query.filter_by(name=name).first()