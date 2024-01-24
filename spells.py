import basics
import classStuff
import random

class Spell:
    def __init__(self,nname,llevel,ttext='',cList=[]):
        self.name=nname
        self.level=llevel
        self.text=ttext
        self.higher=[]
        self.learnedBy=cList
class miniSpell:
    def __init__(self,sspell,nname,nnote,vvalue):
        self.spell=sspell
        self.name=nname
        self.note=nnote
        self.value=vvalue
        
spells={}
loader=[]

def setCantrips(number, character,ckey=''):
    dict={5:2,11:3,17:4}
    for i in range(1,21):
        if i<5:
            dict[i]=1
        elif i<11:
            dict[i]=2
        elif i<17:
            dict[i]=3
        else:
            dict[i]=4
    acidSplash=Spell("Acid Splash",0,'''You shoot acid up to 60'.  You can hit up to two adjacent creatures for '''+str(dict[character.level])+'d6 damage, Dex save negates',['Artificer','Sorcerer','Wizard'])
    bladeWard=Spell("Blade Ward",0,'''You gain resistance against bludgeoning, piercing, and slashing damage from weapon attacks until your next turn ends.''',['Bard','Sorcerer','Warlock','Wizard'])
    if character.level>4:
        text= "takes "+str(dict[character.level]-1)+"d8 extra thunder damage and "
    else:
        text=""
    boomingBlade=Spell("Booming Blade",0,"You make a melee weapon attack with range 5'. On hit target also "+text+ "takes "+str(dict[character.level])+"d8 thunder damage if they willingly move 5 feet or more before your next turn.",['Artificer','Sorcerer','Warlock','Wizard'])
    createBonfire=Spell("Create Bonfire",0,'''You can create a 5' cube bonfire lasting Concentration max 1 minute.
It deals '''+str(dict[character.level])+'''d8 fire damage dex negates against those in the space, entering the space, or ending a turn there.
It lights unattended flamable stuff on fire''',['Artificer','Druid','Sorcerer','Warlock','Wizard'])
    dancingLights=Spell("Dancing Lights",0,'''You create either 4 small lights or 1 big one at points within 120' and each within 20' of another point.
You choose the form for each light from torch, lantern, or orb and they float.
If you have 1 big light you only get a vague humanoid form instead, and it doesn't float.
Regardless, they glow in a 10' radius each, and you can move them 60' each turn as a bonus action, but not past 120' of you.
If a light goes out of range it winks out until back in range.
They last Concentration max 1 min''',['Artificer','Bard','Sorcerer','Wizard'])
    fireBolt=Spell("Fire Bolt",0,'''You do +'''+str(dict[character.level])+'''d10 fire damage to a target in 120' via ranged spell attack.
If it is an unintended flamable object and you hit it, it ignites''',['Artificer','Bard','Sorcerer','Wizard'])
    friends=Spell("Friends",0,'''This spell has no range-based limitations, and even works across planes.
For Concentration max 1 minute, you have advantage on all Charisma checks directed at one creature of your choice that isn't hostile toward you.
When the spell ends, the creature is magically compelled to realize that you used magic to influence its mood and magically becomes hostile toward you (no save).
A creature prone to violence might attack you, while another creature might seek retribution in other ways (at the DM's discretion).''',['Bard','Sorcerer','Warlock','Wizard'])
    frostBite=Spell("Frostbite",0,'''target within 60' must make Con save or take '''+str(dict[character.level])+'''d6 cold damage and have disadvantage on their first attack if any next turn''',['Artificer','Druid','Sorcerer','Warlock','Wizard'])
    if character.level>4:
        text1= str(dict[character.level]-1)+"d8 extra fire damage and "
        text2= str(dict[character.level]-1)+"d8+"
    else:
        text1=""
        text2=""
    greenFlameBlade=Spell("Green Flame Blade",0,'''You make a melee weapon attack that does '''+text1+text2+str(character.stats[character.classes[0].spellStat])+" extra fire damage to a second target you can see adjacent to the first.",['Artificer','Sorcerer','Warlock','Wizard'])
    guidance=Spell("Guidance",0,'''A character you touch recieves +1d4 to its next ability check within Concentration up to 1 min''',['Artificer','Cleric','Druid','Ranger'])
    light=Spell("Light",0,'''Touched object emits bright light 20' and dim light 20' past that for 1 hour.
Your choice of color. You can end the spell by recasting it or as an action.
Object attenders if any may Dex save to negate''',['Artificer','Bard','Cleric','Sorcerer','Wizard'])
    lightningLure=Spell("Lightning Lure",0,"You whip a visible target in 15' with lightning, pulling it adjacent to you on a failed Str save and dealing "+str(dict[character.level])+"d8 lightning damage if you did",['Artificer','Sorcerer','Warlock','Wizard'])
    mageHand=Spell("Mage Hand",0,'''You create a glowing hand that you control within 30'.
It takes your action to use, and has 30' flying movement and an action each time you use it.
It lasts 1 minute or until you make another hand or dismiss it as an action.
It vanishes if it is ever more than 30' from you, and it can't attack or carry more than 10 pounds.
It can't/doesn't trigger/activate magical items/traps''',['Artificer','Bard','Sorcerer','Warlock','Wizard'])
    magicStone=Spell("Magic Stone",0,'''As a bonus action you enchant 3 pebbles for 1 minute.
All beings are magically capable of using these stones to make 60' ranged spell attacks using your spell stat as if you threw it rather than them.
On a hit, the target takes 1d6+'''+str(character.stats[character.classes[0].spellStat])+''' bludgeoning damage.
The spell ends if you cast it again.''',['Artificer','Druid','Warlock'])
    mending=Spell("Mending",0,"You perfectly repair a break, tear, or hole in an object that is no more than 1 foot in its longest dimension.",['Artificer','Bard','Cleric','Druid','Sorcerer','Wizard'])
    message=Spell("Message",0,'''You can send a message that only the intended recipient can hear, and grant them the power to likewise respond.
You don't need line of effect to cast this spell, but 3 feet of wood or dirt, 1 foot of stone, 1 inch of normal metal, or a thin sheet of lead block the spell.
The spell doesn't even need a line, and can twist around corners or through microscopic openings if needed.
Magical silence blocks the spell if it can't weasel around it.
You have to target a specific recipient and a direction.
If you are wrong about the direction or the recipient is more than 120' from you, the spell fails''',['Artificer','Bard','Sorcerer','Wizard'])
    mindSliver=Spell("Mind Sliver",0,'''Target within 60' must Int save or take '''+str(dict[character.level])+'''d6 psychic damage, and the first time it makes a saving throw before the end of your next turn,
it gets -1d4.''',['Bard','Sorcerer','Warlock','Wizard'])
    minorIllusion=Spell("Minor Illusion",0,'''You create a sound or an image within range 30' that lasts for 1 minute.
The illusion also ends if you dismiss it as an action or cast this spell again.

If you create a sound, its volume can range from a whisper to a scream.
It can be any sound you choose, including speech or sounds normally outside the volume range.
The sound continues unabated throughout the duration, or you can make discrete sounds at different times before the spell ends.

If you create an image it must be of an object or objects—such as a chair, muddy footprints, or a small chest— and it must be no larger than a 5' cube.
The image can't create sound, light, smell, or any other sensory effect.
Physical interaction with the image reveals it to be an illusion, because things can pass through it.

If a creature uses its action to examine the sound or image, the creature can determine that it is an illusion with a successful Intelligence (Investigation) check against the usual save DC.
If a creature discerns the illusion for what it is, the illusion becomes faint to the creature.''',['Bard','Sorcerer,Warlock','Wizard'])
    poisonSpray=Spell("Poison Spray",0,"You deal "+str(dict[character.level])+"d12 damage to a target within 10', con save negates.",['Artificer','Bard','Druid','Sorcerer','Warlock','Wizard'])
    prestidigitation=Spell("Prestidigitation",0,'''You can do any of the following at 10' range:
- create an instantaneous, harmless sensory effect, such as a shower of sparks, a puff of wind, faint musical notes, or an odd odor.
- instantaneously light or snuff out a candle, a torch, or a small campfire
- instantaneously clean or soil an object no larger than 1 cubic foot
- You chill, warm, or flavor up to 1 cubic foot of nonliving material (1 hour)
- You make a color, a small mark, or a symbol appear on an object or a surface (1 hour)
- create a nonmagical trinket or an illusory image that can fit in your hand (end of your next turn)

You can have up to three of the above that have durations active at once,
and can end them as an action.''',['Artificer','Bard','Sorcerer','Warlock','Wizard'])
    rayOfFrost=Spell("Ray of Frost",0,'''You deal '''+str(dict[character.level])+'''d8 damage to a target in 60' via ranged spell attack,
and reduce their speed by 10' until the start of your next turn.''',['Artificer','Bard','Sorerer','Wizard'])
    resistance=Spell("Resistance",0,"For Concentration up to 1 minute the touched target can add 1d4 to a saving throw after rolling if they so choose, once.",['Artificer','Cleric','Druid','Ranger'])
    sacredFlame=Spell("Sacred Flame",0,"Target within 60' must Dex save or take "+str(dict[character.level])+"d8 radiant damage.\nThis spell does not need line of effect and ignores all cover.",['Cleric'])
    shockingGrasp=Spell("Shocking Grasp",0,'''Make a melee spell attack, with advantage if the target is wearing metal armor.
If you hit, deal '''+str(dict[character.level])+'''d8 lightning damage and the target loses its reaction.''',['Artificer','Bard','Sorcerer','Wizard'])
    spareTheDying=Spell("Spare the Dying",0,"You succeed on a Wis check to stabilize a target you touch.",['Artificer','Cleric','Ranger'])
    swordBurst=Spell("Sword Burst",0,"Everyone next to you must make a Dex save or take "+str(dict[character.level])+"d6 force damage.", ['Artificer','Sorcerer','Warlock','Wizard'])
    thornWhip=Spell("Thorn Whip",0,"Make a melee spell attack with range 30'.  You deal "+str(dict[character.level])+"d6 piercing damage on a hit and pull a Large or smaller target up to 10' towards you",['Artificer','Druid','Ranger'])
    thunderClap=Spell("Thunderclap",0,"Everyone next to you must make a Con save or take "+str(dict[character.level])+"d6 thunder damage. Also, you make a loud noise.", ['Artificer','Bard','Druid','Sorcerer','Warlock','Wizard'])
    trueStrike=Spell("True Strike",0,'''You have advantage on your first attack roll next turn against a specific target you choose within 30'. This spell requires Concentration.''',['Bard','Sorcerer','Warlock','Wizard'])
    viciousMockery=Spell("Vicious Mockery",0,'''A target within 60' that can hear you must succeed on a Wis save or take'''+str(dict[character.level])+'''d4 psychic damage and have disadvantage on the next attack roll it makes before the end of its next turn.''',['Bard'])

    roller=[]
    roller.append(acidSplash)
    roller.append(bladeWard)
    roller.append(boomingBlade)
    roller.append(createBonfire)
    roller.append(dancingLights)
    roller.append(fireBolt)
    roller.append(friends)
    roller.append(frostBite)
    roller.append(greenFlameBlade)
    roller.append(guidance)
    roller.append(light)
    roller.append(lightningLure)
    roller.append(mageHand)
    roller.append(magicStone)
    roller.append(mending)
    roller.append(message)
    roller.append(mindSliver)
    roller.append(minorIllusion)
    roller.append(poisonSpray)
    roller.append(prestidigitation)
    roller.append(rayOfFrost)
    roller.append(resistance)
    roller.append(sacredFlame)
    roller.append(shockingGrasp)
    roller.append(spareTheDying)
    roller.append(swordBurst)
    roller.append(thornWhip)
    roller.append(thunderClap)
    roller.append(trueStrike)
    roller.append(viciousMockery)
    
    global spells
    cantrips={}
    for i in roller:
        spells[i.name]=i
        cantrips[i.name]=i

    if ckey!='':
        
        if ckey=='a':
            cclass=classStuff.Artificer
        if ckey=='b':
            cclass=classStuff.Bard
        if ckey=='w':
            cclass=classStuff.Wizard
        if ckey=='W':
            cclass=classStuff.Warlock
            
        present=[]
        for i in character.spells:
            if character.spells[i].spell.level==0:
                character.spells[i].spell=cantrips[i]
                present.append(i)

        code=character.saveString
        i=0
        done=False
        while not done:
            if code[0]==ckey:  #e.g. 'a' for Artificer
                value=int(code[4])
                stringKey=i+4
                done=True
            else:
                i+=1
                code=code[1:]
                    
        while value<number:
            j=random.choice(list(cantrips))
            if (j not in present) and (cclass.name in cantrips[j].learnedBy):
                character.addSpell(cantrips[j])
                present.append(j)
                value+=1
        if value>=10:
            raise "We were wrong.  We thought there would never be more than 6, let alone 9.  10 Cantrips.  I'm sorry :("
        character.saveString=character.saveString[:stringKey]+str(value)+character.saveString[stringKey+1:]
                
            


absorbElements=Spell("Absorb Elements",1,'''You can use your reaction to gain resistance to elemental damage you are about to take, and deal 1d6 extra damage of the triggering type on your first hit afterwards.''',['Artificer','Druid','Ranger','Sorcerer','Wizard'])
alarm=Spell("Alarm",1,'''You can take a minute to alarm a door, a window, or an area that is no larger than a 20-foot cube.
An alarm triggers whenever a creature not authorized during casting touches or enters the warded area for 8 hours.
The alarm is mental or audible, chosen when cast.

A mental alarm alerts and wakes you with 1 mile range.
An audible alarm rings like a hand bell for 10 seconds.''',['Artificer','Ranger','Wizard'])
animalFriendship=Spell("Animal Friendship",1,'''Target beast with Int 3 or less that you can see and be seen and heard by within 30' must Wis save or be charmed by you for 24 hours or until you or your companions harm it.''',['Bard','Druid','Ranger'])
bane=Spell("Bane",1,'''3 or fewer targets in 30' must Cha save or get -1d4 on attack rolls and saving throws for Concentration max 1 minutes.''',['Bard','Cleric'])
catapult=Spell("Catapult",1,'''You can make one unattended object weighing 1 to 5 pounds within 60' blast up to 90 feet in a direction you choose.
It stops, dealing and taking 3d8 bludgeoning damage, if it hits something before then.
Creatures in the path must make a Dex save to avoid it''',['Artificer','Sorcerer','Wizard'])
charmPerson=Spell("Charm Person",1,''' Target Humanoid within 30' makes a Wis save and has advantage if you or your allies are fighting them.
On failure, they're charmed by you for 1 hour or until you or your companions harm them. They regard you as a friendly acquaintance.

When the spell ends, they know they were charmed by you.''',['Bard','Druid','Sorcerer','Warlock','Wizard'])
colorSpray=Spell("Color Spray",1,'''6d10 hp of creatures in a 15-foot cone originating from you are affected in ascending order of their current hit points (ignoring unconscious creatures and creatures that can't see).

Starting with the creature that has the lowest current hit points, each creature affected by this spell is blinded until the end of your next turn.
Subtract each creature's hit points from the total before moving on to the creature with the next lowest hit points.
A creature's hit points must be equal to or less than the remaining total for that creature to be affected.''',['Bard','Sorcerer','Wizard'])
command=Spell("Command",1,'''You speak a one-word command to a creature you can see within 60', who Wis saves or follows the command on their next turn.
The spell has no effect if the target is undead, if it doesn't understand your language, or if your command is directly harmful to it.''',['Bard','Cleric','Paladin'])
comprehendLanguages=Spell("Comprehend Languages",1,'''You understand the literal meaning of any spoken language that you hear.
You also understand any written language that you see, but you must be touching the surface on which the words are written.
It takes about 1 minute to read one page of text.''',['Bard','Sorcerer','Warlock','Wizard'])
cureWounds=Spell("Cure Wounds",1,'''You can heal 1d8 + your spell modifier hp via touch''',['Artificer','Bard','Cleric','Druid','Paladin','Ranger'])
detectMagic=Spell("Detect Magic",1,'''You can detect magic within 30 feet for Concentration max 10 mins, using your action to visualize auras and determine schools of magic after detecting the general presence.
The spell goes through solid matter, but only to a limited extent.''',["Artificer",'Bard','Cleric','Druid','Paladin','Ranger','Sorcerer','Wizard'])
disguiseSelf=Spell("Disguise Self",1,'''You can assume a disguise similar in physical form to you for 1 hour. It is a visual illusion''',['Artificer','Bard','Sorcerer','Wizard'])
dissonantWhispers=Spell("Dissonant Whispers",1,'''A target in 60' must Wis save or take 3d6 psychic damage immediately use its reaction, if available, to move as far as its speed allows away from you.
The creature doesn't move into obviously dangerous ground, such as a fire or a pit.
On a successful save, the target takes half as much damage and doesn't have to move away.
A deafened creature automatically succeeds on the save.''',['Bard'])
earthTremor=Spell("Earth Tremor",1,'''Other creatures in 10' Dex save or take 1d6 bludgeoning damage and are knocked prone.
Loose earth or stone ground in the area becomes difficult terrain until cleared, with each square requiring at least 1 minute to clear by hand.''',['Bard','Druid','Sorcerer','Wizard'])
expeditiousRetreat=Spell("Expeditious Retreat",1,'''Cast as a bonus action, you can Dash now and as a bonus action for Concentration max 10 mins.''',['Artificer','Bard','Sorcerer','Warlock','Wizard'])
faerieFire=Spell("Faerie Fire",1,'''Each object and every creature failing a Dex save in a 20' cube within 60' glows your choice of blue, green, or violet (dim light, 10' radius) for Concentration max 1 min.
Attackers have advantage against glowing things they see, and the glow renders invisibility moot.''',['Artificer','Bard','Druid','Ranger'])
falseLife=Spell("False Life",1,'''You get 1d4+4 temp hp''',['Artificer','Bard','Sorcerer','Wizard'])
featherFall=Spell("Feather Fall",1,'''You and up to 5 allies within 60 feet stop falling and slowly descend 60' per round for 1 minute.
The spell ends on a creature when they land.''',['Artificer','Bard','Sorcerer','Wizard'])
grease=Spell("Grease",1,'''cover 10' square within 60' in grease, forcing Dex saves v.s. falling prone on cast, entry, and turn end. Also difficult terrain.''',['Artificer','Bard','Wizard'])
guidingHand=Spell("Guiding Hand",1,'''You can take 1 minute to create a Tiny incorporeal hand of shimmering light in an adjacent unoccupied space you can see.
The hand exists for Concentration max 8 hours, but it disappears if you teleport or you travel to a different plane of existence.

When the hand appears, you name one major landmark, such as a city, mountain, castle, or battlefield on the same plane of existence as you.
Someone in history must have visited the site and mapped it; If the landmark appears on no map in existence, the spell fails.
Otherwise, whenever you move toward the hand, it moves away from you at the same speed you moved, and it moves in the direction of the landmark, always remaining 5' away from you.

If you don't move toward the hand, it remains in place until you do and beckons for you to follow once every 1d4 minutes.''',['Bard','Cleric','Druid','Wizard'])
healingWord=Spell("Healing Word",1,'''As a bonus action heal 1d4 + your spell modifier to target within 60'.''',['Bard','Ceric','Druid'])
heroism=Spell("Heroism",1,'''A touched creature becomes immune to being frightened,
and gains temp hp equal to your spell mod at the start of each of its turns.
Any remaining temp hp are lost when the spell ends, which it does after Concentration max 1 minute.''',['Bard','Paladin'])
idInsinuation=Spell("Id Insinuation",1,'''Target in 60' Wis saves or is incapacitated for Concentration max 1 minute.
If it fails it also takes 1d12 psychic damage when it ends a turn, and it can then make another Wis save.
The spell ends whenever the target saves.''',['Bard','Sorcerer','Warlock','Wizard'])
identify=Spell("Identify",1,'''You can take a minute to learn the magic affecting an object or creature touched, including the full workings of a magical item''',['Artificer','Bard','Wizard'])
illusoryScript=Spell("Illusory Script",1,'''You can take a minute and expend 10 gold in lead ink to write a message on suitable writing material.
You and any creatures you designate when you cast the spell see the writing as normal and written in your hand, though it magically conveys whatever meaning you intended when you wrote the text regardless of language.
To all others, the writing appears as if it were written in an unknown or magical script that is unintelligible.
Alternatively, you can cause the writing to appear to outsiders to be an entirely different message, written in a different hand and language, though the language must be one you know.

Should the spell be dispelled, the original script and the illusion both disappear.
A creature with truesight can read the hidden message.''',['Bard','Warlock','Wizard'])
jump=Spell("Jump",1,'''You triple a creature's jump distance for 1 minute''',['Artificer','Bard','Druid','Ranger','Sorcerer','Wizard'])
longstrider=Spell("Longstrider",1,'''you give a creature +10ft speed for 1 hour''',['Artificer','Bard','Druid','Ranger','Wizard'])
magicMissile=Spell("Magic Missile",1,'''Deal 1d4+1 force damage with each of three missiles unerringly to a target or targets within 120'.''',['Sorcerer','Wizard'])
puppet=Spell("Puppet",1,'''Target humanoid in 120' Con saves or voluntarily moves its speed in a direction you choose.
You can also have them drop everything if they fail the save.
Blocked by charm immunity, and requires only somatic components.''',['Bard','Warlock','Wizard'])
purify=Spell("Purify Food and Drink",1,'''You cleanse food and drink in a 5' sphere''',['Artificer','Cleric','Druid','Paladin','Ranger'])
rayOfSickness=Spell("Ray of Sickness",1,'''60' ranged spell attack for 2d8 poison damage on hit.
On hit, Con save or Poisoned until the end of your next turn.''',['Sorcerer','Wizard'])
sanctuary=Spell("Sanctuary",1,'''As a bonus action, you protect a target within 30 feet for 1 min. Direct attackers must Wis save vs choosing a new target or losing the attack or spell.
If the warded creature makes an attack, casts a spell that affects an enemy, or deals damage to another creature, this spell ends.''',['Artificer','Cleric'])
shield=Spell("Shield",1,'''As a reaction to being hit or taking damage, reverse time before the attack that hit and get +5 AC, possibly causing it to miss.
You retain the AC bonus until your next turn starts.
You are also retroactively rendered immune to Magic Missile by this spell until then.''',['Sorcerer','Wizard'])
silentImage=Spell("Silent Image",1,'''You create an illusory image that is no larger than a 15-foot cube. The image appears at a spot within 60' and lasts for Concentration max 10 minutes.
You can use your action to cause the image to move to any spot within 60'.
As the image changes location, you can alter its appearance so that its movements appear natural.
For example, if you create an image of a creature and move it, you can alter the image so that it appears to be walking.

Physical interaction with the image reveals it to be an illusion, because things can pass through it.
A creature that uses its action to examine the image can determine that it is an illusion with a successful Int (Investigation) check against the save DC.
If a creature discerns the illusion for what it is, the creature can see through the image.''',['Bard','Sorcerer','Wizard'])
silveryBarbs=Spell("Silvery Barbs",1,'''You can use your reaction to force a target succeeding an attack roll, saving throw, or ability check to reroll and use the worse result.

You can then choose a different creature you can see within range (you can choose yourself).
The chosen creature has advantage on the next attack roll, ability check, or saving throw it makes within 1 minute.
A creature can be empowered by only one use of this spell at a time, and the empowerment is "non-magical".''',['Bard','Sorcerer','Wizard'])
sleep=Spell("Sleep",1,'''Up to 5d8 total hp of creatures with 20' of a point you pick within 90' are affected by this spell.
Creatures are affected in ascending order of their current hit points (ignoring unconscious and immune creatures).

Starting the one with lowest current hit points, each creature affected by this spell falls unconscious for 1 min or until they take damage or someone uses an action to shake or slap them awake.
Subtract each creature's hit points from the total before moving on to the creature with the next lowest hit points.
A creature's hit points must be equal to or less than the remaining total for that creature to be affected.

Undead and creatures immune to being charmed aren't affected by this spell.''',['Bard','Sorcerer','Wizard'])
badSnare=Spell("Lesser Snare",1,'''You can take 1 min to create an invisible magical trap in a 5' radius circle that lasts 8 hours from 25' of rope.
It can be detected with an Int(Investigation) check vs your save DC.
It hoists a Small-Large creature into the air upside down, restraining them, Dex save to negate.
Those trapped can escape with Dex saves or Int(Arcana) checks vs your spell save DC.''',['Artificer','Druid','Ranger','Wizard'])
goodSnare=Spell("Snare",1,'''You can take 1 min to create a permanent invisible magical trap in a 5' radius circle from 30' of rope.
It can be detected with an Int(Investigation) check vs your save DC.
It hoists a Small or larger creature into the air upside down, restraining them and applying the prone condition, Dex save to negate.
Those trapped can escape with Dex saves at disadvantage or an outside helper can use Int(Arcana) checks vs your spell save DC.''',['Druid','Ranger','Wizard'])
speakWithAnimals=Spell("Speak with Animals",1,'''You can verbally communicate with and understand beasts for the next 10 minutes''',['Druid','Ranger'])
suddenAwakening=Spell("Sudden Awakening",1,'''As a bonus action, you wake all cratures in 10' and then they may instantly stand up without expending movement.''',['Bard','Ranger','Sorcerer','Wizard'])

causticBrew=Spell("Tasha's Caustic Brew",1,'''Shoot acid in a 30' by 5' line. Each creature in the line must make a Dex save or take 2d4 dmg/turn for Concentration max 1 min or until they use an action to clean it off.''',['Artificer'])
hideousLaughter=Spell("Tasha's Hideous Laughter",1,''' Target in 30' must Wis save or become prone, incapacitated, and unable to stand up for the duration.
A creature with an Intelligence score of 4 or less isn't affected.

At the end of each of its turns, and each time it takes damage, the target can make another Wis save.
The target has advantage if it's triggered by damage.
On a success, the spell ends but the target remains prone until it stands up.''',['Bard','Wizard'])
thunderwave=Spell("Thunderwave",1,'''Everyone in a 15' cube with you adjacent to it or present in a space on a face of the cube
takes 2d8 thunder damage (Con save for half) and is pushed 10' away from you if they failed the save.
Additionally, there's a loud boom.
Additionally, unsecured objects in the spells range are automatically moved 10' away, but not damaged.''',['Bard','Druid','Sorcerer','Wizard'])
unearthlyChorus=Spell("Unearthly Chorus",1,'''Music of a style you choose fills the air around you in a 30' radius.
The music spreads around corners and can be heard from up to 100' away.
The music moves with you, centered on you for the duration.

Until the spell ends, you make Charisma (Performance) checks with advantage.
In addition, you can use a bonus action on each of your turns to beguile one creature you choose within 30' that can see you and hear the music.
The creature must Cha save or become friendly to you for as long as it can hear the music and for 1 hour thereafter.
You make Charisma (Deception) and Charisma (Persuasion) checks against creatures made friendly by this spell with advantage.

Creatures currently being attacked by you or your companions automatically succeed the save for this spell,
but you can attack friendly targets with impunity after they fail the save.

The area effect part of the spell lasts Concentration max 10 minutes''',['Bard'])
unseenServant=Spell("Unseen Servant",1,'''You create an invisible, mindless, shapeless, Medium force that performs simple tasks at your command for 1 hour.
The servant springs into existence in an unoccupied space on the ground within 60'.
It has AC 10, 1 hit point, a Strength of 2, and it can't attack. If it drops to 0 hit points, the spell ends.

Once on each of your turns as a bonus action, you can mentally command the servant to move up to 15 feet and interact with an object.
You can also give it a more general command orally as a free action at any time it can hear you.

The servant can perform simple tasks that a human servant could do, such as fetching things, cleaning, mending, folding clothes, lighting fires, serving food, and pouring wine.
Once you give the command, the servant performs the task to the best of its ability until it completes the task, then waits for your next command.

If you command the servant to perform a task that would move it more than 60 feet away from you, the spell ends.''',['Bard','Warlock','Wizard'])
                   
                   

beastSense=Spell("Beast Sense",2,'''For concentration max 1 hour, you can see and hear through a willing beast
you touch during casting, using its senses rather than your own.''',['Druid','Ranger'])



loader.append(alarm)
loader.append(animalFriendship)
loader.append(bane)
loader.append(catapult)
loader.append(absorbElements)
loader.append(charmPerson)
loader.append(colorSpray)
loader.append(command)
loader.append(comprehendLanguages)
loader.append(cureWounds)
loader.append(detectMagic)
loader.append(disguiseSelf)
loader.append(dissonantWhispers)
loader.append(earthTremor)
loader.append(expeditiousRetreat)
loader.append(faerieFire)
loader.append(falseLife)
loader.append(featherFall)
loader.append(grease)
loader.append(guidingHand)
loader.append(healingWord)
loader.append(heroism)
loader.append(idInsinuation)
loader.append(identify)
loader.append(illusoryScript)
loader.append(jump)
loader.append(longstrider)
loader.append(magicMissile)
loader.append(puppet)
loader.append(purify)
loader.append(rayOfSickness)
loader.append(sanctuary)
loader.append(shield)
loader.append(silentImage)
loader.append(silveryBarbs)
loader.append(sleep)
loader.append(badSnare)
loader.append(goodSnare)
loader.append(speakWithAnimals)
loader.append(suddenAwakening)
loader.append(causticBrew)
loader.append(hideousLaughter)
loader.append(thunderwave)
loader.append(unearthlyChorus)
loader.append(unseenServant)

loader.append(beastSense)
                   
for i in loader:
    spells[i.name]=i

ritualSpells=['Alarm','Animal Messenger','Augury','Beast Sense','Lesser Ceremony','Ceremony','Commune','Commune with City','Commune with Nature','Comprehend Languages','Contact Other Plane','Detect Magic','Detect Poison and Disease','Divination',"Drawmij's Instant Summons",'Feign Death','Find Ancient Familiar','Find Modern Familiar','Forbiddance','Gentle Repose','Guiding Hand','Identify','Illusory Script',"Leomund's Tiny hut",'Locate Animals or Plants','Magic Mouth','Meld into Stone','Memorize Spell','Modify Spell','Phantom Steed','Purify Food and Drink',"Rary's Telepathic Bond",'Scribe Spell','Silence','Skywrite','Speak with Animals',"Tenser's Floating Disk",'Unseen Servant','Water Breathing','Water Walk','Wild Cunning']

def setRituals(character):
    rit=[]
    for i in character.spells:
        if i in ritualSpells:
            rit.append(i)
    if len(rit)>0:
        text='''You can cast the following spells as rituals:

'''
        for i in rit:
            text=text+"- "+i+"\n"
        ritual=basics.Property("Ritual Casting",text)
        character.addProperty(ritual)

def learnSpell(character,known):
    
    mmin=99 #determine level
    ans=0
    for i in known:
        if i!=0 and (len(known[i])<mmin or (len(known[i])==mmin and i>ans)):
            mmin=len(known[i])
            ans=i
            
    j=[] #load spells
    for i in spells: 
        if character.classes[0].name in spells[i].learnedBy and spells[i].level==ans: #will need adjustment for multiclassing, probably additional parameter to function
            j.append(spells[i])

    for i in character.spells: #remove matches
        for k in j:
            if i==k:
                j.remove(k)
            
    
    
    k=random.choice(j) #add spell
    character.addSpell(k)

def highest(cclass,level):
    if cclass.name in ['Artificer']:
        highest={1:1, 5:2, 9:3, 13:4, 17:5}  ##Find the highest spell level known by level
        for i in range(1,5):
            highest[i]=1
        for i in range(5,9):
            highest[i]=2
        for i in range(9,13):
            highest[i]=3
        for i in range(13,17):
            highest[i]=4
        for i in range(17,21):
            highest[i]=5
    if cclass.name in ['Bard']:
        highest={}  ##Find the highest spell level known by level
        for i in range(1,3):
            highest[i]=1
        for i in range(3,5):
            highest[i]=2
        for i in range(5,7):
            highest[i]=3
        for i in range(7,9):
            highest[i]=4
        for i in range(9,11):
            highest[i]=5
        for i in range(11,13):
            highest[i]=6
        for i in range(13,15):
            highest[i]=7
        for i in range(15,17):
            highest[i]=8
        for i in range(17,21):
            highest[i]=9
    return highest[level]

def makeSpellcaster(character,cclass):
    if cclass.name=='Artificer':
        
        aSpell=basics.Property('Artificer Spellcasting','''You can cast spells using thieves' tools or artisans' tools.
                        You can change out your prepared non-cantrip spells from the full list each day.
                        Your save DC is '''+str(basics.getMod(character.stats['int'])+8+character.proficiency)+'.')
        character.addProperty(aSpell)
        boxes={1:2,2:2,3:3}
        for i in range(4,21):
            boxes[i]=4
        sslots=basics.Property('Spell Slots','You have '+str(boxes[character.level])+' 1st level spell slots.')
        character.addProperty(sslots)

        if 'a' not in character.saveString:
            j=[]
            for i in spells:
                if 'Artificer' in spells[i].learnedBy and spells[i].level==1:
                    j.append(spells[i])
            up=0
            for i in range(0,max(basics.getMod(character.stats['int']),1)):
                k=random.choice(j)
                character.addSpell(k)
                j.remove(k)
                up+=1

            if up<10:
                up='0'+str(up)
            else:
                up=str(up)
            character.saveString+='a'+up+'.0'

        code=character.saveString
        i=0
        done=False
        while not done:
            if code[0]=='a':
                key=int(code[1]+code[2])
                done=True
            else:
                i+=1
                code=code[1:]
                
        full=int(character.level/2)+basics.getMod(character.stats['int'])
        diff=full-key #will need adjustment for multiclassing

        lv={}
        for i in range(0,highest(cclass,character.level)+1):
            lv[i]=[]
        for i in character.spells:
            lv[character.spells[i].spell.level].append(i)
            
        while diff>0:
            learnSpell(character,lv)
            diff-=1

        code=character.saveString
        i=0
        done=False
        while not done:
            if code[0]=='a':
                key=i
                done=True
            else:
                i+=1
                code=code[1:]

        dig1=str(int(full/10))
        dig2=str(full%10)
        
        character.saveString=character.saveString[0:key]+'a'+dig1+dig2+character.saveString[key+3:] #save progress
    if cclass.name=='Bard':
        
        aSpell=basics.Property('Bard Spellcasting','''You can cast spells using an instrument as an Arcane focus.
                        Your save DC is '''+str(basics.getMod(character.stats['cha'])+8+character.proficiency)+'.\nYou use Cha for your spellcasting.')
        character.addProperty(aSpell)
        boxes={1:2,2:3,3:4}
        for i in range(4,21):
            boxes[i]=4
        sslots=basics.Property('Spell Slots','You have '+str(boxes[character.level])+' 1st level spell slots.')
        character.addProperty(sslots)

        if 'b' not in character.saveString:
            j=[]
            for i in spells:
                if 'Bard' in spells[i].learnedBy and spells[i].level==1:
                    j.append(spells[i])
            up=0
            for i in range(0,5):
                k=random.choice(j)
                character.addSpell(k)
                j.remove(k)
                up+=1

            if up<10:
                up='0'+str(up)
            else:
                up=str(up)
            character.saveString+='b'+up+'.0'

        code=character.saveString
        i=0
        done=False
        while not done:
            if code[0]=='b':
                key=int(code[1]+code[2])
                done=True
            else:
                i+=1
                code=code[1:]
        skip=0
        if character.level>11:
            skip+=1
            if character.level>15:
                skip+=1
                if character.level>18:
                    skip+=1
                    if character.level>19:
                        skip+=1
            
        full=character.level+4-skip
        diff=full-key #will need adjustment for multiclassing

        lv={}
        for i in range(0,highest(cclass,character.level)+1):
            lv[i]=[]
        for i in character.spells:
            lv[character.spells[i].spell.level].append(i)
            
        while diff>0:
            learnSpell(character,lv)
            diff-=1

        code=character.saveString
        i=0
        done=False
        while not done:
            if code[0]=='b':
                key=i
                done=True
            else:
                i+=1
                code=code[1:]

        dig1=str(int(full/10))
        dig2=str(full%10)
        
        character.saveString=character.saveString[0:key]+'b'+dig1+dig2+character.saveString[key+3:] #save progress
                
            
            
        
            
