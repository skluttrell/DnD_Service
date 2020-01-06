from app import app, db
from app.models import Origin

o1 = Origin(name='Player\'s Hand Book')

db.session.add( o1 )
db.session.commit()