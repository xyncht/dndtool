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

def setCantrips(number, character):
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
    shockingGrasp=Spell("Shocking Grasp",0,'''Make a melee spell attack, with advantage if the target is wearing metal armor.
If you hit, deal '''+str(dict[character.level])+'''d8 lightning damage and the target loses its reaction.''',['Artificer','Bard','Sorcerer','Wizard'])
    spareTheDying=Spell("Spare the Dying",0,"You succeed on a Wis check to stabilize a target you touch.",['Artificer','Cleric','Ranger'])
    swordBurst=Spell("Sword Burst",0,"Everyone next to you must make a Dex save or take "+str(dict[character.level])+"d6 force damage.", ['Artificer','Sorcerer','Warlock','Wizard'])
    thornWhip=Spell("Thorn Whip",0,"Make a melee spell attack with range 30'.  You deal "+str(dict[character.level])+"d6 piercing damage on a hit and pull a Large or smaller target up to 10' towards you",['Artificer','Druid','Ranger'])
    thunderClap=Spell("Thunderclap",0,"Everyone next to you must make a Con save or take "+str(dict[character.level])+"d6 thunder damage. Also, you make a loud noise.", ['Artificer','Bard','Druid','Sorcerer','Warlock','Wizard'])

    roller=[]
    roller.append(acidSplash)
    roller.append(boomingBlade)
    roller.append(createBonfire)
    roller.append(dancingLights)
    roller.append(fireBolt)
    roller.append(frostBite)
    roller.append(greenFlameBlade)
    roller.append(guidance)
    roller.append(light)
    roller.append(lightningLure)
    roller.append(mageHand)
    roller.append(magicStone)
    roller.append(mending)
    roller.append(message)
    roller.append(poisonSpray)
    roller.append(prestidigitation)
    roller.append(rayOfFrost)
    roller.append(resistance)
    roller.append(shockingGrasp)
    roller.append(spareTheDying)
    roller.append(swordBurst)
    roller.append(thornWhip)
    roller.append(thunderClap)

    global spells
    cantrips={}
    for i in roller:
        spells[i.name]=i
        cantrips[i.name]=i

    present=[]
    for i in character.spells:
        if character.spells[i].spell.level==0:
            character.spells[i].spell=cantrips[i]
            present.append(i)
    while len(present)<number:
        j=random.choice(list(cantrips))
        if j not in present:
            character.addSpell(cantrips[j])
            present.append(j)
        

    
absorbElements=Spell("Absorb Elements",1,'''You can use your reaction to gain resistance to elemental damage you are about to take, and deal 1d6 extra damage of the triggering type on your first hit afterwards.''',['Artificer','Druid','Ranger','Sorcerer','Wizard'])
alarm=Spell("Alarm",1,'''You can take a minute to alarm a door, a window, or an area that is no larger than a 20-foot cube.
An alarm triggers whenever a creature not authorized during casting touches or enters the warded area for 8 hours.
The alarm is mental or audible, chosen when cast.

A mental alarm alerts and wakes you with 1 mile range.
An audible alarm rings like a hand bell for 10 seconds.''',['Artificer','Ranger','Wizard'])
catapult=Spell("Catapult",1,'''You can make one unattended object weighing 1 to 5 pounds within 60' blast up to 90 feet in a direction you choose.
It stops, dealing and taking 3d8 bludgeoning damage, if it hits something before then.
Creatures in the path must make a Dex save to avoid it''',['Artificer','Sorcerer','Wizard'])
cureWounds=Spell("Cure Wounds",1,'''You can heal 1d8 + your spell modifier hp via touch''',['Artificer','Bard','Cleric','Druid','Paladin','Ranger'])
detectMagic=Spell("Detect Magic",1,'''You can detect magic within 30 feet for Concentration max 10 mins, using your action to visualize auras and determine schools of magic after detecting the general presence.
The spell goes through solid matter, but only to a limited extent.''',["Artificer",'Bard','Cleric','Druid','Paladin','Ranger','Sorcerer','Wizard'])
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

beastSense=Spell("Beast Sense",2,'''For concentration max 1 hour, you can see and hear through a willing beast
you touch during casting, using its senses rather than your own.''',['Druid','Ranger'])


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
            character.saveString+='a'+up

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
                
                
            
            
        
            
