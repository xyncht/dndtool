import sys
import random
import math
import numpy
import os
import basics
import spells

classString='''1) Artificer
2) Barbarian
3) Bard
4) Cleric
5) Druid
6) Fighter
7) Monk
8) Mystic
9) Paladin
10) Ranger
11) Rogue
12) Sorcerer
13) Warlock
14) Wizard'''

def getMod(stat):
    if stat<10:
        stat-=1
    return int((stat-10)/2)

class Property:
    def __init__(self,nname,ttext='',vvalue=0):
        self.name=nname
        self.text=ttext
        self.value=vvalue

artificerSubclasses=['Alchemist','Armorer','Artillerist','Battle Smith']
barbarianSubclasses=["Wild Magic Barbarian","Zealot","Storm Herald","Berserker","Juggernaut","Ancestral Guardian","Bear Warrior","Eagle Warrior","Elk Warrior","Tiger Warrior","Wolf Warrior"]


def addRandomSkill(char,cclass):
    artificerSkills=['Arcana','History','Investigation','Medicine','Nature','Perception','Sleight of Hand']
    barbarianSkills=['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival']
    if cclass=='Artificer':
        sk1=random.choice(artificerSkills)
        while sk1 in char.proficiencies:
            sk1=random.choice(basics.skillList)            
        char.proficiencies.append(sk1)
    if cclass=='Barbarian':
        sk1=random.choice(barbarianSkills)
        while sk1 in char.proficiencies:
            sk1=random.choice(basics.skillList)            
        char.proficiencies.append(sk1)



def skillGen(char,key):
    
    if key in ['Artificer','Barbarian']: ##General skill gain
        for i in range (0,2):
            addRandomSkill(char,key)
            
    if key=='Artificer': ##Weird stuff
        if "Thieves' Tools" not in char.proficiencies:
            char.proficiencies.append("Thieves' Tools")
        else:
            sk1=random.choice(basics.trueToolsList)
            while sk1 in char.proficiencies:
                sk1=random.choice(basics.toolList)            
            char.proficiencies.append(sk1)
        if "Tinker's Tools" not in char.proficiencies:
            char.proficiencies.append("Tinker's Tools")
        else:
            sk1=random.choice(basics.artisanList)
            while sk1 in char.proficiencies:
                sk1=random.choice(basics.toolList)            
            char.proficiencies.append(sk1)
        sk1=random.choice(basics.artisanList)
        while sk1 in char.proficiencies:
            sk1=random.choice(basics.artisanList)
        char.proficiencies.append(sk1)
        
        
        
    
class Class:
    def __init__(self,nname='',hpdie="d8"):
        self.name=nname
        self.firstNameList={}
        self.lastNameList=[]
        self.hp=5
        if hpdie=="d10":
            self.hp+=1
        if hpdie=="d12":
            self.hp+=2
        if hpdie=="d6":
            self.hp-=1
    def featureGain(self,level,character,subclasses=['none']):  ##May still need to remove class features when changing characters
        return character
    def progress(self,char):
        self.featureGain(char.level,char,char.subclasses[0])
        char.refactor(self)

    def ArtificerGain(self,level,character,subclasses=['none']):
        def start(character):
            spells.makeSpellcaster(character,Artificer)
            spells.setCantrips(0,character)
            spells.setRituals(character)
            
        def learnInfusions(character):

            def getMagicItem(character,key):
                if isinstance(key,list):
                    findMode=True
                    clue=key[0]
                else:
                    key=int(key) #so it can take strings when desired
                    findMode=False
                itemList={}
                text="You can make "
                itemList[1]= '''an Alchemy Jug, capable of producing 1
of the following, once per day:

- 8 ounces Acid
- 1/2 ounce basic poison
- 4 gallons of Beer
- 1 gallon of honey
- 2 gallons of mayonnaise
- 1 quart of oil
- 2 gallons of vinegar
- 8 gallons of fresh water
- 12 gallons of salt water
- 1 gallon of wine

You don't have to produce it all at once, but you can't change the
kind of liquid after you start for a given day.'''
                itemList[2]='''a Bag of Holding, capable of holding up to 500 pounds,
not exceeding a volume of 64 cubic feet, and weighing only 15 pounds.
Retrieving an item from the bag takes an action.

If the bag is overloaded, pierced, or torn its contents are scattered across the Astral Plane.
The bag holds enough air for 1 creature to survive for 10 mintes or a number of creatures
to survive for a proportionate fraction thereof.

The bag can be combined with a portable hole or haversack to create a rift that pulls everything
within 10' into a random spot on the Astral Plane, no save, and then closes, destroying both items.'''
                itemList[3]='''a Cap of Water Breathing'''
                itemList[4]='''Goggles of Night, which grant or improve darkvision'''
                itemList[5]='''Rope of Climbing, which is an animate rope-snake that obeys your will.
It's helpful for climbing, also.'''
                itemList[6]='''a pair of Sending Stones, which let either bearer cast Sending
1/day targeting the bearer of the other stone and doesn't get wasted if there is no other bearer.'''
                itemList[7]='''a Wand of Detect Magic,
which has 3 charges and lets you cast Detect Magic using a charge.
It regains 1d3 charges daily at dawn'''
                itemList[8]='''a Wand of Secrets,
which has 3 charges and lets you automatically find the nearest secret door or trap within 30'
at the cost of a charge. It regains 1d3 charges at dawn.'''
                itemList[9]='''a pair of Boots of Elvenkind, which make your movement silent.
They also grant advantage on Dexterity(stealth) checks where that is useful.'''
                itemList[10]='''a Cloak of Elvenkind, which requires attunement.
It grants you advantage on all Dexterity(stealth) checks,
and imposes disadvantage on Wisdom(Perception) checks against you the rely on sight.

It can be temporarily disabled by pulling down the hood, which takes an action to do or undo.'''
                itemList[11]='''a Cloak of the Manta Ray, which grants you
60' swim speed and water breathing.  It can be disabled by pulling the hood down
which takes an action to do or undo.'''
                itemList[12]='''a pair of Eyes of Charming, which have 3 charges.
They require attunement.
They allow you to cast Charm Person using a charge on a target that you can see
and who can see you.
They regain all charges at dawn.'''
                itemList[13]='''an invisible pair of Gloves of Thievery.
They turn visible when not worn.
They grant a +5 bonus on Dex (sleight of hand) checks.
They grant a +5 bonus on Dex checks to pick locks.'''
                itemList[14]='''a Lantern of Revealing, which functions as an ordinary
hooded lantern, but renders the invisible visible within its bright light.'''
                itemList[15]='''Pipes of Haunting, which have three charges.
The pipes allow a proficient player to expend a charge and render all creatures within 30'
frightened (DC 15 Wis negates).
You can allow non-hostiles to autosucceed the save, as a group.
Frightened creatures can repeat the save and the end of each turn.
The fear ends after 1 minute if not sooner.
Once a creature makes its save, it is immune for 24 hours.
The pipes regain 1d3 charges each dawn.'''
                itemList[16]='''a Ring of Water Walking, which lets you walk on any liquid as if it were solid ground.'''
                ### Need to add the rest for 10th level and higher

                if not findMode:
                    if key == 0:
                        if character.level<5:
                            pick=random.choice(range(1,9))
                        elif character.level<10:
                            pick=random.choice(range(1,17))
                        else:
                            raise "Not ready!"
                        text=text+itemList[pick]
                        return [text,pick]
                    else:
                        return [text+itemList[key],key]
                else:
                    for i in itemList:
                        if text+itemList[i]==clue:
                            return i




            ## Make a list of all infusions        
            chain=[]
            strArmor=Property("Armor of Magical Strength",'''Give armor 6 charges.
When making a Strength check or save, wearer can expend 1 charge to get +Int
If armor would be knocked prone, wearer can use its reaction to expend 1 charge instead.
Requires attunement and regains 1d6 charges at dawn.''')
            chain.append(strArmor)
            enFocus=Property("Enhanced Arcane Focus",'''Give a rod magic that increases the user's spell attack rolls by '''+str(1+int((character.level>9)))+'''.
It also allows the wielder to bypass half cover and all lesser cover.
It requires attunement.''')
            chain.append(enFocus)
            enDefense=Property("Enhanced Defense","Enchant armor or shield to provide +"+str(1+int((character.level>9)))+" AC")
            chain.append(enDefense)
            enWeapon=Property("Enhanced Weapon","Enchant an object for +"+str(1+int((character.level>9)))+" to attack and damage")
            chain.append(enWeapon)
            homunculus=Property("Homunculus Servant",'''Create a homuculus around a semiprecious gem.
The homunculus is a tiny construct that can fly and walk. You choose the homunculus's appearance details.
It has stats that depend on yours and can fire force spikes up to 30' as an action.
It can also use its reaction to deliver touch range spells for you if it is within 120'

It is friendly to you and your companions and obeys your commands.
It heals 2d4 hp from the Mending spell.
It can't take Actions except Dodge unless you sacrifice your bonus action on a turn if you aren't incapacitated.
It takes its turn immediately after yours.
If you or it dies, it vanishes and drops the heart.

It has '''+str(character.level+getMod(character.stats['int'])+1)+" hit points.")
            chain.append(homunculus)
            mindSharpener=Property("Mind Sharpener",'''You can enchant clothing or armor to have 4 charges.
The wearer can use a charge to succeed on a Concetration check instead of failing, after making the roll.
It regains 1d4 charges at dawn''')
            chain.append(mindSharpener)
            repeatingShot=Property("Repeating Shot",'''You can enchant a weapon that uses ammunition.
It gets +1 to hit and damage.
It ignores the loading property-- a user can reload it instantly as a free action.
A wielder can choose to shoot magic ammunition created by the weapon instead of actual ammo if they wish.
If they do, the magic ammo vanishes after use.
The weapon requires attunement.''')
            chain.append(repeatingShot)
            replicateMagicItem1=Property("Replicate First Magic Item","")
            replicateMagicItem2=Property("Replicate Second Magic Item",'')
            replicateMagicItem0=Property("Replicate Zeroth Magic Item",'')
            replicateMagicItem=Property("Replicate Another Magic Item",'')
            chain.append(replicateMagicItem0)
            chain.append(replicateMagicItem)
            chain.append(replicateMagicItem1)
            chain.append(replicateMagicItem2)
            returningWeapon=Property("Returning Weapon","A throwable weapon gets +1 to hit and damage. \nIf it is thrown it reappears in the users hands after the attack")
            chain.append(returningWeapon)
            if character.level>5:
                replicateMagicItem3=Property("Replicate Third Magic Item","")
                replicateMagicItem4=Property("Replicate Fourth Magic Item","")
                chain.append(replicateMagicItem3)
                chain.append(replicateMagicItem4)
                bootsW=Property("Boots of the Winding Path","Wearer can teleport up to 15' as a bonus action to a space they can see that they were at within the current round.\nRequires Attunement")
                chain.append(bootsW)
                radiantW=Property("Radiant Weapon",'''Give 4 charges to a weapon.
The weapon requires attunement.
The weapon gets +1 to hit and damage.
The weapon can be turned on and off as a bonus action.
While 'on' it sheds bright light in 30' and dim light in 30'.
Wielder can use 1 charge to blind attacker as a reaction to being hit, DC '''+str(getMod(character.stats['int'])+8+character.proficiency)+''' Con save negates.
The triggering attack need not be melee and there is no range limitation.''')
                chain.append(radiantW)
                repulShield=Property("Repulsion Shield",'''A shield gains +1 AC and 4 charges.
It requires attunement.
The wielder can use their reaction and 1 charge to push a successful melee attacker back 15'.
The shield regains 1d4 charges at dawn.''')
                chain.append(repulShield)
                resisArm=Property("Resistant Armor","Armor grants resistance to an element of your choice.  \nIt requires attunement.")
                chain.append(resisArm)
                spellRing=Property("Spell-Refueling Ring",'''Grant 1 charge to a ring.
The wearer can use a charge to regain a spell slot of 3rd level or lower.
The ring requires attunement.
The ring regains 1 charge at dawn.''')
                chain.append(spellRing)
                if character.level>9:
                    replicateMagicItem5=Property("Replicate Fifth Magic Item",'')
                    replicateMagicItem6=Property("Replicate Sixth Magic Item",'')
                    chain.append(replicateMagicItem5)
                    chain.append(replicateMagicItem6)
                    helmAw=Property("Helm of Awareness","Helmet grants advantage on initiative rolls and prevents suprise.\nRequires attunement.")
                    chain.append(helmAW)
                    if character.level>13:
                        replicateMagicItem7=Property("Replicate Seventh Magic Item",'')
                        chain.append(replicateMagicItem7)
                        replicateMagicItem8=Property("Replicate Eigth Magic Item",'')
                        chain.append(replicateMagicItem8)
                        arcArmor=Property("Arcane Propulsion Armor",'''You enchant armor to require attunement.  It gains:
- +5 ft walking speed
- magic rocket punch gauntlets that deal 1d8 force damage on melee attack or ranged attack hit at range 20'/60'
- proficiency in rocket punches
- can't be removed against wearer's will
- If the wearer is missing limbs, the armor magically replaces them with prosthetics while worn''')
                        chain.append(arcArmor)
                        if character.level>17:
                            replicateMagicItem9=Property("Replicate Ninth Magic Item",'')
                            chain.append(replicateMagicItem9)
                            replicateMagicItem10=Property("Replicate Tenth Magic Item",'')
                            chain.append(replicateMagicItem10)
            
            ##load old infusions
            if 'inf' in character.saveString:
                code=character.saveString
                i=0
                done=False
                while not done:
                    if code[0]=='i':
                        if code[1]=='n':
                            if code[2]=='f':
                                done=True
                                key1=i
                            else:
                                i+=1
                                code=code[1:]
                        else:
                            i+=1
                            code=code[1:]
                    else:
                        i+=1
                        code=code[1:]
                code=character.saveString[key1+3:]

                i=3
                done=False
                while not done:
                    if code[0] in '1234567890.':
                        i+=1
                        code=code[1:]
                    else:
                        done=True
                        key2=i
                    if len(code)==0:
                        done=True
                        key2=i

                        
                oldString=character.saveString[key1+3:key1+key2]


                ddone=False
                while not ddone:
                    item=False
                    thisOne=""
                    done=False
                    while not done:
                        if oldString[0]=='.':
                            done=True
                            oldString=oldString[1:]
                            if oldString[0]=='.':
                                ddone=True
                        else:
                            thisOne+=oldString[0]
                            oldString=oldString[1:]
                    if '999' in thisOne:
                        item=True
                        if thisOne[0]=='9':
                            push=1
                            thisOne='8'+thisOne[1:]
                        else:
                            push=0
                        both=thisOne.split("999")
                        thisOne=both[0]
                        itemKey=both[1]
                        if push==1:
                            if len(thisOne)>1:
                                thisOne='9'+thisOne[1:]
                            else:
                                thisOne='9'
                    
                    if not item:
                        character.addProperty(chain[int(thisOne)])
                    else:
                        get=getMagicItem(character,int(itemKey))
                        chain[int(thisOne)].text=get[0]
                        character.addProperty(chain[int(thisOne)])


           

                            
            infMap={}
            for i in range(2,21):
                if i<6:
                    infMap[i]=4
                elif i<10:
                    infMap[i]=6
                elif i<14:
                    infMap[i]=8
                elif i<18:
                    infMap[i]=10
                else:
                    infMap[i]=12

                    
            target=infMap[character.level]
            current=[]
            sHelper=[]
            for i in character.properties:
                nameList={}
                for k in chain:
                        nameList[k.name]=k
                if i in nameList:
                    current.append(character.properties[i])
                    sHelper.append(chain.index(nameList[i]))
                    if 'Replicate' in character.properties[i].name:
                        sHelper[-1]=int(str(sHelper[-1])+'999'+str(getMagicItem(character,[character.properties[i].text])))
                    
            infString="inf"
            for i in sHelper:
                infString+=str(i)+'.'
            
            while target>len(current):
                
                choose=random.choice(chain)
                if choose not in current:
                    infString+=str(chain.index(choose))
                    current.append(choose)
                    if 'Replicate' in choose.name:
                        item=getMagicItem(character,0)
                        choose.text=item[0]
                        infString+='999'+str(item[1])
                        
                        
                    infString+='.'    
                    character.addProperty(choose)
                    
            infString+='.' #terminal '.'
            
            if 'inf' in character.saveString:
                code=character.saveString
                i=0
                done=False
                while not done:
                    if code[0]=='i':
                        if code[1]=='n':
                            if code[2]=='f':
                                done=True
                                key1=i
                            else:
                                i+=1
                                code=code[1:]
                        else:
                            i+=1
                            code=code[1:]
                    else:
                        i+=1
                        code=code[1:]
                code=character.saveString[key1+3:]

                i=3
                done=False
                while not done:
                    if code[0] in '1234567890.':
                        i+=1
                        code=code[1:]
                    else:
                        done=True
                        key2=i
                    if len(code)==0:
                        done=True
                        key2=i
                    
                character.saveString=character.saveString[0:key1]+infString+character.saveString[key1+key2:]
            else:
                character.saveString+=infString

        if level==1:
            mTinker=Property("Magical Tinkering",'''You can touch a Tiny nonmagical object with thieves' or artisan's tools as an action to give it one of the following properties, or end the effect:

    - The object sheds bright light in a 5-foot radius and dim light for an additional 5 feet.
    - Whenever tapped by a creature, the object emits a recorded message that can be heard up to 10 feet away. You utter the message when you bestow this property on the object, and the recording can be no more than 6 seconds long.
    - The object continuously emits your choice of an odor or a nonverbal sound (wind, waves, chirping, or the like). The chosen phenomenon is perceivable up to 10 feet away.
    - A static visual effect appears on one of the object's surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like.

Max 1 effect/object. Max '''+str(max(getMod(character.stats['int']),1))+" object at once before new ones replace the oldest.")
            guns=Property("Firearm Proficiency","You are proficient with firearms")
            character.addProperty(guns)
            character.addProperty(mTinker)
            start(character)
            spells.setCantrips(2,character)
        if level==2:
            start(character)
            table={}
            for i in range(0,21):
                if i<6:
                    table[i]=2
                elif i<10:
                    table[i]=3
                elif i<14:
                    table[i]=4
                elif i<18:
                    table[i]=5
                else:
                    table[i]=6
            infusions=Property("Infuse Item",'''When you end a long rest, you may imbue up to '''+str(table[character.level])+ ''' non-magical objects with magic.
 You may attune yourself to them the instant you infuse the items.
The magic lasts till you die and for '''+str(max(character.stats['int'],1))+''' days thereafter.
The infusion also vanishes if you give up your knowledge of an infusion for another.

Each of your infusions can be in only one object at a time and each object can only hold one infusion at a time.
If you try to exceed your maximum number of infusions, the oldest infusion immediately ends, and then the new infusion applies.
If an infusion ends on an item that contains other things, like a bag of holding, its contents harmlessly appear in and around its space.''')
            character.addProperty(infusions)
            learnInfusions(character)

        if level==3:
            start(character)
            sb='none'
            new=False
            for i in character.subclasses: #Check subclass
                if i in artificerSubclasses:
                    sb=i
            if sb=='none': #Assign
                sb=random.choice(artificerSubclasses)
                character.subclasses.append(sb)
                if character.subclasses[0]=='none':
                    character.subclasses=character.subclasses[1:]
                new=True
            if sb=='Alchemist':
                if new:
                    sk1='Alchemist\'s Supplies'
                    while sk1 in character.proficiencies:
                        sk1=random.choice(basics.artisanList)
                    character.proficiencies.append(sk1)
                character.addSpell(spells.spells["Healing Word"],'always available',1)
                character.addSpell(spells.spells["Ray of Sickness"],'always available',1)
                expElix=Property('Experimental Elixir','''You make an elixir with Alchemist's Supplies each long rest. It has one of the following effects, at random:
- Heal 2d4+'''+str(basics.getMod(character.stats['int']))+''' hp
- Walking speed increases by 10' for 1 hour
- +1 AC for 10 minutes
- + 1d4 to every attack roll and save for one minute
- 10' fly speed for 10 minutes.
- Replicate Alter Self with 10 minute duration (no concentration)

As an action, a creature can drink the elixir or administer it to an incapacitated creature.
It lasts until the next long rest or until consumed.

You can sacrifice spell slots to create additional elixirs at any time-- 1 elixir per spell slot regardless of level.
When you do so, you use your action to create the elixir in an empty flask you touch,
and you choose the elixir's effect rather than rolling.''')
                character.addProperty(expElix)
            if sb=='Armorer':
                if 'Heavy Armor' not in character.proficiencies:
                    character.proficiencies.append('Heavy Armor')
                if new:
                    sk1='Smith\'s Tools'
                    while sk1 in character.proficiencies:
                        sk1=random.choice(basics.artisanList)
                    character.proficiencies.append(sk1)
                character.addSpell(spells.spells["Magic Missile"],'always available',1)
                character.addSpell(spells.spells["Thunderwave"],'always available',1)
                aArmor=Property("Arcane Armor",'''As an action, you can enchant your armor with Smith's Tools.

You gain the following benefits while wearing this armor:

- If the armor normally has a Strength requirement, the arcane armor lacks this requirement for you.
- You can use the arcane armor as a spellcasting focus for your artificer spells.
- The armor attaches to you and can't be removed against your will.
- It expands to cover your entire body.
- The armor replaces any missing limbs, functioning identically to a limb it replaces.
- You can retract or deploy the helmet as a bonus action
- You can doff or don the armor as an action.

The armor continues to be Arcane Armor until you don another suit of armor or you die.''')
                character.addProperty(aArmor)
                if new:
                    model=random.choice([0,1])
                    if model==0:
                        character.saveString+='I'
                if 'I' in character.saveString:
                    armorMod=Property("Armor Model: Infiltrator",''' 
You can use your armor to make weapon attacks with Int with range of 90'/300', dealing 1d6 lightning damage.
You can add your Int to the damage in place of Dex.

1/turn, you can deal an extra 1d6 lightning damage on a hit with that attack.

Your walking speed increases by 5 feet.

You have advantage on Dexterity (Stealth) checks.''')
                else:
                    armorMod=Property("Armor Model: Guardian",'''
You can make melee attacks with your armor using Int instead of Str, dealing 1d8 thunder damage.
On hit, target has disadvantage on attacks against targets other than you until the start of your next turn

As a bonus action, you can lose all temp hp you have and gain '''+str(character.level)+''' temp hp instead.
You lose these temporary hit points if you doff the armor.
You can use this bonus action '''+str(character.proficiency)+" times per long rest.")
                character.addProperty(armorMod)
            if sb=="Artillerist":
                if new:
                    sk1='Woodcarver\'s Tools'
                    while sk1 in character.proficiencies:
                        sk1=random.choice(basics.artisanList)
                    character.proficiencies.append(sk1)
                character.addSpell(spells.spells["Shield"],'always available',1)
                character.addSpell(spells.spells["Thunderwave"],'always available',1)
                eldCannon=Property("Eldritch Cannon",'''You can using woodcarver's tools or smith's tools to magically create a Small or Tiny eldritch cannon on flat empty ground next to you as an action.
A Small eldritch cannon occupies its space, and a Tiny one can be held in one hand.
You get 1 free cannon per long rest, plus you regain the ability to create a cannon each time you expend a spell slot.
You can have only one cannon at a time and can't create one while you have one.

The cannon is a magical object. Regardless of size, the cannon has 18 AC and '''+str(character.level*5)+''' hp.
It is immune to poison damage and psychic damage, and all conditions.
If it is forced to make an ability check or a saving throw, treat all its ability scores as 10 (+0).
If the mending spell is cast on it, it regains 2d6 hit points.
It disappears if it is reduced to 0 hit points or after 1 hour. You can dismiss it early as an action.

When you create the cannon, you determine its appearance and whether it has legs. You also decide which type it is.
On each of your turns, you can take a bonus action to cause the cannon to activate if you are within 60 feet of it.
As part of the same bonus action, you can direct the cannon to walk or climb up to 15 feet to an unoccupied space, provided it has legs.

The type of the cannon determines what happens when you activate it:

Flamethrower	The cannon blasts an adjacent 15-foot cone.
                Each creature there takes 2d8 fire damage, DC '''+str(getMod(character.stats['int'])+8+character.proficiency)+''' Dex save for half.
                The fire ignites any flammable objects in the area that aren't being worn or carried.
                
Force Ballista	Make a ranged spell attack for 2d8 force damage, originating from the cannon, at a target within 120'.
                If you hit a creature, it is pushed 5' away.
                
Protector	The cannon grants itself and each creature of your choice within 10' of it 1d8+'''+str(max(1,character.stats['int']))+" temp hp.")
                character.addProperty(eldCannon)
            if sb=="Battle Smith":
                if new:
                    sk1='Smith\'s Tools'
                    while sk1 in character.proficiencies:
                        sk1=random.choice(basics.artisanList)
                    character.proficiencies.append(sk1)
                character.addSpell(spells.spells["Shield"],'always available',1)
                character.addSpell(spells.spells["Heroism"],'always available',1)
                battleReady=Property("Battle Ready","You can use Int instead of Str or Dex for attack and damage rolls with magic weapons")
                character.addProperty(battleReady)
                if 'All Martial Weapons' not in character.proficiencies:
                    character.proficiencies.append('All Martial Weapons')
                steelDef=Property("Steel Defender",'''You have a golem companion. It is friendly to you and your companions, and it obeys your commands.

The defender takes its turn immediately after you on the save initiative count.
The only Action it can take is Dodge, unless you sacrifice a bonus action on your turn.
If you are incapacitated, the defender can take any action of its choice, not just Dodge.

It is immune to surprise.
If the mending spell is cast on it, it regains 2d6 hit points.
If it has died within the last hour, you can use your smith's tools as an action to revive it, provided you are within 5 feet of it and you expend a spell slot of 1st level or higher.
The steel defender returns to life after 1 minute with all its hit points restored.

At the end of a long rest, you can create a new steel defender if you have your smith's tools with you.
If you already have a steel defender from this feature, the first one immediately perishes.
The defender also perishes if you die.

It has '''+str(2+character.stats['int']+5*character.level)+''' hp and 15 AC.''')
                character.addProperty(steelDef)
            rightTool=Property("The Right Tool for the Job",'''You can create artisan's tools of any kind ex nihilo using thieves' or artisan's tools and 1 hour.
You can do this work as part of a long or short rest without it counting as any kind of interruption, even to sleep.
The tools so created are non-magical, but have several "non-magical" properties:

- you can cause them to cease existing at any time
- they cease existing if you begin using this feature again''')
            character.addProperty(rightTool)
                
                
        return character
    def BarbarianGain(cclass,level,character,subclasses=['none']):
        if level==1:
            rage=Property("Rage",'''In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action. While raging, you gain the following benefits if you aren't wearing heavy armor:
    - You have advantage on Strength checks and Strength saving throws.
    - When you make a melee weapon attack using Strength, you gain a +2 bonus to the damage roll.
    - You have resistance to bludgeoning, piercing, and slashing damage.

    Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then.
    You can also end your rage on your turn as a bonus action.

    Once you have raged twice, you must finish a long rest before you can rage again.''')
            if getMod(character.stats['con'])>0:
                armor=Property('Unarmored Defense','''While you are not wearing armor, your Armor Class is '''+str(10 + getMod(character.stats['dex']) + getMod(character.stats['con']))+'.')
                character.addProperty(armor)
            character.addProperty(rage)
            return character
        elif level==2:
            dSense=Property("Danger Sense",'''You have advantage on Dexterity saving throws against effects that you can see, such as traps and spells''')
            reckless=Property("Reckless Attack",'''When you make your first attack on your turn, you can decide to attack recklessly.
Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.''')
            character.addProperty(dSense)
            character.addProperty(reckless)
            return character
        elif level==3:
            sb='none'
            new=False
            rage=Property("Rage",'''In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action. While raging, you gain the following benefits if you aren't wearing heavy armor:
    - You have advantage on Strength checks and Strength saving throws.
    - When you make a melee weapon attack using Strength, you gain a +2 bonus to the damage roll.
    - You have resistance to bludgeoning, piercing, and slashing damage.

    Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then.
    You can also end your rage on your turn as a bonus action.

    Once you have raged thrice, you must finish a long rest before you can rage again.''',1)
            character.addProperty(rage)
            for i in character.subclasses: #Check subclass
                if i in barbarianSubclasses:
                    sb=i
            if sb=='none':
                sb=random.choice(barbarianSubclasses)
                character.subclasses.append(sb)
                if character.subclasses[0]=='none':
                    character.subclasses=character.subclasses[1:]
                new=True
            if sb=="Ancestral Guardian":
                aGuard=Property("Ancestral Protectors",'''While you're raging, the first creature you hit with an attack on your turn becomes the target of spirits which hinder its attacks.
Until the start of your next turn, they have disadvantage on any attack roll that isn't against you, and when they hit a creature other than you with an attack, that creature has resistance to the damage dealt by the attack.
The effect on the target ends early if your rage ends.''')
                character.addProperty(aGuard)
            if sb=="Berserker":
                frenzy=Property("Frenzy",'''You can go into a frenzy when you rage.
If you do so, for the duration of your rage you can make a single melee weapon attack as a bonus action on each of your turns after this one.
When your rage ends, you suffer one level of exhaustion.''')
                character.addProperty(frenzy)
            if sb=="Juggernaut":
                tBlows=Property("Thunderous Blows",'''When you hit a creature with a melee attack while you're raging, you can push that creature up to 5 feet away from you in a direction of your choice.
A creature that is Huge or larger makes a DC '''+str(getMod(character.stats['str'])+8+character.proficiency)+''' Strength save. On a success, the creature is not pushed.''')
                spMountain=Property("Spirit of the Mountain",'''While you are raging, you can't be knocked prone or moved along the ground against your will.''')
                character.addProperty(tBlows)
                character.addProperty(spMountain)
            if sb=="Storm Herald":
                if new: ##should change every level maybe
                    die=random.choice(['T','t',''])
                    character.saveString+=die
                if 't' in character.saveString:
                    sAura=Property("Storm Aura",'''When you rage, or as a bonus action while doing so, all other creatures within 10 feet take 2 fire damage each.''')
                elif 'T' not in character.saveString:
                    sAura=Property("Storm Aura",'''When you rage, or as a bonus action while doing so, you can strike one creature you can see within 10 feet. They take 1d6 lightning damage, DC '''+str(8+character.proficiency+getMod(character.stats['con']))+" Dex save for half")
                else:
                    sAura=Property("Storm Aura",'''When you rage, or as a bonus action while doing so, each creature of your choice within 10 feet gains 2 temporary hit points''')
                character.addProperty(sAura)
            if sb=="Zealot":
                if new:
                    flip=random.choice[1,0]
                    if flip:
                        character.saveString+='r'
                if 'r' in character.saveString:
                    word='radiant'
                else:
                    word='necrotic'
                dFury=Property("Divine Fury","While raging, your first successful weapon attack each turn deals 1d6 + "+str(int(character.level/2))+" extra "+word+" damage.")
                character.addProperty(dFury)
                zeal=Property("Warrior of the Gods","If a spell restores you to life, the caster doesn't need material components")
                character.addProperty(zeal)
            if 'Warrior' in sb:
                character.addSpell(spells.spells["Beast Sense"],'ritual only',-1)
                character.addSpell(spells.spells["Speak with Animals"],'ritual only',-1)
                if 'Elk' in sb:
                    tSpirit=Property("Totem Spirit","While raging not in heavy armor, your land speed increases by 15 feet")
                if 'Wolf' in sb:
                    tSpirit=Property("Totem Spirit","While raging even in heavy armor, your allies have advantage on melee attacks against enemies within 5 feet of you")
                if 'Bear' in sb:
                    tSpirit=Property("Totem Spirit","While raging even in heavy armor, you have resistance to all non-psychic damage")
                if 'Tiger' in sb:
                    tSpirit=Property("Totem Spirit","While raging even in heavy armor, you can jump +10 feet far and +3 feet high")
                if 'Eagle' in sb:
                    tSpirit=Property("Totem Spirit","While raging not in heavy armor, enemies have disadvantage on opportunity attacks against you, and you can Dash as a bonus action")
                character.addProperty(tSpirit)
            if 'Wild Magic Barbarian'==sb:
                mSense=Property("Magic Awareness",'''As an action, you can sense magic. Until the end of your next turn, you know the location of any spell or magic item within 60 feet without total cover.
When you sense a spell, you learn which school of magic it belongs to. You can use this feature '''+str(character.proficiency)+''' times per long rest.''')
                wbSurge=Property("Wild Surge","When you enter your rage, roll a d8 on the Wild Magic table to determine the magical effect produced, all of which are beneficial.")
                character.addProperty(wbSurge)
                character.addProperty(mSense)
            return character
        return character
                

  

classList=[]

Wizard=Class("Wizard","d6")
Fighter=Class("Fighter","d10")
Barbarian=Class("Barbarian","d12")
Monk=Class("Monk","d8")
Rogue=Class("Rogue","d8")
Druid=Class("Druid","d8")
Ranger=Class("Ranger","d10")
Bard=Class("Bard","d8")
Cleric=Class("Cleric","d8")
Paladin=Class("Paladin","d10")
Sorcerer=Class("Sorcerer","d6")
Warlock=Class("Warlock","d8")
Artificer=Class("Artificer","d8")
Artificer.spellStat='int'
Mystic=Class("Mystic","d8")
classList.append(Artificer)
classList.append(Barbarian)
classList.append(Bard)
classList.append(Cleric)
classList.append(Druid)
classList.append(Fighter)
classList.append(Monk)
classList.append(Mystic)
classList.append(Paladin)
classList.append(Ranger)
classList.append(Rogue)
classList.append(Sorcerer)
classList.append(Warlock)
classList.append(Wizard)


import classNames

Barbarian.featureGain=Barbarian.BarbarianGain
Artificer.featureGain=Artificer.ArtificerGain

def classLookup(nname):
    if '/' not in nname:
        for i in classList:
            if i.name==nname:
                return [i]
        if nname in barbarianSubclasses:
            return classLookup("Barbarian")
        if nname in ["Evoker","Necromancer"]:
            return classLookup("Wizard")
    else:
        raise "D: D: not ready!!!"
