from app import app, db
from app.models import Spell, ClassSpecialty, Origin, EldritchInvocation

ei1 = EldritchInvocation(
	name = 'agonizing blast',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_spell = Spell.query.filter_by(name='eldritch blast').first().id,
	description = 'When you cast eldritch blast, add your Charisma modifier to the damage it deals on a hit.'
)
ei2 = EldritchInvocation(
	name = 'armor of shadows',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You can cast make armor on yourself at will, Without expending a spell slot or material components.'
)
ei3 = EldritchInvocation(
	name = 'ascendant step',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 9,
	description = 'You can cast levitate on yourself at will, without expending a spell slot or material components.'
)
ei4 = EldritchInvocation(
	name = 'beast speech',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You can cast speak with animals at will, without expending a spell slot.'
)
ei5 = EldritchInvocation(
	name = 'beguiling influence',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You gain proficiency in the Deception and Persuasion skills.'
)
ei6 = EldritchInvocation(
	name = 'bewitching whispers',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 7,
	description = 'You can cast compulsion once using a warlock spell slot. You can\'t do so again until you finish a long rest.'
)
ei7 = EldritchInvocation(
	name = 'book of ancient secrets',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_pact = 'pact of the tome',
	description = 'You can now inscribe magical rituals in your Book of Shadows. Choose two 1st-level spells that have the ritual tag from any class\'s spell list (the two needn\'t be from the same list). The spells appear in the book and don\'t count against the number of spells you know. With your Book of Shadows in hand, you can cast the chosen spells as rituals. You can\'t cast the spells except as rituals, unless you\'ve learned them by some other means. You can also cast a warlock spell you know as a ritual if it has the ritual tag. On your adventures, you can add other ritual spells to your Book of Shadows. When you find such a spell, you can add it to the book if the spell\'s level is equal to or less than half your warlock level (rounded up) and if you can spare the time to transcribe the spell. For each level of the spell, the transcription process takes 2 hours and costs 50 gp for the rare inks needed to inscribe it.'
)
ei8 = EldritchInvocation(
	name = 'chains of carceri',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 15,
	prerequisite_pact = 'pact of the chain',
	description = 'You can cast hold monster at will–targeting a celestial, fiend, or elemental–without expending a spell slot or material components. You must finish a long rest before you can use this invocation on the same creature again.'
)
ei9 = EldritchInvocation(
	name = 'devil\'s sight',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet.'
)
ei10 = EldritchInvocation(
	name = 'dreadful word',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 7,
	description = 'You can cast confusion once using a warlock spell slot. You can\'t do so again until you finish a long rest.'
)
ei11 = EldritchInvocation(
	name = 'eldritch sight',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You can cast detect magic at will, without expending a spell slot.'
)
ei12 = EldritchInvocation(
	name = 'eldritch spear',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_spell = Spell.query.filter_by(name='eldritch blast').first().id,
	description = 'When you cast eldritch blast, its range is 300 feet.'
)
ei13 = EldritchInvocation(
	name = 'eyes of the rune keeper',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You can read all writing.'
)
ei14 = EldritchInvocation(
	name = 'fiendish vigor',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You can cast false life on yourself at will as a 1st-level spell, without expending a spell slot or material components.'
)
ei15 = EldritchInvocation(
	name = 'gaze of two minds',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You can use your action to touch a willing humanoid and perceive through its senses until the end of your next turn. As long as the creature is on the same plane of existence as you, you can use your action on subsequent turns to maintain this connection, extending the duration until the end of your next turn. While perceiving through the other creature\'s senses, you benefit from any special senses possessed by that creature, and you are blinded and deafened to your own surroundings.'
)
ei16 = EldritchInvocation(
	name = 'lifedrinker',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 12,
	prerequisite_pact = 'pact of the blade',
	description = 'When you hit a creature with your Pact weapon, the creature takes extra necrotic damage equal to your Charisma modifier (minimum 1).'
)
ei17 = EldritchInvocation(
	name = 'mask of many faces',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You can cast disguise self at will, without expending a spell slot.'
)
ei18 = EldritchInvocation(
	name = 'master of myriad forms',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 15,
	description = 'You can cast alter self at will, without expending a spell slot.'
)
ei19 = EldritchInvocation(
	name = 'minions of chaos',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 9,
	description = 'You can cast conjure elemental once using a warlock spell slot. You can\'t do so again until you finish a long rest.'
)
ei20 = EldritchInvocation(
	name = 'mire the mind',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 5,
	description = 'You Can cast slow once using a warlock spell slot. You can\'t do so again until you finish a long rest.'
)
ei21 = EldritchInvocation(
	name = 'misty visions',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You can cast silent image at will, without expending a spell slot or material components.'
)
ei22 = EldritchInvocation(
	name = 'one with shadows',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 5,
	description = 'When you are in an area Of dim light or darkness, you Can use your action to become invisible until you move or take an action or a reaction.'
)
ei23 = EldritchInvocation(
	name = 'otherworldly leap',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 9,
	description = 'You can cast jump on yourself at will, without expending a spell slot or material components.'
)
ei24 = EldritchInvocation(
	name = 'repelling blast',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_spell = Spell.query.filter_by(name='eldritch blast').first().id,
	description = 'When you hit a creature with eldritch blast, you can push the creature up to 10 feet away from you in a straight line.'
)
ei25 = EldritchInvocation(
	name = 'sculptor of flesh',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 7,
	description = 'You can cast polymorph once using a warlock spell slot. You can\'t do so again until you finish a long rest.'
)
ei26 = EldritchInvocation(
	name = 'sign of ill omen',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 5,
	description = 'You can cast bestow curse once using a warlock spell slot. You can\'t do so again until you finish a long rest.'
)
ei27 = EldritchInvocation(
	name = 'thief of five fates',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	description = 'You can cast bane once using a warlock spell slot. You can\'t do so again until you finish a long rest.'
)
ei28 = EldritchInvocation(
	name = 'thirsting blade',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 5,
	prerequisite_pact = 'pact of the blade',
	description = 'You can attack with your pact weapon twice, instead of once, whenever you take the Attack action on your turn.'
)
ei29 = EldritchInvocation(
	name = 'visions of distant realms',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 15,
	description = 'You can cast arcane eye at will, without expending a spell slot.'
)
ei30 = EldritchInvocation(
	name = 'voice of the chain master',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_pact = 'pact of the chain',
	description = 'You can communicate telepathically with your familiar and perceive through your familiar\'s senses as long as you are on the same plane of existence. Additionally, while perceiving through your familiar\'s senses, you can speak through your familiar in your own voice, even if your familiar is normally incapable of speech.'
)
ei31 = EldritchInvocation(
	name = 'whispers of the grave',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 9,
	description = 'You can cast speak with dead at will, without expending a spell slot.'
)
ei32 = EldritchInvocation(
	name = 'witch sight',
	origin_id = Origin.query.filter_by(name='Player\'s Hand Book').first().id,
	prerequisite_level = 15,
	description = 'You can see the true form of any shapechanger or creature concealed by illusion or transmutation magic while the creature is within 30 feet Of you and within line of sight.'
)

invocations = [
	ei1,ei2,ei3,ei4,ei5,ei6,ei7,ei8,ei9,ei10,
	ei11,ei12,ei13,ei14,ei15,ei16,ei17,ei18,ei19,ei20,
	ei21,ei22,ei23,ei24,ei25,ei26,ei27,ei28,ei29,ei30,
	ei30,ei31,ei32
]

db.session.add_all(invocations)
db.session.commit()