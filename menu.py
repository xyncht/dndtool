import sys
import random
import math
import numpy
import os
from basics import *
import classStuff
from classStuff import classList
from character import *
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
    for i in range(1,curfile.level+1):
        curfile=curfile.classes[0].featureGain(i,curfile)
    curfile.hp=curfile.classes[0].hp*(1+curfile.level)-2+curfile.level*getMod(curfile.stats["con"])
    for i in curfile.classes:
        curfile.refactor(i)
    return curfile

def save(curfile):
    file= open(curfile.name+'.txt', 'w') ##will overwrite existing file with same name if present until check implemented!
    file.write(curfile.name+"@"+curfile.classSpread()+"@"+str(curfile.level)+"@"+curfile.race.name+"@"+str(curfile.stats["str"])+"@"+str(curfile.stats["dex"])+"@"+str(curfile.stats["con"])+"@"+str(curfile.stats["int"])+"@"+str(curfile.stats["wis"])+"@"+str(curfile.stats["cha"])+"@"+curfile.saveString+"@@")
    file.close()
    print("\n\nfile saved as "+curfile.name+'.txt\n')
    
def detMenu(curfile):
    sub=True
    while sub:
        q=input("Would you like to view Class (F)eatures,(S)pells,(I)tems, or go (B)ack?\n")
        print("\n\n")
        if q in ['f','F','Features','features','c','C','class','Class']:
            for k in curfile.properties:
                print(curfile.properties[k].text+"\n\n")
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
                iter+=1
                    
        if q in ['i','I','items','Items']:
            pass
        if q in ['b','B','back','Back']:
            sub=False
            
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
