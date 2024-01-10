import sys
import random
import math
import numpy
import os

def getMod(stat):
    if stat<10:
        stat-=1
    return int((stat-10)/2)

class Property:
    def __init__(self,nname,kkind,vvalue=0,llevel=1):
        self.name=nname
        self.kind=kkind
        self.value=vvalue
        self.llevel=1

class Class:
    def __init__(self,nname='',hpdie="d8"):
        self.name=nname
        self.properties={}
        self.firstNameList={}
        self.lastNameList=[]
        self.hp=5
        if hpdie=="d10":
            self.hp+=1
        if hpdie=="d12":
            self.hp+=2
        if hpdie=="d6":
            self.hp-=1
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
    def progress(self,char):
        pass

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
Mystic=Class("Mystic","d8")
classList.append(Artificer)
classList.append(Barbarian)
classList.append(Bard)
classList.append(Fighter)
classList.append(Druid)
classList.append(Cleric)
classList.append(Ranger)
##classList.append(Rogue)
##classList.append(Monk)
##classList.append(Paladin)
##classList.append(Mystic)
##classList.append(Sorcerer)
##classList.append(Wizard)
##classList.append(Warlock)

Artificer.firstNameList={"Male" : ["Alec","Oil","Alkali","Salt","Sparky","Malachi","Ham","Crovak","Arturo","Arthur","Fash","Beebo","Clint","Colton","Iniquious","Able","Wort"], "Female" : ["Sparky","Fizzle","Estrella","Star","Tink","Lisa","Elizabeth","Mildred","Esther","Ether","Gravity","Orba","Acid","Peridot","Effervescence","Amber","Quima","Serena","Xiphura","Gemma"]}
Artificer.lastNameList=["Tinkerman","Tralysis","Barr","Vintner","Gnomekin","Mason","Freeman","Depth","Crafthome","Gemwise","Workready"]
Barbarian.firstNameList={"Male" : ["Quake","Mountain-in-Winter","Sun-on-Taiga","Grog","Agog","Crovax","Conan","Urgor","Amos","Belphor","Yuri","Igor","Bull","Ox","Quarm","Brutus","Wolf","Pugillius","Brock"], "Female" : ["Olga","Hilda","Hilde","Gorma","Argovf","Brunhilde","Brunna","Ronna","Rocce","Wrath-of-the-Mother","Geovanna","Quake","Daughter-of-Bear"]}
Barbarian.lastNameList=["Rocksteady","","Giantsoul","of the Mountain","of the Sky Father","of the North","of the West","Wildkin","the Hammer","the Unstoppable","the Unconquered","the Defiant", "the Bloody","the Red","the Black","the Fair","Skullbreaker","Bearslayer","Dragonslayer","Flesheater","Brokenshield","Lastman","the Furious","Steele","Stoneskin","Ironhide","Snow","the Strong","Fisher","Hunter","Orchild","Wilkins","Wilkin","Galica","the Axe"]
Bard.firstNameList={"Male" : ["Wolfgang","Amadeus","John","Gabriel","Glint","Rough","Fabio","Cassius","Giacomo","Stereo","Franz","Ludwig","Jean-Paule","Viswanathan","Romeo","Pierre","Pedro","Clement","Temerius"],"Female" : ["Rose","Juliet","Humility","Star","Benitia","Blessing","Chamomile","Eve","Susan","Darla","Shirley","Dorothea","Tsing","Xiaotong","Nona","Hildegard","Florence","Lili","Amy","Clara","Florence"]}
Bard.lastNameList=["Singer","Stryker","Starr","Trumpet","Drummer","Sparkle","Casanova","Farussi","Maddalena","Golde","the Proud"]
Fighter.firstNameList={"Male" : ["John","Sabre","Grok","Bartholomew","Chester","Donnovan","Spartacus","Maximus","Septimus","Alder","William","Eric","Aldrich","Garth"], "Female" : ["Samantha","Vixian","Vanessa","Claudia","Karla","Nani","Hanako","Cherry","Apple","Brier","Faustina","Fidelma","Anastasia","Hippolyta","Hippolyta","Melanippe","Antiope"]}
Fighter.lastNameList=["Carver","Themiscyrian","the Warrior","Freeman","of the Sword","Arm-bearer","Shield-Bearer","Verias","Valerian","Kingsman","Kane","the Brave","the Daring","the Bold","the Quick","the Red","the Black","the Brown","the Grey"]
Druid.firstNameList={"Male":["Wind-in-Branches","Pebble","Stone-from-the-Heavens","Odin","Cody","Alder","Birch","Durian","Jack","Elder","Alph","Dogwood","Mulberry","Birch","Oak"], "Female":["Apple","Cherry","Yew","Birch","Blueberry","Clover","Greenleaf","Pomegranate","Melonie","Willow","Ash","Sequoia","Swallowtail","Moshka","Fern","Brooke","Spring-Moss","Sunshadow","Rain-on-Snow","Brier","Thorn","Rose","Dahlia","Poppy","Rafflesia","Flora","Florence","Nightsong","Water-meets-Land"]}
Druid.lastNameList=["Greenblossom","Blueblossom","Redflower","Springtide","Eventide","Winters","Summerfield","Acorn", "Bitterblossom", "Elderberry","Sargassum","Swampwallow","Bear-brother","Wolfmother","Swift","Swallow","Hare","Rabbit","Bounces-Brightly","Treechild","the Wanderer","the Lost","the Finder","Moonwatcher","Stargazer","Druid","Demonslayer","Forest-Friend","Desertkin","of the Sands","of the Sea","of the River","Elksmate","Hart","of the Wilds","Wilde","Strange"]
Cleric.firstNameList={"Male":["Bartholomew","Elric","Æsa","Carlos","Jesus","Muhammad","Muhatma","Sidartha","Moses","Able","Honor","Elija","Isaiah","Obadiah","Ezekial","Ezra","Malachi","Amr","Ali","Bartok","Cyril","Patrick","Stephen","Andrew","George","Vishy","Sunil","Rohan","Temperance","Hope"],"Female":["Keziah","Marie","Claire","Ester","Ethyl","Rahab","Deuteronomy","Joan","Zipporah","Ximena","Leah","Miriam","Rebecca","Sara","Huldah","Abigail","Serenity","Hope","Charity","Temperance","Chastity","Prudence","Blessing"]}
Cleric.lastNameList=["the Merciful","the Mild","the Merciless","the Flambeaux","the Evangelist","Flameheart","Frostbrow","Priest","Book","Booker","Ready-for-Death","the Undying","Peacemaker","Peacebreaker","Lifetaker","Lifebringer","of the Far Waters","the Second","the Third","the Eighth","the Blessed","who Blesses","Crop-Blesser","Raindancer","Medicine-maker","Sits-with-Spirits","the Questioning","the Atheist","the Forgiven","of the Far Ones"]
Ranger.firstNameList={"Male":["Sabre","Oscar","Pebble","Gultch","Red","John","Vaegram","Cordell","James","Ezekial","Joseph","Yussef","Arman","Alder","Vengeance","Dogwood","Ivan","Ariel"],"Female":["Raven","Crow","Owl","Littleflower","Whiteflower","Rose","Thorn","Saffron","Rose-of-Sharron","Esmerelda","Pear","Effervescence","Moonlight","Xera","Fara","Fidelma","Faithless","Hope","Dawn","Twilight","Wind-on-Stone","Grace","Liena"]}
Ranger.lastNameList=["the Wild","Windrunner","Blade","Zephyr","of the Forest","Ranger","Strider","the Mountain","the Fierce","the Quick","Eagle-eye","Bear's-Strength","Bearslayer","Dragonslayer","the Proud","the Watcher","Returned","the Survivor","Bowmaker","Fletcher","Flint","Knapper","Smith","Doe"]

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
    def abilityMod(self,char):
        for i in self.abilityMods:
            char.stats[i]=char.stats[i]+self.abilityMods[i]
        if self.name=="Human":
            for i in char.stats:
                char.stats[i]+=1

Human=Race("Human")
Elf=Race("Elf")
Dwarf=Race("Dwarf")
Gnome=Race("Gnome")

raceList=[]
raceList.append(Human)
##raceList.append(Elf)
##raceList.append(Dwarf)
##raceList.append(Gnome)

Human.firstNameList={"Male":["Bart","Dmitri","Vassily","Arthur","Steve","John","Jack","Michael","Bert","Ernesto","Ulrich","Vladomir","Patrick","George","Pafnuty","Cyril","Ping","Abe","Jin","Tsu","Suh","Ivan","Boris","Gregor","Franz","Wilhelm","Otis","Evan","Able","Isaac","Abraham","Jacob","Moses","Anaxamenes","Raila","Oginga","Agwambo"],"Female":["Susan","Samantha","Xena","Ximena","Jane","Mildred","Minerva","Miranda","Karla","Olga","Hilda","Heidi","Brunhilde","Vasolina","Ana","Adelheld","Janet","Rose","Estrella","Isabella","Esperanza","Innessa","Natalya","Larisa","Agrafena","Alina","Inga","Ingrid","Augusta","Valerie","Aoi","Aiko","Fumiko","Chiyo","Bai","Chen","Baozhai","Enya","Soo yun","Hana","Gyeong","Chuki","Bishara","Aanuoluwakiishi","Diekololaoluwa","Ayotunde","Pippi","Teicuih","Tlazohtzin"]}
Human.lastNameList=["Oruba","Ramaposa","Mbumba","Katsyv","Chebyshev","the Black","the Red","the Fair","the Brown","the Grey","the White","White","Black","Fisher","Book","Carpenter","Shepard","Roaver","Wheeler","Carter","Keeper","Beesly","Smith","Downe","Hoover","Rodriguez","Fernandez","Cervantes","O'Reily","O'Toole","O'Mally","O'Loxly","Anand"]
Human.abilityMods={}

def classLookup(nname):
    if '/' not in nname:
        for i in classList:
            if i.name==nname:
                return [i]
    else:
        raise "D: D: not ready!!!"
def raceLookup(nname):
    return Human

class Character:
    def __init__(self):
        self.classes=[]
        self.stats={}
        pass
    def firstLevel(self,attributeGen="StandardArray"):
        self.level=1
        gender=random.choice(["Male","Female"])
        cclass=random.choice(classList)
        rrace=random.choice(raceList)
        self.classes=[cclass]
        self.race=rrace
        roll=random.choice([True,False])
        if roll:
            nname=random.choice(cclass.firstNameList[gender])
        else:
            nname=random.choice(rrace.firstNameList[gender])
        roll=random.choice([True,False])
        if roll:
            nnname=random.choice(cclass.lastNameList)
        else:
            nnname=random.choice(rrace.lastNameList)
        self.name= nname+" "+nnname

        self.stats={"str":10,"dex":10,"con":10,"int":10,"wis":10,"cha":10}
        if attributeGen=="3d6Fixed":
            raise "3d6Fixed is not defined"
        elif attributeGen=="4d6DropOne":
            raise "4d6DropOne is not defined"
        elif attributeGen=="StandardArray":
            values=[15,14,13,12,10,8]
            numpy.random.shuffle(values)
            for i in self.stats:
                self.stats[i]=0+values[0]
                values.pop(0)
            self.race.abilityMod(self)

        self.hp=self.classes[0].hp*2-2+getMod(self.stats["con"])
        ##self.features=self.classes[0].featureGain(1)
    def randLevelUp(self):
        self.level+=1
        self.hp+=self.classes[0].hp
        if self.level%4==0:
            j=0
            k=''
            for i in self.stats:
                if self.stats[i]>j:
                    k=i
                    j=self.stats[i]
            self.stats[k]+=2
        random.choice(self.classes).progress(self) ###may need self= this
            
                
    def classSpread(self):
        if len(self.classes)==1:
            return self.classes[0].name
        else:
            raise("class Spreader not implemented")
    def printOut(self):
        print("You are "+self.name+", a level "+str(self.level)+" "+self.race.name+" "+self.classSpread()+".\n")
        
    
        
    def generate():
        This=Character()
        repeat=True
        while repeat:
            repeat=False
            q=input("What level character would you like to create?\n")
            print("\n\n")
            if int(q) not in range(1,21):
                if q in ['b','B','Back','back','q','Q','quit','Quit']:
                    return -1
                else:
                    print("Sorry, I didn't understand that.  Try entering a number from 1 to 20, or (b)ack.\n")
                    repeat=True
        repeat=True
        while repeat:
            repeat=False
            s=input("Would you like to set any other parameters? (y/n)\n")
            print("\n\n")
            if s in ['y','Y','yes','Yes','s','S','set','Set']:
                print("not yet implemented\n")
            elif s not in ['n','N','no','No','NO','r','R','roll','Roll','','\n']:
                repeat=True
            
        level=int(q)
        This.firstLevel()
        i=1
        while i<level:
            This.randLevelUp()
            i=i+1
        return This

def loadUp(text):
    def nextWord():
        char=""
        nonlocal text
        while True:
            if text[0]=="@":
                text=text[1:]
                return char
            else:
                char=char+text[0]
                text=text[1:]
    curfile=Character()
    curfile.name=nextWord()
    curfile.classes=classLookup(nextWord())
    curfile.level=int(nextWord())
    curfile.race=raceLookup(nextWord())
    curfile.stats["str"]=int(nextWord())
    curfile.stats["dex"]=int(nextWord())
    curfile.stats["con"]=int(nextWord())
    curfile.stats["int"]=int(nextWord())
    curfile.stats["wis"]=int(nextWord())
    curfile.stats["cha"]=int(nextWord())
    curfile.hp=curfile.classes[0].hp*2-2+getMod(curfile.stats["con"])
    return curfile

def subMenu(curfile):
    sub=True
    while sub:
        q=input("Would you like to (v)iew more detailed information about your character, (s)ave your character to a text file, return to the main (m)enu, or (q)uit?\n")
        if q in ['y','Y','yes','Yes','v','V','view','View']:
            print("\033[H\033[J", end="") ##clears screen via escape codes
            curfile.printOut()
            print("\n\n")
            print("You have "+str(curfile.hp)+" hit points\n")
            print("Your ability scores are:\n")
            print("Str: "+str(curfile.stats["str"])+"\n")
            print("Dex: "+str(curfile.stats["dex"])+"\n")
            print("Con: "+str(curfile.stats["con"])+"\n")
            print("Int: "+str(curfile.stats["int"])+"\n")
            print("Wis: "+str(curfile.stats["wis"])+"\n")
            print("Cha: "+str(curfile.stats["cha"])+"\n")
            input("Enter any prompt to continue")
        if q in ['s',"S",'save',"Save",'y','Y','yes','Yes']:
            file= open(curfile.name+'.txt', 'w') ##will overwrite existing file with same name if present until check implemented!
            file.write(curfile.name+"@"+curfile.classSpread()+"@"+str(curfile.level)+"@"+curfile.race.name+"@"+str(curfile.stats["str"])+"@"+str(curfile.stats["dex"])+"@"+str(curfile.stats["con"])+"@"+str(curfile.stats["int"])+"@"+str(curfile.stats["wis"])+"@"+str(curfile.stats["cha"])+"@@")
            file.close()
            print("\n\nfile saved as "+curfile.name+'.txt\n')
        if q in ['q','Q','quit','Quit','exit','Exit','e','E','x','X','n','N','no','No']:
            input("\nHave a good day :)\n")
            sys.exit(0)
        if q in ['m','M','menu','Menu','main','Main','b','B','Back','back']:
            sub=False

def loadMenu():
    print("Load which file?\n")
    keyset={}
    iter=1
    for ffile in os.listdir():
        if ffile.endswith(".txt"):
            # Prints only text file present in Current Directory
            print(str(iter)+") "+ffile)
            keyset[iter]=ffile
    print("\n")
    y=input()
    if int(y) not in keyset:
        raise "fix keyset user sanity checking"

    ##Get the actual contents of the file into memory
    file=open(keyset[int(y)])
    text=file.read()
    curfile=loadUp(text)
    subMenu(curfile)
        



while True:
    x=input ("Welcome to the 5e Character Roller!  Would you like to (l)oad a character, (r)oll up a new one, (a)dd new data files, or (q)uit the game?\n")
    print("\n\n")
    if x in ['q','Q','quit','Quit']:
        sys.exit(0)
    if x in ['r','R','roll','Roll']:
        curfile=Character.generate()
        curfile.printOut()
        subMenu(curfile)
    if x in ['l','L','load','Load']:
        loadMenu()       
            
                
        
    else:
        print("Sorry, I didn't understand that.  Please try again.\n")
