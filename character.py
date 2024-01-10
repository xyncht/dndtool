import sys
import random
import math
import numpy
import os
from basics import *
from classStuff import *
from raceStuff import *

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
        self.hp+=self.classes[0].hp+getMod(self.stats['con'])
        if self.level%4==0:
            j=0
            k=''
            for i in self.stats:
                if self.stats[i]>j:
                    k=i
                    j=self.stats[i]
            self.stats[k]+=2
            if k == "con":
                self.hp+=self.level
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


        



