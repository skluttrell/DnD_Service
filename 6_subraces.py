from app import app, db
from app.models import Subrace, Feature

sr1 = Subrace(
	name='hill dwarf',
	description = 'As a hill dwarf, you have keen senses, deep intuition, and remarkable resilience. The gold dwarves of Faer&#251;n in their mighty southern kingdom are hill dwarves, as are the exiled Neidar and the debased Klar of Krynn in the Dragonlance setting.',
	subrace_features = [
		Feature.query.filter_by(code='rf7dwf7hd1').first(),
		Feature.query.filter_by(code='rf8dwf8hd2').first()
	]
)
sr2 = Subrace(
	name='mountain dwarf',
	description = 'As a mountain dwarf, you\'re strong and hardy, accustomed to a difficult life in rugged terrain. You\'re probably on the tall side (for a dwarf), and tend toward lighter coloration. The shield dwarves of northern Faer&#251;n, as well as the ruling Hylar clan and the noble Daewar clan Of Dragonlance, are mountain dwarves.',
	subrace_features = [
		Feature.query.filter_by(code='rf9dwf9md1').first(),
		Feature.query.filter_by(code='rf10dwf10md2').first()
	]
)
sr3 = Subrace(
	name='high elf',
	description = 'As a high elf, you have a keen mind and a mastery of at least the basics of magic.\nIn many of the worlds of D&#38;D, there are two kinds of high elves. One type (which includes the gray elves and valley elves of Greyhawk, the Silvanesti of Dragonlance, and the sun elves of the Forgotten Realms) is haughty and reclusive, believing themselves to be superior to non-elves and even other elves.\nThe other type (including the high elves Of Greyhawk, the Qualinesti of Dragonlance, and the moon elves of the Forgotten Realms) are more common and more friendly, and often encountered among humans and other races.\nThe sun elves of Faerün (also called gold elves or sunrise elves) have bronze skin and hair of copper, black, or golden blond. Their eyes are golden, silver, or black. Moon elves (also called silver elves or gray elves) are much paler, with alabaster skin sometimes tinged with blue. They often have hair of silver-white, black, or blue, but various shades of blond, brown, and red are not uncommon. Their eyes are blue or green and flecked with gold.',
	subrace_features = [
		Feature.query.filter_by(code='rf16elf6he1').first(),
		Feature.query.filter_by(code='rf17elf7he2').first(),
		Feature.query.filter_by(code='rf18elf8he3').first(),
		Feature.query.filter_by(code='rf19elf9he4').first()
	]
)
sr4 = Subrace(
	name='wood elf',
	description = 'As a wood elf, you have keen senses and intuition, and your fleet feet carry you quickly and stealthily through your native forests. This category includes the wild elves (grugach) of Greyhawk and the Kagonesti of Dragonlance, as well as the races called wood elves in Greyhawk and the Forgotten Realms. In Faer&#251;n, wood elves (also called wild elves, green elves, or forest elves) are reclusive and distrusting of non-elves.\nWood elves\' skin tends to be copperish in hue, sometimes with traces of green. Their hair tends toward browns and blacks, but it is occasionally blond or copper-colored. Their eyes are green, brown, or hazel.',
	subrace_features = [
		Feature.query.filter_by(code='rf20elf10we1').first(),
		Feature.query.filter_by(code='rf21elf11we2').first(),
		Feature.query.filter_by(code='rf22elf12we3').first(),
	]
)
sr5 = Subrace(
	name='dark elf (drow)',
	description = 'Descended from an earlier subrace of elves, the drow were banished from the surface world for following the goddess Lolth down the path of evil. Now they have built their own civilization in the depths of the Underdark, patterned after the Way of Lolth.\nAlso called dark elves, the drow have skin that resembles charcoal or obsidian, as well as stark white or pale yellow hair. They commonly have very pale eyes (so pale as to be mistaken for white) in shades of lilac, silver, pink, red, and blue.\nThey tend to be smaller and thinner than most elves.\n[h]the darkness of the drow[/h]Were it not for one renowned exception, the race of drow would be universally reviled. To most, they are a race of demon-worshiping marauders dwelling in the subterranean depths of the Underdark, emerging only on the blackest nights to pillage and slaughter the surface dwellers they despise. Their society is depraved and preoccupied with the favor of Lolth, their spider-goddess, who sanctions murder and the extermination of entire families as noble houses vie for position.\nYet one drow, at least, broke the mold. In the world of the Forgotten Realms, Drizzt Do\'Urden, ranger of the North, has proven his quality as a good-hearted defender of the weak and innocent. Rejecting his heritage and adrift in a world that looks upon him with terror and loathing, Drizzt is a model for those few drow who follow in his footsteps, trying to find a life apart from the evil society of their Underdark homes.\nDrow grow up believing that other surface-dwelling races are inferior, worthless&#8211;except as slaves. Drow who develop a conscience or find it necessary to cooperate with members of other races find it hard to overcome that prejudice, especially when they are so Often on the receiving end of hatred.\nDrow adventurers are rare. Check with your Dungeon Master to see if you can play one.',
	subrace_features = [
		Feature.query.filter_by(code='rf23elf13de1').first(),
		Feature.query.filter_by(code='rf24elf14de2').first(),
		Feature.query.filter_by(code='rf25elf15de3').first(),
		Feature.query.filter_by(code='rf26elf16de4').first(),
		Feature.query.filter_by(code='rf27elf17de5').first()
	]
)
sr6 = Subrace(
	name='lightfoot',
	description = 'As a lightfoot halfling, you can easily hide from notice, even using other people as cover. You\'re inclined to be affable and get along well with others. In the Forgotten Realms, lightfoot halflings have spread the farthest and thus are the most common variety.\nLightfoots are more prone to wanderlust than other halflings, and often dwell a long side other races or take up a nomadic life. In the world of Greyhawk, these halflings are called hairfeet or tallfellows.',
	subrace_features = [
		Feature.query.filter_by(code='rf32hlg5lf1').first(),
		Feature.query.filter_by(code='rf33hlg6lf2').first()
	]
)
sr7 = Subrace(
	name='stout',
	description = 'As a stout halfling, you\'re hardier than average and have some resistance to poison. Some say that stouts have dwarven blood. In the Forgotten Realms, these halflings are called stronghearts, and they\'re most common in the south.',
	subrace_features = [
		Feature.query.filter_by(code='rf34hlg7st1').first(),
		Feature.query.filter_by(code='rf35hlg8st2').first()
	]
)
sr8 = Subrace(
	name='forest gnome',
	description = 'As a forest gnome, you have a natural knack for illusion and inherent quickness and stealth. In the worlds Of D&#38;D, forest gnomes are rare and secretive. They gather in hidden communities in sylvan forests, using illusions and trickery to conceal themselves from threats or to mask their escape should they be detected. Forest gnomes tend to be friendly with other good-spirited woodland folk, and they regard elves and good fey as their most important allies. These gnomes befriend small forest animals and rely on them for information about threats that might prowl their lands.',
	subrace_features = [
		Feature.query.filter_by(code='rf44gnm4fg1').first(),
		Feature.query.filter_by(code='rf45gnm5fg2').first(),
		Feature.query.filter_by(code='rf46gnm6fg3').first()
	]
)
sr9 = Subrace(
	name='rock gnome',
	description = 'As a rock gnome, you have a natural inventiveness and hardiness beyond that of other gnomes. Most gnomes in the worlds of D&#38;D are rock gnomes, including the tinker gnomes of the Dragonlance setting.',
	subrace_features = [
		Feature.query.filter_by(code='rf47gnm7rg1').first(),
		Feature.query.filter_by(code='rf48gnm8rg2').first(),
		Feature.query.filter_by(code='rf49gnm9rg3').first()
	]
)
sr10 = Subrace(
	name='deep gnome',
	description = 'A third subrace of gnomes, the deep gnomes (or svirfneblin), live in small communities scattered in the Underdark. Unlike the duergar and the drow, svirfneblin are as good as their surface cousins. However, their humor and enthusiasm are dampened by their oppressive environment, and their inventive expertise is directed mostly toward stonework.'
)

subraces = [ sr1,sr2,sr3,sr4,sr5,sr6,sr7,sr8,sr9,sr10 ]

db.session.add_all(subraces)
db.session.commit()