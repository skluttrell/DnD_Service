from app import app, db
from app.models import BreathWeapon, Race

race = Race.query.filter_by(name='dragonborn').first().id
bw1 = BreathWeapon(race_id=race,dragon='black',damage_type='acid',breath_weapon='5 by 30 ft. line',save='dex')
bw2 = BreathWeapon(race_id=race,dragon='blue',damage_type='lightning',breath_weapon='5 by 30 ft. line',save='dex')
bw3 = BreathWeapon(race_id=race,dragon='brass',damage_type='fire',breath_weapon='5 by 30 ft. line',save='dex')
bw4 = BreathWeapon(race_id=race,dragon='bronze',damage_type='lightning',breath_weapon='5 by 30 ft. line',save='dex')
bw5 = BreathWeapon(race_id=race,dragon='copper',damage_type='acid',breath_weapon='5 by 30 ft. line',save='dex')
bw6 = BreathWeapon(race_id=race,dragon='gold',damage_type='fire',breath_weapon='15 ft. cone',save='dex')
bw7 = BreathWeapon(race_id=race,dragon='green',damage_type='poison',breath_weapon='15 ft. cone',save='con')
bw8 = BreathWeapon(race_id=race,dragon='red',damage_type='fire',breath_weapon='15 ft. cone',save='dex')
bw9 = BreathWeapon(race_id=race,dragon='silver',damage_type='cold',breath_weapon='15 ft. cone',save='con')
bw10 = BreathWeapon(race_id=race,dragon='white',damage_type='cold',breath_weapon='15 ft. cone',save='con')

breath_weapons = [ bw1,bw2,bw3,bw4,bw5,bw6,bw7,bw8,bw9,bw10 ]

db.session.add_all(breath_weapons)
db.session.commit()