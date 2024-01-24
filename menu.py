import sys
import random
import math
import numpy
import os
from basics import *
import classStuff
from classStuff import classList
from character import *
import raceStuff
import spells

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
                
    def spellLoad(char):
        ttext=char.spellString
        loop=True
        array=[]
        current=''
        while loop:
            if ttext[0]=='#':
                array.append(current)
                if len(ttext)>1:
                    ttext=ttext[1:]
                    current=''
                else:
                    loop=False
            else:
                current+=ttext[0]
                ttext=ttext[1:]
        spells.setCantrips(0,char)
        for i in array:
            if i != '':
                char.flashSpell(spells.spells[i])
                
    curfile=Character()
    curfile.name=nextWord()
    t=nextWord()
    curfile.classes=classStuff.classLookup(t)
    if t!=curfile.classes[0].name:
        curfile.subclasses=[t]
    curfile.level=int(nextWord())
    curfile.race=raceLookup(nextWord())
    curfile.stats["str"]=int(nextWord())
    curfile.stats["dex"]=int(nextWord())
    curfile.stats["con"]=int(nextWord())
    curfile.stats["int"]=int(nextWord())
    curfile.stats["wis"]=int(nextWord())
    curfile.stats["cha"]=int(nextWord())
    curfile.saveString=nextWord()
    curfile.spellString=nextWord()
    while len(curfile.spellString)>0 and curfile.spellString[-1]=='#': ##delete this and two following lines maybe
        curfile.spellString=curfile.spellString[:-1]
    curfile.spellString+='#'
    spellLoad(curfile)
    curfile.skillLoad(nextWord())
    for i in range(1,curfile.level+1):
        curfile=curfile.classes[0].featureGain(i,curfile)
    curfile.hp=curfile.classes[0].hp*(1+curfile.level)-2+curfile.level*getMod(curfile.stats["con"])
    curfile.race.makeRace(curfile,False) # load race without regenerating everything and reapplying stat mods.
    for i in curfile.classes:
        curfile.refactor(i)

    return curfile

def save(curfile):
    prof=''
    for i in curfile.proficiencies:
        prof+=i
        prof+='#'
    for i in curfile.expertises:
        prof+=i
        prof+='#'
    file= open(curfile.name+'.txt', 'w') ##will overwrite existing file with same name if present until check implemented!
    file.write(curfile.name+"@"+curfile.classSpread()+"@"+str(curfile.level)+"@"+curfile.race.name+"@"+str(curfile.stats["str"])+"@"+str(curfile.stats["dex"])+"@"+str(curfile.stats["con"])+"@"+str(curfile.stats["int"])+"@"+str(curfile.stats["wis"])+"@"+str(curfile.stats["cha"])+"@"+curfile.saveString+"@"+curfile.spellString+'#'+'@'+prof+"@"+"@@")
    file.close()
    print("\n\nfile saved as "+curfile.name+'.txt\n')
    
def detMenu(curfile):
    sub=True
    while sub:
        q=input("Would you like to view Class (F)eatures,(P)roficiencies,(S)pells,(I)tems, or go (B)ack?\n")
        print("\n\n")
        if q in ['f','F','Features','features','c','C','class','Class']:
            for k in curfile.properties:
                print(curfile.properties[k].text+"\n\n")
        if q in ['p','P','prof','Prof','proficiencies','Proficiencies','proficiency','Proficiency']:
            sp=[]
            tp=[]
            se=[]
            te=[]
            for k in curfile.proficiencies:
                if k in curfile.expertises:
                    if k in basics.skillList:
                        se.append(k)
                    else:
                        te.append(k)
                else:
                    if k in basics.skillList:
                        sp.append(k)
                    else:
                        tp.append(k)
            print("You are proficient in:\n")
            for i in sp:
                print("- "+i)
            if len(tp)>0:
                if len(sp)>0:
                    print("               As well as:\n")
                for i in tp:
                    print("- "+i)
            if len(se)>0 or len(te)>0:
                print("You have expertise in:\n")
                for i in se:
                    print("- "+i)
                if len(te)>0:
                    if len(se)>0:
                        print("               As well as:\n")
                    for i in te:
                        print("- "+i)
                
            
        if q in ['s','S','spells','Spells']:
            levelSort=[[],[],[],[],[],[],[],[],[],[]]
            for k in curfile.spells:
                levelSort[curfile.spells[k].spell.level].append(k)
            iter=0
            while iter<10:
                if len(levelSort[iter])>0:
                    print("level "+str(iter)+":")
                for i in levelSort[iter]:
                    if curfile.spells[i].note != '':
                        nnote='('+curfile.spells[i].note+')'
                    else:
                        nnote=''
                    print(curfile.spells[i].name+nnote+":")
                    print(curfile.spells[i].spell.text)
                    print("\n")
                iter+=1
                    
        if q in ['i','I','items','Items']:
            pass
        if q in ['b','B','back','Back']:
            sub=False
            
def subMenu(curfile):
    if curfile.name==Character().name:
        return
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
            detMenu(curfile)
                    
                    
        if q in ['s',"S",'save',"Save",'y','Y','yes','Yes']:
            save(curfile)
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
            iter+=1
    print("\n")
    y=input()
    if int(y) not in keyset:
        raise "fix keyset user sanity checking"

    ##Get the actual contents of the file into memory
    file=open(keyset[int(y)])
    text=file.read()
    curfile=loadUp(text)
    subMenu(curfile)


    
def parameterize():
    repeat=True
    while repeat:
        repeat=False
        x=input("Would you like to set any additional parameters? (y/n) or (b)ack\n\n")
        print("\n\n")
        if x in ['y','Y','yes','Yes']:
            y=input('''Choose Parameters:
- (c)lass prespecified
- (r)ace prespecified

''')
            string={}
            if 'c' in y:
                z=input('''Specify class:\n\n'''+classStuff.classString+'\n\n')
                if z in '12345678910111314':
                    c=classStuff.classList[int(z)-1]
                    string['c']=c
                else:
                    raise "bad number"
            if 'r' in y:
                z=input('''Choose a race:
1) Human
2) Elf

''')
                if z=='1':
                    r=raceStuff.Human
                if z=='2':
                    r=raceStuff.Elf
                
                string['r']=r
            return string

        elif x in ['n','N','no','No']:
            return ''
        elif x in ['m','M','menu','Menu','main','Main','b','B','Back','back']:
            return 'BACK'
        else:
            repeat=True
            print("Sorry, I didn't understand that.\n")
        

def mainMenu():
    while True:
        x=input ("Welcome to the 5e Character Roller!  Would you like to (l)oad a character, (r)oll up a new one, (a)dd new data files, or (q)uit the game?\n")
        print("\n\n")
        if x in ['q','Q','quit','Quit']:
            sys.exit(0)
        if x in ['r','R','roll','Roll']:
            curfile=Character.generate(parameterize())
            curfile.printOut()
            subMenu(curfile)
        if x in ['l','L','load','Load']:
            loadMenu()       
                
                    
            
        else:
            print("Sorry, I didn't understand that.  Please try again.\n")

