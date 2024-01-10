import sys
import random
import math
import numpy
import os
import basics

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

def classLookup(nname):
    if '/' not in nname:
        for i in classList:
            if i.name==nname:
                return [i]
    else:
        raise "D: D: not ready!!!"
