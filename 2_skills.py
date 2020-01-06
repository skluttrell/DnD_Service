from app import app, db
from app.models import Skill

sk1 = Skill(name='animal handling',ability='wis')
sk2 = Skill(name='athletics',ability='str')
sk3 = Skill(name='intimidation',ability='cha')
sk4 = Skill(name='nature',ability='int')
sk5 = Skill(name='perception',ability='wis')
sk6 = Skill(name='survival',ability='wis')
sk7 = Skill(name='history',ability='int')
sk8 = Skill(name='insight',ability='wis')
sk9 = Skill(name='medicine',ability='wis')
sk10 = Skill(name='persuasion',ability='cha')
sk11 = Skill(name='religion',ability='int')
sk12 = Skill(name='arcana',ability='int')
sk13 = Skill(name='acrobatics',ability='dex')
sk14 = Skill(name='stealth',ability='dex')
sk15 = Skill(name='investigation',ability='int')
sk16 = Skill(name='deception',ability='cha')
sk17 = Skill(name='performance',ability='cha')
sk18 = Skill(name='sleight of hand',ability='dex')

skills = [ sk1,sk2,sk3,sk4,sk5,sk6,sk7,sk8,sk9,sk10,sk11,sk12,sk13,sk14,sk15,sk16,sk17,sk18 ]

db.session.add_all(skills)
db.session.commit()