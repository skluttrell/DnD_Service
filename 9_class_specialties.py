from app import app, db
from app.models import ClassSpecialty, DiscreetLevelFeatures, Feature

cs1 = ClassSpecialty(
	name='path of the berserker',
	description = 'For some barbarians, rage is a means to an end&#8211;that end being violence. The Path of the Berserker is a path of untrammeled fury, slick with blood. As you enter the berserker\'s rage, you thrill in the chaos of battle, heedless of your own health or well-being.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf20bar20pb1').first(),
		Feature.query.filter_by(code='cf21bar21pb2').first(),
		Feature.query.filter_by(code='cf22bar22pb3').first(),
		Feature.query.filter_by(code='cf23bar23pb4').first()
	]
)
cs2 = ClassSpecialty(
name='path of the totem warrior',
	description = 'The Path of the Totem Warrior is a spiritual journey, as the barbarian accepts a spirit animal as guide, protector, and inspiration. In battle, your totem spirit fills you with supernatural might, adding magical fuel to your barbarian rage.\nMost barbarian tribes consider a totem animal to be kin to a particular clan. In such cases, it is unusual for an individual to have more than one totem animal spirit, though exceptions exist.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf24bar24pt1').first(),
		Feature.query.filter_by(code='cf25bar25pt2').first(),
		Feature.query.filter_by(code='cf26bar26pt3').first(),
		Feature.query.filter_by(code='cf27bar27pt4').first(),
		Feature.query.filter_by(code='cf28bar28pt5').first()
	]
)
cs3 = ClassSpecialty(
	name='college of lore',
	description = '',
	class_specialty_features = [
		Feature.query.filter_by(code='cf46brd18cl1').first(),
		Feature.query.filter_by(code='cf47brd19cl2').first(),
		Feature.query.filter_by(code='cf48brd20cl3').first(),
		Feature.query.filter_by(code='cf49brd21cl4').first()
	]
)
cs4 = ClassSpecialty(
	name='college of valor',
	description = 'Bards of the College of Valor are daring skalds whose tales keep alive the memory of the great heroes of the past, and thereby inspire a new generation of heroes. These bards gather in mead halls or around great bonfires to sing the deeds of the mighty, both past and present. They travel the land to witness great events firsthand and to ensure that the memory of those events doesn\'t pass from the world. With their songs, they inspire others to reach the same heights of accomplishments as the heroes of Old.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf50brd22cv1').first(),
		Feature.query.filter_by(code='cf51brd23cv2').first(),
		Feature.query.filter_by(code='cf52brd24cv3').first(),
		Feature.query.filter_by(code='cf53brd25cv4').first()
	]
)
cs5 = ClassSpecialty(
	name='knowledge domain',
	description = 'The gods of knowledge&#8211;including Oghma, Boccob, Gilean, Aureon, and Thoth&#8211;value learning and understanding above all. Some teach that knowledge is to be gathered and shared in libraries and universities, or promote the practical knowledge of craft and invention. Some deities hoard knowledge and keep its secrets to themselves. And some promise their followers that they will gain tremendous power if they unlock the secrets of the multiverse. Followers of these gods study esoteric lore, collect old tomes, delve into the secret places of the earth, and learn all they can. Some gods of knowledge promote the practical knowledge of craft and invention, including smith deities like Gond, Reorx, Onatar, Moradin, Hephaestus, and Goibhniu.]n],[tc]knowledge domain spells[/tc][th]cleric level[/th/]spells[/th][tr]1st[/td/]command, identify[/tr][tr]3rd[/td/]augury, suggestion[/tr][tr]5th[/td/]nondetection, speak with dead[/tr][tr]7th[/td/]arcane eye, confusion[/tr][tr]9th[/td/]legend lore, scrying[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf67clc14kd1').first(),
		Feature.query.filter_by(code='cf68clc15kd2').first(),
		Feature.query.filter_by(code='cf69clc16kd3').first(),
		Feature.query.filter_by(code='cf70clc17kd4').first(),
		Feature.query.filter_by(code='cf71clc18kd5').first()
	]
)
cs6 = ClassSpecialty(
	name='life domain',
	description = 'The Life domain focuses on the vibrant positive energy&#8211;one of the fundamental forces of the universe&#8211;that sustains all life. The gods of life promote vitality and health through healing the sick and wounded, caring for those in need, and driving away the forces of death and undeath. Almost any non-evil deity can claim influence over this domain, particularly agricultural deities (such as Chauntea, Arawai, and Demeter), sun gods (such as Lathander, Pelor, and Re-Horakhty), gods of healing or endurance (such as Ilmater, Mishakal, Apollo, and Diancecht), and gods of home and community (such as Hestia, Hathor, and Boldrei).\n[tc]life domain spells[/tc][th]cleric level[/th/]spells[/th][tr]1st[/td/]bless, cure wounds[/tr][tr]3rd[/td/]lesser restoration, spiritual weapon[/tr][tr]5th[/td/]beacon of hope, revivify[/tr][tr]7th[/td/]death ward, guardian of faith[/tr][tr]9th[/td/]mass cure wounds, raise dead[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf72clc19lf1').first(),
		Feature.query.filter_by(code='cf73clc20lf2').first(),
		Feature.query.filter_by(code='cf74clc21lf3').first(),
		Feature.query.filter_by(code='cf75clc22lf4').first(),
		Feature.query.filter_by(code='cf76clc23lf5').first(),
		Feature.query.filter_by(code='cf77clc24lf6').first()
	]
)
cs7 = ClassSpecialty(
	name = 'light domain',
	description = 'Gods of light&#8211;including Helm, Lathander, Pholtus, Branchala, the Silver Flame, Belenus, Apollo, and Re-Horakhty&#8211;promote the ideals of rebirth and renewal, truth, vigilance, and beauty, often using the symbol of the sun. Some of these gods are portrayed as the sun itself or as a charioteer who guides the sun across the sky. Others are tireless sentinels whose eyes pierce every shadow and see through every deception. Some are deities Of beauty and artistry, who teach that art is a vehicle for the soul\'s improvement. Clerics of a god of light are enlightened souls infused with radiance and the power of their gods\' discerning vision, charged with chasing away lies and burning away darkness.\n[tc]light domain spells[/tc[th]cleric level[/th/]spells[/th][tr]1st[/td/]burning hands, faerie fire[/tr][tr]3rd[/td/]flaming sphere, scorching ray[/tr][tr]5th[/td/]daylight, fireball[/tr][tr]7th[/td/]guardian of faith, wall of fire[/tr][tr]9th[/td/]flame strike, scrying[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf78clc25lt1').first(),
		Feature.query.filter_by(code='cf79clc26lt2').first(),
		Feature.query.filter_by(code='cf80clc27lt3').first(),
		Feature.query.filter_by(code='cf81clc28lt4').first(),
		Feature.query.filter_by(code='cf82clc29lt5').first(),
		Feature.query.filter_by(code='cf83clc30lt6').first()
	]
)
cs8 = ClassSpecialty(
	name = 'nature domain',
	description = 'Gods of nature are as varied as the natural world itself. From inscrutable gods of the deep forests (such as Silvanus, Obad-Hai, Chislev, Balinor, and Pan) to deities associated with particular springs and groves (such as Eldath). Druids revere nature as a whole and might serve one of these deities, practicing mysterious rites and reciting all-but-forgotten prayers in their own secret tongue. But many of these gods have clerics as well, champions who take a more active role in advancing the interests of a particular nature god. These clerics might hunt the evil monstrosities that despoil the woodlands, bless the harvest of the faithful, or wither the crops of those who anger their gods.\n[tc]nature domain spells[/tc][th]cleric level[/th/]spells[/th][tr]1st[/td/]animalfriendship, speak with animals[/tr][tr]3rd[/td/]barkskin, spike growth[/tr][tr]5th[/td/]plant growth, wind wall[/tr][tr]7th[/td/]dominate beast, grasping vine[/tr][tr]9th[/td/]insect plague, tree stride[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf84clc31nd1').first(),
		Feature.query.filter_by(code='cf85clc32nd2').first(),
		Feature.query.filter_by(code='cf86clc33nd3').first(),
		Feature.query.filter_by(code='cf87clc34nd4').first(),
		Feature.query.filter_by(code='cf88clc35nd5').first(),
		Feature.query.filter_by(code='cf89clc36nd6').first()
	]
)
cs9 = ClassSpecialty(
	name = 'tempest domain',
	description = 'Gods whose portfolios include the Tempest domain&#8211; including Talos, Umberlee, Kord, Zeboim, the Devourer, Zeus, and Thor&#8211;govern Storms, sea, and sky. They include gods of lightning and thunder, gods of earthquakes, some fire gods, and certain gods of violence, physical strength, and courage. In some pantheons, a god of this domain rules over other deities and is known for swift justice delivered by thunderbolts. In the pantheons of seafaring people, gods of this domain are ocean deities and the patrons of sailors. Tempest gods send their clerics to inspire fear in the common folk, either to keep those folk on the path of righteousness or to encourage them to offer sacrifices of propitiation to ward off divine wrath.\n[tc]tempest domain spells[/tc][th]cleric level[/th/]spells[/heading]th[tr]1st[/tr/]fog cloud, thunderwave[/tr][tr]3rd[/td/]gust of wind, shatter[/tr][tr]5th[/td/]call lightning, sleet storm[/tr][tr]7th[/td/]control water, ice storm[/tr][tr]9th[/td/]destructive wave, insect plague[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf90clc37td1').first(),
		Feature.query.filter_by(code='cf91clc38td2').first(),
		Feature.query.filter_by(code='cf92clc39td3').first(),
		Feature.query.filter_by(code='cf93clc40td4').first(),
		Feature.query.filter_by(code='cf94clc41td5').first(),
		Feature.query.filter_by(code='cf95clc42td6').first()
	]
)
cs10 = ClassSpecialty(
	name = 'trickery domain',
	description = 'Gods of trickery&#8211;such as Tymora, Beshaba, Olidammara, the Traveler, Garl Glitter-gold, and Loki&#8211;are mischief-makers and instigators who stand as a constant challenge to the accepted order among both gods and mortals. They\'re patrons of thieves, scoundrels, gamblers, rebels, and liberators. Their clerics are a disruptive force in the world, puncturing pride, mocking tyrants, stealing from the rich, freeing captives, and flouting hollow traditions. They prefer subterfuge, pranks, deception, and theft rather than direct confrontation.\n[tc]trickery domain spells[/tc][th]cleric level[/th/]spells[/th][tr]1st[/td/]charm person, disguise self[/tr][tr]3rd[/td/]mirror image, pass without trace[/tr][tr]5th[/td/]blink, dispel magic[/tr][tr]7th[/td/]dimension door, polymorph[/tr][tr]9th[/td/]dominate person, modify memory[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf96clc43tr1').first(),
		Feature.query.filter_by(code='cf97clc44tr2').first(),
		Feature.query.filter_by(code='cf98clc45tr3').first(),
		Feature.query.filter_by(code='cf99clc46tr4').first(),
		Feature.query.filter_by(code='cf100clc47tr5').first()
	]
)
cs11 = ClassSpecialty(
	name = 'war domain',
	description = 'War has many manifestations. It can make heroes of ordinary people. It can be desperate and horrific, with acts of cruelty and cowardice eclipsing instances of excellence and courage. In either case, the gods of war watch over warriors and reward them for their great deeds. The clerics of such gods excel in battle, inspiring others to fight the good fight or offering acts of violence as prayers. Gods of war include champions of honor and chivalry (such as Torm, Heironeous, and Kiri-Jolith) as well as gods of destruction and pillage (such as Erythnul, the Fury, Gruumsh, and Ares) and gods of conquest and domination (such as Bane, Hextor, and Maglubiyet). Other war gods (such as Tempus, Nike, and Nuada) take a more neutral stance, promoting war in all its manifestations and supporting warriors in any circumstance.\n[tc]war domain spells[/tc][th]cleric level[/th/]spells[/th][tr]1st[/td/]divinefavor, shield of faith[/tr][tr]3rd[/td/]magic weapon, spiritual weapon[/tr][tr]5th[/td/]crusader\'s mantle, spirit guardians[/tr][tr]7th[/td/]freedom of movement, stoneskin[/tr][tr]9th[/td/]flame strike, hold monster[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf101clc48wd1').first(),
		Feature.query.filter_by(code='cf102clc49wd2').first(),
		Feature.query.filter_by(code='cf103clc50wd3').first(),
		Feature.query.filter_by(code='cf104clc51wd4').first(),
		Feature.query.filter_by(code='cf105clc52wd5').first(),
		Feature.query.filter_by(code='cf106clc53wd6').first()
	]
)
cs12 = ClassSpecialty(
	name = 'circle of the land',
	description = 'The Circle of the Land is made up of mystics and sages who safeguard ancient knowledge and rites through a vast oral tradition. These druids meet within sacred circles of trees or standing stones to whisper primal secrets in Druidic. The circle\'s wisest members preside as the chief priests of communities that hold to the Old Faith and serve as advisors to the rulers of those folk. As a member of this circle, your magic is influenced by the land where you were initiated into the circle\'s mysterious rites.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf121dru15cl1').first(),
		Feature.query.filter_by(code='cf122dru16cl2').first(),
		Feature.query.filter_by(code='cf123dru17cl3').first(),
		Feature.query.filter_by(code='cf124dru18cl4').first(),
		Feature.query.filter_by(code='cf125dru19cl5').first(),
		Feature.query.filter_by(code='cf126dru20cl6').first()
	]
)
cs13 = ClassSpecialty(
	name = 'circle of the moon',
	description = 'Druids of the Circle of the Moon are fierce guardians of the wilds. Their order gathers under the full moon to share news and trade warnings. They haunt the deepest parts of the wilderness, where they might go for weeks on end before crossing paths with another humanoid creature, let alone another druid.\nChangeable as the moon, a druid of this circle might prowl as a great cat one night, soar over the treetops as an eagle the next day, and crash through the undergrowth in bear form to drive off a trespassing monster. The wild is in the druid\'s blood.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf127dru21cm1').first(),
		Feature.query.filter_by(code='cf128dru22cm2').first(),
		Feature.query.filter_by(code='cf129dru23cm3').first(),
		Feature.query.filter_by(code='cf130dru24cm4').first(),
		Feature.query.filter_by(code='cf131dru25cm5').first()
	]
)
cs14 = ClassSpecialty(
	name = 'champion',
	description = 'The archetypal Champion focuses on the development of raw physical power honed to deadly perfection. Those who model themselves on this archetype combine rigorous training with physical excellence to deal devastating blows.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf144fht13ch1').first(),
		Feature.query.filter_by(code='cf145fht14ch2').first(),
		Feature.query.filter_by(code='cf146fht15ch3').first(),
		Feature.query.filter_by(code='cf147fht16ch4').first(),
		Feature.query.filter_by(code='cf148fht17ch5').first()
	]
)
cs15 = ClassSpecialty(
	name = 'battle master',
	description = 'Those who emulate the archetypal Battle Master employ martial techniques passed down through generations. To a Battle Master, combat is an academic field, sometimes including subjects beyond battle such as weaponsmithing and calligraphy. Not every fighter absorbs the lessons of history, theory, and artistry that are reflected in the Battle Master archetype, but those who do are well-rounded fighters of great skill and knowledge.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf149fht18bm1').first(),
		Feature.query.filter_by(code='cf150fht19bm2').first(),
		Feature.query.filter_by(code='cf151fht20bm3').first(),
		Feature.query.filter_by(code='cf152fht21bm4').first(),
		Feature.query.filter_by(code='cf153fht22bm5').first()
	]
)
cs16 = ClassSpecialty(
	name = 'eldritch knight',
	description = 'The archetypal Eldritch Knight combines the martial mastery common to all fighters with a careful study Of magic. Eldritch Knights use magical techniques similar to those practiced by wizards. They focus their Study on two of the eight schools of magic: abjuration and evocation. Abjuration spells grant an Eldritch Knight additional protection in battle, and evocation spells deal damage to many foes at once, extending the fighter\'s reach in combat. These knights learn a comparatively small number of spells, committing them to memory instead of keeping them in a spellbook.',
	discreet_level_features = [
		DiscreetLevelFeatures.query.filter_by(code='ek1').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek2').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek3').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek4').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek5').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek6').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek7').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek8').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek9').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek10').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek11').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek12').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek13').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek14').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek15').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek16').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek17').first(),
		DiscreetLevelFeatures.query.filter_by(code='ek18').first()
],
	class_specialty_features = [
		Feature.query.filter_by(code='cf154fht23ek1').first(),
		Feature.query.filter_by(code='cf155fht24ek2').first(),
		Feature.query.filter_by(code='cf156fht25ek3').first(),
		Feature.query.filter_by(code='cf157fht26ek4').first(),
		Feature.query.filter_by(code='cf158fht27ek5').first(),
		Feature.query.filter_by(code='cf159fht28ek6').first()
	]
)
cs17 = ClassSpecialty(
	name = 'way of the open hand',
	description = 'Monks of the Way of the Open Hand are the ultimate masters of martial arts combat, whether armed or unarmed. They learn techniques to push and trip their opponents. manipulate ki to heal damage to their bodies, and practice advanced meditation that can protect them from harm.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf183mnk24wh1').first(),
		Feature.query.filter_by(code='cf184mnk25wh2').first(),
		Feature.query.filter_by(code='cf185mnk26wh3').first(),
		Feature.query.filter_by(code='cf186mnk27wh4').first()
	]
)
cs18 = ClassSpecialty(
	name = 'way of the shadow',
	description = 'Monks of the Way of Shadow follow a tradition that values stealth and subterfuge. These monks might be called ninjas or shadowdancers, and they serve as spies and assassins. Sometimes the members of a ninja monastery are family members, forming a clan sworn to secrecy about their arts and missions. Other monasteries are more like thieves\' guilds, hiring out their services to nobles, rich merchants, or anyone else who can pay their fees. Regardless of their methods, the heads of these monasteries expect the unquestioning obedience of their students.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf187mnk28ws1').first(),
		Feature.query.filter_by(code='cf188mnk29ws2').first(),
		Feature.query.filter_by(code='cf189mnk30ws3').first(),
		Feature.query.filter_by(code='cf190mnk31ws4').first()
	]
)
cs19 = ClassSpecialty(
	name='way of the four elements',
	description = 'You follow a monastic tradition that teaches you to harness the elements. When you focus your ki, you can align yourself with the forces of creation and bend the four elements to your will, using them as an extension of your body. Some members of this tradition dedicate themselves to a single element, but others weave the elements together. Many monks of this tradition tattoo their bodies with representations of their ki powers, commonly imagined as coiling dragons, but also as phoenixes, fish, plants, mountains, and cresting waves.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf191mnk32we1').first()
	]
)
cs20 = ClassSpecialty(
	name = 'oath of devotion',
	description = 'The Oath of Devotion binds a paladin to the loftiest ideals of justice, virtue, and order. Sometimes called cavaliers, white knights, or holy warriors, these paladins meet the ideal of the knight in shining armor, acting with honor in pursuit of justice and the greater good. They hold themselves to the highest standards of conduct, and some, for better or worse, hold the rest of the world to the same standards. Many who swear this oath are devoted to gods of law and good and use their gods\' tenets as the measure of their devotion. They hold angels&#8211;the perfect servants of good&#8211;as their ideals, and incorporate images of angelic wings into their helmets or coats of arms.\n[h]tenets of devotion[/h]Though the exact words and strictures of the Oath of Devotion vary, paladins Of this oath share these tenets.\nHonesty. Don\'t lie or cheat. Let your word be your promise.\nCourage. Never fear to act, though caution is wise.\nCompassion. Aid others, protect the weak, and punish those who threaten them. Show mercy to your foes, but temper it with wisdom.\nHonor. Treat others with fairness, and let your honorable deeds be an example to them. Do as much good as possible while causing the least amount of harm.\nDuty. Be responsible for your actions and their Consequences, protect those entrusted to your care, and obey those who have just authority over you.\n[h]oath spells[/h]You gain oath spells at the paladin levels listed.\n[tc]oath of devotion spells[/tc][th]paladin level[/th/]spells[/th][tr]3rd[/td/]protection from evil and good, sanctuary[/tr][tr]5th[/td/]lesser restoration, zone Of truth[/tr][tr]9th[/td/]beacon of hope, dispel magic[/tr][tr]13th[/td/]freedom of movement, guardian of faith[/tr][tr]17th[/td/]commune, flame strike[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf210pln19od1').first(),
		Feature.query.filter_by(code='cf211pln20od2').first(),
		Feature.query.filter_by(code='cf212pln21od3').first(),
		Feature.query.filter_by(code='cf213pln22od4').first()
	]
)
cs21 = ClassSpecialty(
name = 'oath of the ancients',
	description = 'The Oath of the Ancients is as old as the race of elves and the rituals of the druids. Sometimes called fey knights, green knights, or horned knights, paladins who swear this oath cast their lot with the side of the light in the cosmic struggle against darkness because they love the beautiful and life-giving things of the world, not necessarily because they believe in principles Of honor, courage, and justice. They adorn their armor and clothing With images of growing things&#8211;leaves, antlers or flowers&#8211;to reflect their commitment to preserving life and light in the world.\n[h]tenets of the ancients[/h]The tenets of the Oath of the Ancients have been preserved for uncounted centuries. This oath emphasizes the principles of good above any concerns of law or chaos. Its four central principles are simple.\nKindle the Light. Through your acts of mercy, kindness, and forgiveness, kindle the light of hope in the world, beating back despair.\nShelter the Light. Where there is good, beauty, love, and laughter in the world, stand against the wickedness that would swallow it. Where life flourishes, stand against the forces that would render it barren.\nPreserve Your Own Light. Delight in song and laughter, in beauty and art. If you allow the light to die in your own heart, you can\'t preserve it in the world.\nBe the Light. Be a glorious beacon for all who live in despair. Let the light of your joy and courage shine forth in all your deeds.\n[h]oath spells[/h]You gain oath spells at the paladin levels listed.\n[tc]oath of the ancients spells[/tc][th]paladin level[/th/]spells[/th][tr]3rd[/td/]ensnaring strike, speak with animals[/tr][tr]5th[/td/]misty step, moonbeam[/tr][tr]9th[/td/]plant growth, protection from energy[/tr][tr]13th[/td/]ice storm, stoneskin[/tr][tr]17th[/td/]commune with nature, tree stride[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf214pln23oa1').first(),
		Feature.query.filter_by(code='cf215pln24oa2').first(),
		Feature.query.filter_by(code='cf216pln25oa3').first(),
		Feature.query.filter_by(code='cf217pln26oa4').first()
	]
)
cs22 = ClassSpecialty(
	name = 'oath of vengeance',
	description = 'The Oath of Vengeance is a solemn commitment to punish those who have committed a grievous sin. When evil forces slaughter helpless villagers, when an entire people turns against the will of the gods, when a thieves\' guild grows too violent and powerful, when a dragon rampages through the countryside&#8211;at times like these, paladins arise and swear an Oath of Vengeance to set right that which has gone wrong. To these paladins&#8211;sometimes called avengers or dark knights&#8211;their own purity is not as important as delivering justice.\n[h]tenets of vengeance[/h]The tenets of the Oath of Vengeance vary by paladin, but all the tenets revolve around punishing wrongdoers by any means necessary. Paladins who uphold these tenets are willing to sacrifice even their own righteousness to mete out justice upon those who do evil, so the paladins are often neutral or lawful neutral in alignment. The core principles of the tenets are brutally simple.\nFight the Greater Evil. Faced with a choice of fighting my sworn foes or combating a lesser evil, I choose the greater evil.\nNo Mercy for the Wicked. Ordinary foes might win my mercy, but my sworn enemies do not.\nBy Any Means Necessary. My qualms can\'t get in the way of exterminating my foes.\nRestitution. If my foes wreak ruin on the world, it is because I failed to stop them. I must help those harmed by their misdeeds.\n[h]oath spells[/h]You gain oath spells at the paladin levels listed.\n[tc]oath of vengeance spells[/tc][th]paladin level[/th/]spells[/th][tr]3rd[/td/]bane, hunter\'s mark[/tr][tr]5th[/td/]hold person, misty step[/tr][tr]9th[/td/]haste, protection from energy[/tr][tr]13th[/td/]banishment, dimension door[/tr][tr]17th[/td/]hold monster, scrying[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf218pln27ov1').first(),
		Feature.query.filter_by(code='cf219pln28ov2').first(),
		Feature.query.filter_by(code='cf220pln29ov3').first(),
		Feature.query.filter_by(code='cf221pln30ov4').first()
	]
)
cs23 = ClassSpecialty(
	name = 'hunter',
	description = 'Emulating the Hunter archetype means accepting your place as a bulwark between civilization and the terrors of the wilderness. As you walk the Hunter\'s path, you learn specialized techniques for fighting the threats you face, from rampaging ogres and hordes of orcs to towering giants and terrifying dragons.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf240rgr19hr1').first(),
		Feature.query.filter_by(code='cf241rgr20hr2').first(),
		Feature.query.filter_by(code='cf242rgr21hr3').first(),
		Feature.query.filter_by(code='cf243rgr22hr4').first()
	]
)
cs24 = ClassSpecialty(
	name = 'beast master',
	description = 'The Beast Master archetype embodies a friendship between the civilized races and the beasts of the wild. United in focus, beast and ranger fight the monsters that threaten civilization and the wilderness alike.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf244rgr23bm1').first(),
		Feature.query.filter_by(code='cf245rgr24bm2').first(),
		Feature.query.filter_by(code='cf246rgr25bm3').first(),
		Feature.query.filter_by(code='cf247rgr26bm4').first()
	]
)
cs25 = ClassSpecialty(
	name = 'thief',
	description = 'You hone your skills in the larcenous arts. Burglars, bandits, cutpurses, and other criminals typically follow this archetype, but so do rogues who prefer to think of themselves as professional treasure seekers, explorers, delvers, and investigators. In addition to improving your agility and stealth, you learn skills useful for delving into ancient ruins, reading unfamiliar languages, and using magic items you normally couldn\'t employ.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf267rgu20th1').first(),
		Feature.query.filter_by(code='cf268rgu21th2').first(),
		Feature.query.filter_by(code='cf269rgu22th3').first(),
		Feature.query.filter_by(code='cf270rgu23th4').first(),
		Feature.query.filter_by(code='cf271rgu24th5').first()
	]
)
cs26 = ClassSpecialty(
	name = 'assassin',
	description = 'You focus your training on the grim art of death. Those who adhere to this archetype are diverse: hired killers, spies, bounty hunters, and even specially anointed priests trained to exterminate the enemies of their deity. Stealth, poison, and disguise help you eliminate your foes with deadly efficiency.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf272rgu25as1').first(),
		Feature.query.filter_by(code='cf273rgu26as2').first(),
		Feature.query.filter_by(code='cf274rgu27as3').first(),
		Feature.query.filter_by(code='cf275rgu28as4').first(),
		Feature.query.filter_by(code='cf276rgu29as5').first()
	]
)
cs27 = ClassSpecialty(
	name='arcane trickster',
	description = 'Some rogues enhance their fine-honed skills Of stealth and agility with magic, learning tricks of enchantment and illusion. These rogues include pickpockets and burglars, but also pranksters, mischief-makers, and a significant number of adventurers.',
	discreet_level_features = [
		DiscreetLevelFeatures.query.filter_by(code='at1').first(),
		DiscreetLevelFeatures.query.filter_by(code='at2').first(),
		DiscreetLevelFeatures.query.filter_by(code='at3').first(),
		DiscreetLevelFeatures.query.filter_by(code='at4').first(),
		DiscreetLevelFeatures.query.filter_by(code='at5').first(),
		DiscreetLevelFeatures.query.filter_by(code='at6').first(),
		DiscreetLevelFeatures.query.filter_by(code='at7').first(),
		DiscreetLevelFeatures.query.filter_by(code='at8').first(),
		DiscreetLevelFeatures.query.filter_by(code='at9').first(),
		DiscreetLevelFeatures.query.filter_by(code='at10').first(),
		DiscreetLevelFeatures.query.filter_by(code='at11').first(),
		DiscreetLevelFeatures.query.filter_by(code='at12').first(),
		DiscreetLevelFeatures.query.filter_by(code='at13').first(),
		DiscreetLevelFeatures.query.filter_by(code='at14').first(),
		DiscreetLevelFeatures.query.filter_by(code='at15').first(),
		DiscreetLevelFeatures.query.filter_by(code='at16').first(),
		DiscreetLevelFeatures.query.filter_by(code='at17').first(),
		DiscreetLevelFeatures.query.filter_by(code='at18').first()
	],
	class_specialty_features = [
		Feature.query.filter_by(code='cf277rgu30at1').first(),
		Feature.query.filter_by(code='cf278rgu31at2').first(),
		Feature.query.filter_by(code='cf279rgu32at3').first(),
		Feature.query.filter_by(code='cf280rgu33at4').first(),
		Feature.query.filter_by(code='cf281rgu34at5').first()
	]
)
cs28 = ClassSpecialty(
	name = 'draconic bloodline',
	description = 'Your innate magic comes from draconic magic that was mingled with your blood or that of your ancestors. Most often, sorcerers with this origin trace their descent back to a mighty sorcerer of ancient times who made a bargain with a dragon or who might even have claimed a dragon parent. Some of these bloodlines are well established in the world, but most are obscure. Any given sorcerer could be the first of a new bloodline, as a result of a pact or some other exceptional circumstance.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf292scr11da1').first(),
		Feature.query.filter_by(code='cf293scr12da2').first(),
		Feature.query.filter_by(code='cf294scr13da3').first(),
		Feature.query.filter_by(code='cf295scr14da4').first(),
		Feature.query.filter_by(code='cf296scr15da5').first()
	]
)
cs29 = ClassSpecialty(
	name = 'wild magic',
	description = 'Your innate magic comes from the forces of chaos that underlie the order of creation. You might have endured exposure to raw magic, perhaps through a planar portal leading to Limbo, the Elemental Planes, or the Far Realm. Perhaps you were blessed by a fey being or marked by a demon. Or your magic could be a fluke of your birth, with no apparent cause. However it came to be, this magic churns within you, waiting for any outlet.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf297scr16wm1').first(),
		Feature.query.filter_by(code='cf298scr17wm2').first(),
		Feature.query.filter_by(code='cf299scr18wm3').first(),
		Feature.query.filter_by(code='cf300scr19wm4').first(),
		Feature.query.filter_by(code='cf301scr20wm5').first()
	]
)
cs30 = ClassSpecialty(
	name = 'the archfey',
	description = 'Your patron is a lord or lady of the fey, a creature of legend who holds secrets that were forgotten before the mortal races were born. This being\'s motivations are often inscrutable, and sometimes whimsical, and might involve a striving for greater magical power or the settling of age-old grudges. Beings of this sort include the Prince of Frost; the Queen of Air and Darkness, ruler of the Gloaming Court; Titania of the Summer Court; her consort Oberon, the Green Lord; Hyrsam, the Prince of Fools, and ancient hags.[h]expanded spell list[/h]The Archfey lets you choose from an expanded list Of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you.\n[tc]archfey expanded spells[/tc][th]spell level[/th/]spells[/th][tr]1st[/td/]faerie fire, sleep[/tr][tr]2nd[/td/]calm emotions, phantasmal force[/tr][tr]3rd[/td/]blink, plant growth[/tr][tr]4th[/td/]dominate beast, greater invisibility[/tr][tr]5th[/td/]dominate person, seeming[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf314war13af1').first(),
		Feature.query.filter_by(code='cf315war14af2').first(),
		Feature.query.filter_by(code='cf316war15af3').first(),
		Feature.query.filter_by(code='cf317war16af4').first()
	]
)
cs31 = ClassSpecialty(
	name = 'the fiend',
	description = 'You have made a pact with a fiend from the lower planes of existence, a being whose aims are evil, even if you strive against those aims. Such beings desire the corruption or destruction of all things, ultimately including you. Fiends powerful enough to forge a pact include demon lords such as Demogorgon, Orcus, Fraz\'Urb-luu, and Baphomet; archdevils such as Asmodeus, Dispater, Mephistopheles, and Belial; pit fiends and balors that are especially mighty; and ultroloths and other lords of the yugoloths.\n[h]expanded spell list[/h]The Fiend lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you.\n[tc]fiend expanded spells[/tc][th]spell level[/th/]spells[/th][tr]1st[/td/]burning hands, command[/tr][tr]2nd[/td/]blindness/deafness, scorching ray[/tr][tr]3rd[/td/]fireball, stinking cloud[/tr][tr]4th[/td/]fire shield, wall of fire[/tr][tr]5th[/td/]flame strike, hallow[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf318war17tf1').first(),
		Feature.query.filter_by(code='cf319war18tf2').first(),
		Feature.query.filter_by(code='cf320war19tf3').first(),
		Feature.query.filter_by(code='cf321war20tf4').first()
	]
)
cs32 = ClassSpecialty(
	name = 'the great old one',
	description = 'Your patron is a mysterious entity whose nature is utterly foreign to the fabric of reality. It might come from the Far Realm, the space beyond reality, or it could be one of the elder gods known only in legends. Its motives are incomprehensible to mortals, and its knowledge so immense and ancient that even the greatest libraries pale in comparison to the vast secrets it holds. The Great Old One might be unaware of your existence or entirely indifferent to you, but the secrets you have learned allow you to draw your magic from it. Entities of this type include Ghaunadar, called That Which Lurks; Tharizdun, the Chained God; Dendar, the Night Serpent: Zargon, the Returner; Great Cthulhu; and other unfathomable beings.[h]expanded spell list[/h]The Great Old One lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you.\n[tc]great old one expanded spells[/tc][th]spell level[/th/]spells[/th][tr]1st[/td/]dissonant whispers, Tasha\'s hideous laughter[/tr][tr]2nd[/td/]detect thoughts, phantasmalforce[/tr][tr]3rd[/td/]clairvoyance, sending[/tr][tr]4th[/td/]dominate beast. Evard\'s black tentacles[/tr][tr]5th[/td/]dominate person, telekinesis[/tr][/t]',
	class_specialty_features = [
		Feature.query.filter_by(code='cf322war21go1').first(),
		Feature.query.filter_by(code='cf323war22go2').first(),
		Feature.query.filter_by(code='cf324war23go3').first(),
		Feature.query.filter_by(code='cf325war24go4').first()
	]
)
cs33 = ClassSpecialty(
	name = 'school of abjuration',
	description = 'The School of Abjuration emphasizes magic that blocks, banishes, or protects. Detractors of this school say that its tradition is about denial, negation rather than positive assertion. You understand, however, that ending harmful effects, protecting the weak, and banishing evil influences is anything but a philosophical void. It is a proud and respected vocation. Called abjurers, members of this school are sought when baleful spirits require exorcism, when important locations must be guarded against magical spying, and when portals to other planes of existence must be closed.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf336wiz11ab1').first(),
		Feature.query.filter_by(code='cf337wiz12ab2').first(),
		Feature.query.filter_by(code='cf338wiz13ab3').first(),
		Feature.query.filter_by(code='cf339wiz14ab4').first(),
		Feature.query.filter_by(code='cf340wiz15ab5').first()
	]
)
cs34 = ClassSpecialty(
	name = 'school of conjuration',
	description = 'As a conjurer, you favor spells that produce objects and creatures out of thin air. You can conjure billowing clouds of killing fog or summon creatures from elsewhere to fight on your behalf. As your mastery grows, you learn spells of transportation and can teleport yourself across vast distances, even to other planes of existence, in an instant.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf341wiz16co1').first(),
		Feature.query.filter_by(code='cf342wiz17co2').first(),
		Feature.query.filter_by(code='cf343wiz18co3').first(),
		Feature.query.filter_by(code='cf344wiz19co4').first(),
		Feature.query.filter_by(code='cf345wiz20co5').first(),
	]
)
cs35 = ClassSpecialty(
	name = 'school of divination',
	description = 'The counsel of a diviner is sought by royalty and commoners alike, for all see a clearer understanding of the past, present, and future. As a diviner, you strive to part the veils of space, time, and consciousness so that you can see clearly. You work to master spells of discernment, remote viewing, supernatural knowledge, and foresight.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf346wiz21di1').first(),
		Feature.query.filter_by(code='cf347wiz22di2').first(),
		Feature.query.filter_by(code='cf348wiz23di3').first(),
		Feature.query.filter_by(code='cf349wiz24di4').first(),
		Feature.query.filter_by(code='cf350wiz25di5').first()
	]
)
cs36 = ClassSpecialty(
	name = 'school of enchantment',
	description = 'As a member of the School of Enchantment, you have honed your ability to magically entrance and beguile other people and monsters. Some enchanters are peacemakers who bewitch the violent to lay down their arms and charm the cruel into showing mercy. Others are tyrants who magically bind the unwilling into their service. Most enchanters fall somewhere in between.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf351wiz26en1').first(),
		Feature.query.filter_by(code='cf352wiz27en2').first(),
		Feature.query.filter_by(code='cf353wiz28en3').first(),
		Feature.query.filter_by(code='cf354wiz29en4').first(),
		Feature.query.filter_by(code='cf355wiz30en5').first()
	]
)
cs37 = ClassSpecialty(
	name = 'school of evocation',
	description = 'You focus your study on magic that creates powerful elemental effects such as bitter cold, searing flame, rolling thunder, crackling lightning, and burning acid. Some evokers find employment in military forces, serving as artillery to blast enemy armies from afar. Others use their spectacular power to protect the weak, while some seek their own gain as bandits, adventurers, or aspiring tyrants.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf356wiz31ev1').first(),
		Feature.query.filter_by(code='cf357wiz32ev2').first(),
		Feature.query.filter_by(code='cf358wiz33ev3').first(),
		Feature.query.filter_by(code='cf359wiz34ev4').first(),
		Feature.query.filter_by(code='cf360wiz35ev5').first()
	]
)
cs38 = ClassSpecialty(
	name = 'school of illusion',
	description = 'You focus your studies on magic that dazzles the senses, befuddles the mind, and tricks even the wisest folk. Your magic is subtle, but the illusions crafted by your keen mind make the impossible seem real. Some illusionists&#8211;including many gnome wizards&#8211;are benign tricksters who use their spells to entertain. Others are more sinister masters of deception, using their illusions to frighten and fool others for their personal gain.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf361wiz36il1').first(),
		Feature.query.filter_by(code='cf362wiz37il2').first(),
		Feature.query.filter_by(code='cf363wiz38il3').first(),
		Feature.query.filter_by(code='cf364wiz39il4').first(),
		Feature.query.filter_by(code='cf365wiz40il5').first()
	]
)
cs39 = ClassSpecialty(
	name = 'school of necromancy',
	description = 'The School of Necromancy explores the cosmic forces of life, death, and undeath. As you focus your studies in this tradition, you learn to manipulate the energy that animates all living things. As you progress, you learn to sap the life force from a creature as your magic destroys its body, transforming that vital energy into magical power you can manipulate.\nMost people see necromancers as menacing, or even villainous, due to the close association with death. Not all necromancers are evil, but the forces they manipulate are considered taboo by many societies.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf366wiz41ne1').first(),
		Feature.query.filter_by(code='cf367wiz42ne2').first(),
		Feature.query.filter_by(code='cf368wiz43ne3').first(),
		Feature.query.filter_by(code='cf369wiz44ne4').first(),
		Feature.query.filter_by(code='cf370wiz45ne5').first()
	]
)
cs40 = ClassSpecialty(
	name = 'school of transmutation',
	description = 'You are a student of spells that modify energy and matter. To you, the world is not a fixed thing, but eminently mutable, and you delight in being an agent of change.\nYou wield the raw stuff of creation and learn to alter both physical forms and mental qualities. Your magic gives you the tools to become a smith on reality\'s forge.\nSome transmuters are tinkerers and pranksters, turning people into toads and transforming copper into silver for fun and occasional profit. Others pursue their magical studies with deadly seriousness, seeking the power of the gods to make and destroy worlds.',
	class_specialty_features = [
		Feature.query.filter_by(code='cf371wiz46tr1').first(),
		Feature.query.filter_by(code='cf372wiz47tr2').first(),
		Feature.query.filter_by(code='cf373wiz48tr3').first(),
		Feature.query.filter_by(code='cf374wiz49tr4').first(),
		Feature.query.filter_by(code='cf375wiz50tr5').first()
	]
)

specialties = [
	cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8,cs9,cs10,
	cs11,cs12,cs13,cs14,cs15,cs16,cs17,cs18,cs19,cs20,
	cs21,cs22,cs23,cs24,cs25,cs26,cs27,cs28,cs29,cs30,
	cs31,cs32,cs33,cs34,cs35,cs36,cs37,cs38,cs39,cs40
]

db.session.add_all(specialties)
db.session.commit()