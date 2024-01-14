import sys
import random
import math
import numpy
import os
from basics import *
from classStuff import *
from raceStuff import *
import spells

class Character:
    def __init__(self):
        self.classes=[]
        self.subclasses=["none"]
        self.stats={}
        self.properties={}
        self.saveString=''
        self.proficiency=2
        self.spells={}
        self.spellString=''
        self.name=''
        pass
    
    def addProperty(self,nname,ttext='',vvalue=0,):
        bbreak=0
        prev=-1
        for i in self.properties:
            if i==nname:
                prev=self.properties[nname].value
                if prev>value:
                    bbreak=1
        if not bbreak:
            self.properties[nname]=Property(nname,ttext,vvalue)
    def addProperty(self,property):
        bbreak=0
        prev=-1
        for i in self.properties:
            if i==property.name:
                prev=self.properties[i].value
                if prev>property.value:
                    bbreak=1
        if not bbreak:
            self.properties[property.name]=property
            
    def firstLevel(self,mod):
        if 'a' not in mod:
            attributeGen="StandardArray"
        self.level=1
        gender=random.choice(["Male","Female"])
        cclass=random.choice(classList)
        if 'c' in mod:
            cclass=mod['c']
        rrace=random.choice(raceList)
        if 'r' in mod:
            rrace=mod['r']
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
        self=self.classes[0].featureGain(1,self)
        
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
            if k=='con':
                self.hp+=self.level
        if self.level in [5,9,13,17]:
            self.proficiency+=1
        random.choice(self.classes).progress(self) ###may need self= this
            
                
    def classSpread(self):
        if len(self.classes)==1:
            if self.subclasses[0]=='none':
                return self.classes[0].name
            else:
                return self.subclasses[0] ##Multiclassing work needed
        else:
            raise("class Spreader not implemented")

    def printOut(self):
        if self.name!=Character().name:
            print("You are "+self.name+", a level "+str(self.level)+" "+self.race.name+" "+self.classSpread()+".\n")
        
    
    def refactor(self,cclass):
        storage=self.stats
        hpstore=self.hp
        for i in range(1,self.level+1):
            self=self.classes[0].featureGain(i,self)
            self.stats=storage
            self.hp=hpstore

    def generate(mode):
        if mode=='BACK':
            return Character()
        
        This=Character()
        repeat=True
        while repeat:
            repeat=False
            q=input("What level character would you like to create?\n")
            print("\n\n")
            if int(q) not in range(1,21): ##int(q) throws error for non-int q
                if q in ['b','B','Back','back','q','Q','quit','Quit']:
                    return -1
                else:
                    print("Sorry, I didn't understand that.  Try entering a number from 1 to 20, or (b)ack.\n")
                    repeat=True
            
        level=int(q)           
        This.firstLevel(mode)
        i=1
        while i<level:
            This.randLevelUp()
            i=i+1
        This.refactor(This.classes[0])
        return This
    
    def addSpell(self,sspell,nnote='',vvalue=0):
        conflict=False
        key=-999
        
        for i in self.spells:
            if i==sspell.name:
                conflict=True
                key=i
        if not conflict:
            self.spells[sspell.name]=spells.miniSpell(sspell,sspell.name,nnote,vvalue)
            self.spellString+='#'+sspell.name
        else:
            if nnote in self.spells[key].note:
                pass
            elif vvalue<0 and self.spells[key].value>=0:
                pass
            elif vvalue==0 and self.spells[key].value>0:
                pass
            elif vvalue>0 and self.spells[key].value<=0:
                self.spells[sspell.name]=spells.miniSpell(sspell,sspell.name,nnote,vvalue)
            elif vvalue==0 and self.spells[key].value<0:
                self.spells[sspell.name]=spells.miniSpell(sspell,sspell.name,nnote,vvalue)
            elif vvalue>0:
                newnote=self.spells[key].note+" and "+nnote
                self.spells[sspell.name]=spells.miniSpell(sspell,sspell.name,newnote,vvalue)
            elif vvalue<0:
                newnote=self.spells[key].note+" or "+nnote
                self.spells[sspell.name]=spells.miniSpell(sspell,sspell.name,newnote,vvalue)
        
                


        



