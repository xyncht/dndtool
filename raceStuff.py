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
    def makeRace(self,character):
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
            for i in character.stats:
                character.stats[i]+=1
        if character.race.name=="High Elf":
            makeElf(character)
            makeBaseHighElf(character)
            
            

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

# Generate and print 5 longer elven names
print("\n\n elven names ")
for _ in range(5):
    print(generate_elven_name())
Elf.abilityMods={}

Elf.firstNameList={"Male":generate_elven_name(), "Female":generate_elven_name()}
Elf.lastNameList=[generate_elven_name()]



def generate_dwarven_name():
    prefixes = ["Bor", "Thrain", "Gim", "Durin", "Dwalin", "Bal", "Thor", "Gloin", "Oin", "Fili"]
    midfixes = ["in", "ar", "or", "ur", "un", "an", "ril", "din", "grim", "thor"]
    suffixes = ["rock", "beard", "forge", "stone", "hammer", "shield", "iron", "axe", "helm", "miner"]

    generated_name = random.choice(prefixes) + random.choice(midfixes) + random.choice(suffixes)
    return generated_name.capitalize()

# Generate and print 5 dwarven names
print("\n\n dwarf names ")
for _ in range(5):
    print(generate_dwarven_name())
    

def generate_gnomish_name():
    prefixes = ["Giz", "Blix", "Nim", "Fizz", "Zig", "Blip", "Tock", "Glim", "Diz", "Snip"]
    midfixes = ["ble", "plo", "tink", "glee", "wiz", "fiz", "kib", "snick", "noodle", "twizzle"]
    suffixes = ["gadget", "whistle", "widget", "noodle", "crank", "sprocket", "gizmo", "spark", "buckle", "spinner"]

    generated_name = random.choice(prefixes) + random.choice(midfixes) + random.choice(suffixes)
    return generated_name.capitalize()

# Generate and print 5 gnomish names
print("\n\n Gnome names ")
for _ in range(5):
    print(generate_gnomish_name())

def generate_gnomish_name():
    prefixes = ["Gizmo", "Blixle", "Nimble", "Fizzle", "Zigzag", "Blipper", "Tockle", "Glimmer", "Dizzle", "Snicker"]
    midfixes = ["ble", "plo", "tink", "glee", "wiz", "fiz", "kib", "snick", "noodle", "twizzle"]
    suffixes = ["gadget", "whistle", "widget", "noodle", "crank", "sprocket", "gizmo", "spark", "buckle", "spinner"]

    generated_name = random.choice(prefixes) + random.choice(midfixes) + random.choice(suffixes)
    return generated_name.capitalize()

# Generate and print 10 longer gnomish names
print("\n\n Gnome names #2")
for _ in range(5):
    print(generate_gnomish_name())
    

def generate_guttural_orcish_name():
    prefixes = ["Gruk", "Drek", "Gor", "Throk", "Mog", "Hak", "Kor", "Nar", "Gul", "Zar"]
    suffixes = ["Gr", "Keh", "Mog", "Th", "Rok", "Sk", "Gh", "Nar", "Zog", "Thr"]

    generated_name = random.choice(prefixes) + random.choice(suffixes)
    return generated_name.capitalize()

# Generate and print 5 orcish names with guttural suffixes
print("\n\n Ork names ")
for _ in range(5):
    print(generate_guttural_orcish_name())


def generate_halfling_name():
    prefixes = ["Bil", "Fro", "Sam", "Pip", "Mer", "Ro", "Pri", "Dai", "Tom", "Ru"]
    suffixes = ["bo", "odo", "m", "pin", "ie", "sey", "hill", "den", "bur", "der"]
    middle_names = ["Berry", "Leaf", "Meadow", "Sunflower", "Daisy", "Breeze", "Puddle", "Pebble", "Sparrow", "Tumble"]

    first_name = random.choice(prefixes) + random.choice(suffixes)
    middle_name_1 = random.choice(middle_names)
    middle_name_2 = random.choice([name for name in middle_names if name != middle_name_1])
    middle_name_3 = random.choice([name for name in middle_names if name != middle_name_1 and name != middle_name_2])
    last_name = random.choice(prefixes) + random.choice(suffixes)+ random.choice(suffixes)

    return f"{first_name} {middle_name_1} {middle_name_2} {middle_name_3} {last_name}"

# Generate and print 5 halfling names with three distinct middle names
print("\n\n Halfling names ")
for _ in range(5):
    print(generate_halfling_name())



###end Knat stuff

def makeElf(character):
    character.stats['dex']+=2
    darkV=basics.Property("Darkvision",'''You can see in dim light within 60' as if it were bright light, and in darkness as if it were dim light.
                          You can't discern color in darkness.''')
    character.addProperty(darkV)
    sk1='Perception'
    while sk1 in character.proficiencies:
        sk1=random.choice(basics.skillList)
    feyAnc=basics.Property("Fey Ancestry","You have advantage on saving throws against being charmed, and magic can't put you to sleep")
    character.addProperty(feyAnc)
    trance=basics.Property("Fey Ancestry","You only need to meditate for 4 hours, rather than sleep and spend 8 hours, to long rest.")
    character.addProperty(trance)
    for lang in ['Elvish','Common']:
        while lang in character.languages:
            lang=random.choice(basics.languageList)
        character.languages.append(lang)
    
def makeBaseHighElf(character):
    character.race.name="High Elf"
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
    
elfSubraces=['High Elf']
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
