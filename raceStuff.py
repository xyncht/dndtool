import basics
import random
import copy
import classStuff
import spells

class Race:
    def __init__(self,nname=''):
        self.name=nname
        self.properties={}
        self.firstNameList={}
        self.lastNameList=[]
    def addProperty(self,nname,kkind,vvalue=0,llevel=1):
        bbreak=0
        for i in self.properties:
            if i==nname:
                raise Exception("property already exists: \""+nname+"\"")
                bbreak=1
        if not bbreak:
            self.properties.append(nname,Property(nname,kkind,vvalue,llevel))
    def addProperty(self,property):
        bbreak=0
        for i in self.properties:
            if i==property.name:
                raise Exception("property already exists: \""+property.name+"\"")
                bbreak=1
        if not bbreak:
            self.properties.append(property.name,property)
    def makeRace(self,character,new=True):
        if self.name=="Human":
            global humanSubraces
            sub=copy.copy(self)
            sub.name=random.choice(humanSubraces)
            character.race=sub
            
        elif self.name=="Elf":
            global elfSubraces
            sub=copy.copy(self)
            sub.name=random.choice(elfSubraces)
            character.race=sub

        if character.race.name=="Lesser Human":
            if new:
                for i in character.stats:
                    character.stats[i]+=1
        if character.race.name=="High Elf":
            makeElf(character,new)
            makeBaseHighElf(character,new)
        if character.race.name=="Astral Elf":
            makeAstralElf(character,new)
        if character.race.name=="Avariel":
            makeElf(character,new)
            makeAvariel(character,new)
        if character.race.name=="Drow":
            makeElf(character,new)
            makeDrow(character,new)
        if character.race.name=="Variant Eladrin":
            makeElf(character,new)
            makeUAEladrin(character,new)
        if character.race.name=="Lesser Eladrin":
            makeElf(character,new)
            makeDMGEladrin(character,new)
        if character.race.name=="Eladrin":
            makeElf(character,new)
            makeMTFEladrin(character,new)
        if character.race.name=="Grugach":
            makeElf(character,new)
            makeGrugach(character,new)
        if character.race.name=="Valenar Eladrin":
            makeElf(character,new)
            makeDMGEladrin(character,new)
            makeValenar(character,new)
        if character.race.name=="Aereni Eladrin":
            makeElf(character,new)
            makeDMGEladrin(character,new)
            makeAereni(character,new)
        if character.race.name=="Valenar High Elf":
            makeElf(character,new)
            makeBaseHighElf(character,new)
            makeValenar(character,new)
        if character.race.name=="Aereni High Elf":
            makeElf(character,new)
            makeBaseHighElf(character,new)
            makeAereni(character,new)
        if character.race.name in ['Wood Elf','Bishatar Elf','Tirahar Elf']:
            makeElf(character,new)
            makeWoodElf(character,new)
        if character.race.name=="Vahadar Elf":
            makeElf(character,new)
            makeVahadar(character,new)
        if character.race.name=="Mark of Shadow Elf":
            makeElf(character,new)
            makeMarkofShadow(character,new)
        
Human=Race("Human")
Elf=Race("Elf")
#Dwarf=Race("Dwarf")
#Gnome=Race("Gnome")
#Half-Ork=Race("Half-Ork")
#Halfling=Race("Halfling")
#Tiefling
#Dragonborn
#Goliath
#Aasimar

raceList=[]
raceList.append(Human)
raceList.append(Elf)
##raceList.append(Dwarf)
##raceList.append(Gnome)
##raceList.append(Half-Ork)
##raceList.append(Halfling)




Human.firstNameList={"Male":["Bart","Dmitri","Vassily","Arthur","Steve","John","Jack","Michael","Bert","Ernesto","Ulrich","Vladomir","Patrick","George","Pafnuty","Cyril","Ping","Abe","Jin","Tsu","Suh","Ivan","Boris","Gregor","Franz","Wilhelm","Otis","Evan","Able","Isaac","Abraham","Jacob","Moses","Anaxamenes","Raila","Oginga","Agwambo"],"Female":["Susan","Samantha","Xena","Ximena","Jane","Mildred","Minerva","Miranda","Karla","Olga","Hilda","Heidi","Brunhilde","Vasolina","Ana","Adelheld","Janet","Rose","Estrella","Isabella","Esperanza","Innessa","Natalya","Larisa","Agrafena","Alina","Inga","Ingrid","Augusta","Valerie","Aoi","Aiko","Fumiko","Chiyo","Bai","Chen","Baozhai","Enya","Soo yun","Hana","Gyeong","Chuki","Bishara","Aanuoluwakiishi","Diekololaoluwa","Ayotunde","Pippi","Teicuih","Tlazohtzin"]}
Human.lastNameList=["Oruba","Ramaposa","Mbumba","Katsyv","Chebyshev","the Black","the Red","the Fair","the Brown","the Grey","the White","White","Black","Fisher","Book","Carpenter","Shepard","Roaver","Wheeler","Carter","Keeper","Beesly","Smith","Downe","Hoover","Rodriguez","Fernandez","Cervantes","O'Reily","O'Toole","O'Mally","O'Loxly","Anand"]
Human.abilityMods={}

###Start Knat Chat GPT stuff
def generate_elven_name():
    prefixes = ["Ae", "Lir", "Tha", "Elen", "Gal", "Ar", "Lor", "Sil", "Cae", "Fin"]
    midfixes = ["r", "th", "l", "rion", "en", "ion", "ia", "on", "el", "a"]
    mid_midfixes = ["aer", "eth", "ith", "rae", "yra", "ele", "ano", "lia", "ara", "quen"]
    suffixes = ["th", "el", "ion", "or", "ias", "en", "ra", "iel", "on", "il"]

    generated_name = (
        random.choice(prefixes)
        + random.choice(midfixes)
        + random.choice(mid_midfixes)
        + random.choice(suffixes)
    )
    return generated_name.capitalize()


Elf.firstNameList={"Male":generate_elven_name(), "Female":generate_elven_name()}
Elf.lastNameList=[generate_elven_name()]


##def generate_dwarven_name():
##    prefixes = ["Bor", "Thrain", "Gim", "Durin", "Dwalin", "Bal", "Thor", "Gloin", "Oin", "Fili"]
##    midfixes = ["in", "ar", "or", "ur", "un", "an", "ril", "din", "grim", "thor"]
##    suffixes = ["rock", "beard", "forge", "stone", "hammer", "shield", "iron", "axe", "helm", "miner"]
##
##    generated_name = random.choice(prefixes) + random.choice(midfixes) + random.choice(suffixes)
##    return generated_name.capitalize()
##
##
##
##def generate_gnomish_name():
##    prefixes = ["Giz", "Blix", "Nim", "Fizz", "Zig", "Blip", "Tock", "Glim", "Diz", "Snip"]
##    midfixes = ["ble", "plo", "tink", "glee", "wiz", "fiz", "kib", "snick", "noodle", "twizzle"]
##    suffixes = ["gadget", "whistle", "widget", "noodle", "crank", "sprocket", "gizmo", "spark", "buckle", "spinner"]
##
##    generated_name = random.choice(prefixes) + random.choice(midfixes) + random.choice(suffixes)
##    return generated_name.capitalize()
##
##
##def generate_gnomish_name():
##    prefixes = ["Gizmo", "Blixle", "Nimble", "Fizzle", "Zigzag", "Blipper", "Tockle", "Glimmer", "Dizzle", "Snicker"]
##    midfixes = ["ble", "plo", "tink", "glee", "wiz", "fiz", "kib", "snick", "noodle", "twizzle"]
##    suffixes = ["gadget", "whistle", "widget", "noodle", "crank", "sprocket", "gizmo", "spark", "buckle", "spinner"]
##
##    generated_name = random.choice(prefixes) + random.choice(midfixes) + random.choice(suffixes)
##    return generated_name.capitalize()
##
##
##    
##
##def generate_guttural_orcish_name():
##    prefixes = ["Gruk", "Drek", "Gor", "Throk", "Mog", "Hak", "Kor", "Nar", "Gul", "Zar"]
##    suffixes = ["Gr", "Keh", "Mog", "Th", "Rok", "Sk", "Gh", "Nar", "Zog", "Thr"]
##
##    generated_name = random.choice(prefixes) + random.choice(suffixes)
##    return generated_name.capitalize()
##
##
##
##
##def generate_halfling_name():
##    prefixes = ["Bil", "Fro", "Sam", "Pip", "Mer", "Ro", "Pri", "Dai", "Tom", "Ru"]
##    suffixes = ["bo", "odo", "m", "pin", "ie", "sey", "hill", "den", "bur", "der"]
##    middle_names = ["Berry", "Leaf", "Meadow", "Sunflower", "Daisy", "Breeze", "Puddle", "Pebble", "Sparrow", "Tumble"]
##
##    first_name = random.choice(prefixes) + random.choice(suffixes)
##    middle_name_1 = random.choice(middle_names)
##    middle_name_2 = random.choice([name for name in middle_names if name != middle_name_1])
##    middle_name_3 = random.choice([name for name in middle_names if name != middle_name_1 and name != middle_name_2])
##    last_name = random.choice(prefixes) + random.choice(suffixes)+ random.choice(suffixes)
##
##    return f"{first_name} {middle_name_1} {middle_name_2} {middle_name_3} {last_name}"




###end Knat stuff

def makeElf(character,new=True):
    if new:
        character.stats['dex']+=2
        
        sk1='Perception'
        while sk1 in character.proficiencies:
            sk1=random.choice(basics.skillList)
        for lang in ['Elvish','Common']:
            while lang in character.languages:
                lang=random.choice(basics.languageList)
            character.languages.append(lang)

    darkV=basics.Property("Darkvision",'''You can see in dim light within 60' as if it were bright light, and in darkness as if it were dim light.
                          You can't discern color in darkness.''')
    character.addProperty(darkV)
    feyAnc=basics.Property("Fey Ancestry","You have advantage on saving throws against being charmed, and magic can't put you to sleep")
    character.addProperty(feyAnc)
    trance=basics.Property("Trance","You only need to meditate for 4 hours, rather than sleep and spend 8 hours, to long rest.")
    character.addProperty(trance)
def makeAstralElf(character,new=True):
    if new:
        x=random.choice(list(character.stats.keys()))
        y=x
        z=y
        while y==x:
            y=random.choice(list(character.stats.keys()))
        while z==y or z==x:
            z=random.choice(list(character.stats.keys()))
        coin=random.choice([True,False])
        if coin:
            character.stats[x]+=2
            character.stats[y]+=1
        else:
            character.stats[x]+=1
            character.stats[y]+=1
            character.stats[z]+=1
            
        save=copy.copy(character.classes)
        i=character.stats['int']
        w=character.stats['wis']
        c=character.stats['cha']

        if i>c and i>w:
            character.classes=[classStuff.Wizard]
        elif c>i and c>w:
            character.classes=[classStuff.Bard]
        elif w>i and w>c:
            character.classes=[classStuff.Cleric]
        elif i>=w:
            character.classes=[classStuff.Wizard]
        else:
            character.classes=[classStuff.Cleric]
        
        spells.setCantrips(0,character)
        x=random.choice(['Dancing Lights','Light','Sacred Flame'])
        y=spells.spells[x]
        character.addSpell(y)

        character.classes=save
        sk1='Perception'
        while sk1 in character.proficiencies:
            sk1=random.choice(basics.skillList)
        character.proficiencies.append(sk1)
        while sk1 in character.proficiencies:
            sk1=random.choice(basics.skillList)
        character.proficiencies.append(sk1)

        sk2=random.choice(basics.toolList)
        while sk2 in character.proficiencies:
            sk2=random.choice(basics.toolList)
        character.proficiencies.append(sk2)
        trance=basics.Property("Astral Trance",'''You only need to meditate for 4 hours, rather than sleep and spend 8 hours, to long rest.
Your '''+sk1+''' and '''+sk2+''' proficiencies are special.
You can swap them out each long rest for any other option.
The tool proficiency can be swapped for a weapon proficiency if you insist.''')
    
        for lang in ['Common','Common']:
            while lang in character.languages:
                lang=random.choice(basics.languageList)
            character.languages.append(lang)
    else:
        trance=basics.Property("Astral Trance",'''You only need to meditate for 4 hours, rather than sleep and spend 8 hours, to long rest.
One each of your skill and tool proficiencies are special.
You can swap out those skill and tool proficiencies each long rest for any other option.
The tool proficiency can be swapped for a weapon proficiency if you insist.''')
    
    darkV=basics.Property("Darkvision",'''You can see in dim light within 60' as if it were bright light, and in darkness as if it were dim light.
You can't discern color in darkness.''')
    character.addProperty(darkV)
    feyAnc=basics.Property("Fey Ancestry","You have advantage on saving throws against being charmed")
    character.addProperty(feyAnc)
    character.addProperty(trance)
    starStep=basics.Property("Starlight Step",'''As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see.
You can use this trait '''+str(character.proficiency)+''' times per long rest.''')
    character.addProperty(starStep)
    
def makeBaseHighElf(character,new=True):
    if new:
        character.stats['int']+=1
    
        save=copy.copy(character.classes)
        character.classes=[classStuff.Wizard]
        spells.setCantrips(1,character)
        character.classes=save
    
        character.proficiencies.extend(['Longsword','Shortsword','Shortbow','Longbow'])

        sk1='Elvish'
        while sk1 in character.languages:
            sk1=random.choice(basics.languageList)
        character.languages.append(sk1)

def makeAvariel(character,new=True):
    flight=basics.Property("Flight","You have a fly speed of 30'.  You can't fly in medium or heavy armor.")
    character.addProperty(flight)
    if new:
        sk1='Auran'
        while sk1 in character.languages:
            sk1=random.choice(basics.languageList)
        character.languages.append(sk1)

def makeDrow(character,new=True):
    if new:
        character.stats['cha']+=1
        spells.setCantrips(0,character)
        character.addSpell(spells.spells["Dancing Lights"])
        character.proficiencies.extend(['rapier','shortsword','hand crossbow'])
    sdark=basics.Property("Darkvision",'''You can see in dim light within 120' as if it were bright light, and in darkness as if it were dim light.
                          You can't discern color in darkness.''',1)
    character.addProperty(sdark)
    sunsens=basics.Property("Sunlight Sensitivity",'''You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you,
the target of your attack, or whatever you are trying to perceive is in direct sunlight.''')
    character.addProperty(sunsens)
    save=copy.copy(character.classes)
    character.classes=[classStuff.Bard]
    if character.level>=3 and "Faerie Fire" not in character.spells.keys():
        character.addSpell(spells.spells["Faerie Fire"],"1 free/long rest")
    if character.level>=5 and "Darkness" not in character.spells.keys():
        character.addSpells(spells.spells["Darkness"],"1 free/long rest")
    character.classes=save

def makeUAEladrin(character,new=True):
    if new:
        r=random.choice([1,0])
        if r:
            character.stats['int']+=1
        else:
            character.stats['cha']+=1
        season=random.choice(['s','f','w',''])
        cantrip={'s':"Fire Bolt",'f':"Friends",'w':"Chill Touch",'':'Minor Illusion'}
        while cantrip[season] in character.spells.keys():
            season=random.choice(['s','f','w',''])
        character.saveString+=season

    feyStep=basics.Property("Fey Step","As a bonus action 1/short rest you can magically teleport up to 30' to an empty space you can see.")

    cantrip={'s':"Fire Bolt",'f':"Friends",'w':"Chill Touch",'':'Minor Illusion'}
    if 's' in character.saveString:
        season='s'
    elif 'f' in character.saveString:
        season='f'
    elif 'w' in character.saveString:
        season='w'
    else:
        season=''
    if character.stats['int']<character.stats['cha']:
        blurb='cha, which is '+str(character.stats['cha'])
        swap=[classStuff.Bard]
    else:
        blurb='int, which is '+str(character.stats['int'])
        swap=[classStuff.Wizard]
    
    
    shiftingSeasons=basics.Property("Shifting Seasons",'''You can change your season, altering your personality and swapping a cantrip at the end of each short rest.
Your current cantrip is '''+cantrip[season]+'''.
Your spellstat for this is '''+blurb+".")
    if cantrip[season] not in character.spells:
        save=copy.copy(character.classes)
        character.classes=swap
        setCantrips(0,character)
        character.addSpell(spells.spells[cantrip[season]],"seasonal",-1)
    character.addProperty(feyStep)
    character.addProperty(shiftingSeasons)

def makeDMGEladrin(character,new=True):
    if new:
        character.stats['int']+=1
        season=random.choice(['s','f','w',''])
        character.saveString+=season
        character.addSpell(spells.spells["Misty Step"],"free 1/short rest",1)
        character.proficiencies.extend(['Longsword','Shortsword','Shortbow','Longbow'])
def makeMTFEladrin(character,new=True):
    if new:
        character.stats['int']+=1
        season=random.choice(['s','f','w',''])
        character.saveString+=season
    if 's' in character.saveString:
        season='s'
    elif 'f' in character.saveString:
        season='f'
    elif 'w' in character.saveString:
        season='w'
    else:
        season=''
    spec={'s':'','w':'','f':'','':''}
    if character.level>=3:
        spec['s']= '''\nThen each adjecent creature you choose takes '''+str(max(basics.getMod(character.stats['cha']),1))+''' fire damage.'''
        spec['']='''\nYou can use this ability to instead teleport a willing touched creature.'''
        spec['w']='''\nThen one formerly seen, formerly adjacent creature of your choice Wis saves v.s. DC '''+str(8+character.proficiency+basics.getMod(character.stats['cha']))+''' or be frightened of you until the end of your next turn.'''
        spec['f']='''\nThen up to two creatures you choose must DC '''+str(8+character.proficiency+basics.getMod(character.stats['cha']))+''' Wis save or be charmed by you for 1 minute or until you or your allies damage it'''
    feyStep=basics.Property("Fey Step","As a bonus action 1/short rest you can magically teleport up to 30' to an empty space you can see."+spec[season])

    character.addProperty(feyStep)
    if character.level>=3:
        blurb='and Fey Step effect '
    else:
        blurb=''
    shiftingSeasons=basics.Property("Shifting Seasons",'''You can change your season, altering your personality '''+blurb+'''at the end of each long rest.''')
    
def makeGrugach(character,new):
    if new:
        character.stats['str']+=1
    
        save=copy.copy(character.classes)
        ssave=character.saveString
        character.classes=[classStuff.Druid]
        spells.setCantrips(1,character)
        character.saveString=ssave
        character.classes=save
    
        character.proficiencies.extend(['Spear','Net','Shortbow','Longbow'])
        for i in character.languages:
            if i=='Common':
                q=random.choice(basics.languageList)
                while q in character.languages:
                    q=random.choice(basics.languageList)
                t=character.languages.index(i)
        character.languages[t]=q
            
        sk1='Sylvan'
        while sk1 in character.languages:
            sk1=random.choice(basics.languageList)
        character.languages.append(sk1)
        
def makeAereni(character,new):
    if new:
        for i in character.proficiencies[:]: ##slice creates temp copy so removal is safe
            if i in ['Longbow','Shortbow','Longsword','Shortsword']:
                character.proficiencies.remove(i)
        roll=random.choice([1,0])
        if roll:
            sk1=random.choice(basics.skillList)
            while sk1 in character.proficiencies:
                sk1=random.choice(basics.skillList)
        else:
            sk1=random.choice(basics.trueToolsList)
            while sk1 in character.proficiencies:
                sk1=random.choice(basics.trueToolsList)
        character.expertises.append(sk1)
def makeValenar(character,new):
    if new:
        for i in character.proficiencies[:]:
            if i in ['Shortsword','Longsword']:
                character.proficiencies.remove(i)
        character.proficiencies.extend(['Scimitar','Double Scimitar'])
def makeVahadar(character,new):
    if new:
        character.stats['wis']+=1
    
        save=copy.copy(character.classes)
        character.classes=[classStuff.Druid]
        spells.setCantrips(1,character)
        character.classes=save
    
        character.proficiencies.extend(['Longsword','Shortsword','Shortbow','Longbow'])

        sk1='Elvish'
        while sk1 in character.languages:
            sk1=random.choice(basics.languageList)
        character.languages.append(sk1)
def makeWoodElf(character,new):
    if new:
        character.stats['wis']+=1
    maskWild=Property("Mask of the Wild",'''You can attempt to hide when lightly obscured, if the obstruction if from a natural source.''')
    fleetFoot=Property("Fleet of Foot",'''Your base walking speed is 35'.''')
    character.proficiencies.extend(['Longsword','Shortsword','Shortbow','Longbow'])
    character.addProperty(maskWild)
    character.addProperty(fleetFoot)
def makeMarkofShadow(character,new):
    if new:
        character.stats['cha']+=1
        save=copy.copy(character.classes)
        character.classes=['Bard']
        spells.setCantrips(0,character)
        character.addSpell(spells.spells['Minor Illusion'])
        character.classes=save
        
    for i in ["Disguise Self","Silent Image","Darkness","Pass Without Trace","Clairvoyance","Major Image","Greater Invisibility", "Hallucinatory Terrain","Mislead"]:
        if i not in character.spellExtensions and i not in character.spells.keys():
            character.spellExtensions.append(i)
    if character.level>=3 and 'Invisibility' not in character.spells.keys():
        character.addSpell(spells.spells['Invisibility'])
    cunningInt=Property("Cunning Intuition","+1d4 to Charisma (Performance) and Dexterity (Stealth) checks")
    character.addProperty(cunningInt)
    


    
        


                   
elfSubraces=['Astral Elf','High Elf','Avariel','Drow','Variant Eladrin','Lesser Eladrin','Eladrin','Grugach','Aereni High Elf','Aereni Eladrin','Valenar High Elf','Valenar Eladrin','Vahadar Elf','Bishatar Elf','Tirahar Elf','Mark of Shadow Elf']
humanSubraces=['Lesser Human']

def raceLookup(nname):
    for i in raceList:
        if i.name==nname:
            return i
    if nname in elfSubraces:
        e=copy.copy(raceLookup("Elf"))
        e.name=nname
        return e
    if nname in humanSubRaces:
        e=copy.copy(raceLookup("Human"))
        e.name=nname
        return e
