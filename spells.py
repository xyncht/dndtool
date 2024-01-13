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

absorbElements=Spell("Absorb Elements",1,'''You can use your reaction to gain resistance to elemental damage you are about to take, and deal 1d6 extra damage of the triggering type on your first hit afterwards.''',['Artificer','Druid','Ranger','Sorcerer','Wizard'])
alarm=Spell("Alarm",1,'''You can take a minute to alarm a door, a window, or an area that is no larger than a 20-foot cube.
An alarm triggers whenever a creature not authorized during casting touches or enters the warded area for 8 hours.
The alarm is mental or audible, chosen when cast.

A mental alarm alerts and wakes you with 1 mile range.
An audible alarm rings like a hand bell for 10 seconds.''',['Artificer','Ranger','Wizard'])
beastSense=Spell("Beast Sense",2,'''For concentration max 1 hour, you can see and hear through a willing beast
you touch during casting, using its senses rather than your own.''',['Druid','Ranger'])
catapult=Spell("Catapult",1,'''You can make one unattended object weighing 1 to 5 pounds within 60' blast up to 90 feet in a direction you choose. It stops, dealing and taking 3d8 bludgeoning damage, if it hits something before then. Creatures in the path must make a Dex save to avoid it''',['Artificer','Sorcerer','Wizard'])
cureWounds=Spell("Cure Wounds",1,'''You can heal 1d8 + your spell modifier hp via touch''',['Artificer','Bard','Cleric','Druid','Paladin','Ranger'])
detectMagic=Spell("Detect Magic",1,'''You can detect magic within 30 feet for Concentration max 10 mins, using your action to visualize auras and determine schools of magic after detecting the general presence.  The spell goes through solid matter, but only to a limited extent.''',["Artificer",'Bard','Cleric','Druid','Paladin','Ranger','Sorcerer','Wizard'])
disguiseSelf=Spell("Disguise Self",1,'''You can assume a disguise similar in physical form to you for 1 hour. It is a visual illusion''',['Artificer','Bard','Sorcerer','Wizard'])
expeditiousRetreat=Spell("Expeditious Retreat",1,'''Cast as a bonus action, you can Dash now and as a bonus action for Concentration max 10 mins.''',['Artificer','Bard','Sorcerer','Warlock','Wizard'])
faerieFire=Spell("Faerie Fire",1,'''Each object and every creature failing a Dex save in a 20' cube within 60' glows your choice of blue, green, or violet (dim light, 10' radius) for Concentration max 1 min.
Attackers have advantage against glowing things they see, and the glow renders invisibility moot.''',['Artificer','Bard','Druid','Ranger'])
falseLife=Spell("False Life",1,'''You get 1d4+4 temp hp''',['Artificer','Bard','Sorcerer','Wizard'])
featherFall=Spell("Feather Fall",1,'''You and up to 5 allies within 60 feet stop falling and slowly descend 60' per round for 1 minute.
The spell ends on a creature when they land.''',['Artificer','Bard','Sorcerer','Wizard'])
grease=Spell("Grease",1,'''cover 10' square within 60' in grease, forcing Dex saves v.s. falling prone on cast, entry, and turn end. Also difficult terrain.''',['Artificer','Bard','Wizard'])
identify=Spell("Identify",1,'''You can take a minute to learn the magic affecting an object or creature touched, including the full workings of a magical item''',['Artificer','Bard','Wizard'])
jump=Spell("Jump",1,'''You triple a creature's jump distance for 1 minute''',['Artificer','Bard','Druid','Ranger','Sorcerer','Wizard'])
longstrider=Spell("Longstrider",1,'''you give a creature +10ft speed for 1 hour''',['Artificer','Bard','Druid','Ranger','Wizard'])
purify=Spell("Purify Food and Drink",1,'''You cleanse food and drink in a 5' sphere''',['Artificer','Cleric','Druid','Paladin','Ranger'])
sanctuary=Spell("Sanctuary",1,'''As a bonus action, you protect a target within 30 feet for 1 min. Direct attackers must Wis save vs choosing a new target or losing the attack or spell.
If the warded creature makes an attack, casts a spell that affects an enemy, or deals damage to another creature, this spell ends.''',['Artificer','Cleric'])
badSnare=Spell("Lesser Snare",1,'''You can take 1 min to create an invisible magical trap in a 5' radius circle that lasts 8 hours from 25' of rope.
It can be detected with an Int(Investigation) check vs your save DC.
It hoists a Small-Large creature into the air upside down, restraining them, Dex save to negate.
Those trapped can escape with Dex saves or Int(Arcana) checks vs your spell save DC.''',['Artificer','Druid','Ranger','Wizard'])
goodSnare=Spell("Snare",1,'''You can take 1 min to create a permanent invisible magical trap in a 5' radius circle from 30' of rope.
It can be detected with an Int(Investigation) check vs your save DC.
It hoists a Small or larger creature into the air upside down, restraining them and applying the prone condition, Dex save to negate.
Those trapped can escape with Dex saves at disadvantage or an outside helper can use Int(Arcana) checks vs your spell save DC.''',['Druid','Ranger','Wizard'])
speakWithAnimals=Spell("Speak with Animals",1,'''You can verbally communicate with and understand beasts for the next 10 minutes''',['Druid','Ranger'])
causticBrew=Spell("Tasha's Caustic Brew",1,'''Shoot acid in a 30' by 5' line. Each creature in the line must make a Dex save or take 2d4 dmg/turn for Concentration max 1 min or until they use an action to clean it off.''',['Artificer'])

loader.append(beastSense)
loader.append(speakWithAnimals)
loader.append(alarm)
loader.append(catapult)
loader.append(absorbElements)
loader.append(cureWounds)
loader.append(detectMagic)
loader.append(disguiseSelf)
loader.append(expeditiousRetreat)
loader.append(faerieFire)
loader.append(falseLife)
loader.append(featherFall)
loader.append(grease)
loader.append(identify)
loader.append(jump)
loader.append(longstrider)
loader.append(purify)
loader.append(sanctuary)
loader.append(badSnare)
loader.append(goodSnare)
loader.append(causticBrew)    
for i in loader:
    spells[i.name]=i

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
            for i in range(0,max(basics.getMod(character.stats['int']),1)):
                character.addSpell(random.choice(j))
            character.saveString+='a'
            
