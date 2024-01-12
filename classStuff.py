import sys
import random
import math
import numpy
import os
import basics
import spells

def getMod(stat):
    if stat<10:
        stat-=1
    return int((stat-10)/2)

class Property:
    def __init__(self,nname,ttext='',vvalue=0):
        self.name=nname
        self.text=ttext
        self.value=vvalue

barbarianSubclasses=["Wild Magic Barbarian","Zealot","Storm Herald","Berserker","Juggernaut","Ancestral Guardian","Bear Warrior","Eagle Warrior","Elk Warrior","Tiger Warrior","Wolf Warrior"]

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
            Spells.makeSpellcaster(character,Artificer):
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
            for i in character.subclasses:
                if i in barbarianSubclasses:
                    sb=i
            if sb=='none':
                sb=random.choice(barbarianSubclasses)
                character.subclasses.append(sb)
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

# ... (uncecked names)

Rogue.firstNameList = {"Male": ["Shadow", "Silent", "Swift", "Dagger", "Whisper", "Rat", "Sly", "Deceit", "Cunning", "Mystery", "Fox", "Rogue", "Shade", "Noctis", "Garrett", "Viper", "Slade"],
                     "Female": ["Shadow", "Silent", "Swift", "Dagger", "Whisper", "Rat", "Sly", "Deceit", "Cunning", "Mystery", "Fox", "Rogue", "Shade", "Noctis", "Garrett", "Viper", "Slade"]}
Rogue.lastNameList = ["the Shadow", "Silentfoot", "Swiftblade", "Daggerfall", "Whisperwind", "Blackcloak", "Greythief", "Deceitful", "Cunning", "Mysterio", "Foxworthy", "Nightshade", "Nocturnal", "Darkblade", "Viperscale", "Silade"]

Monk.firstNameList = {"Male": ["Zen", "Harmony", "Tranquil", "Qi", "Meditation", "Calm", "Wisdom", "Flow", "Balance", "Enlightenment", "Peace", "Serenity", "Brother", "Sister", "Silent", "Still", "Master", "Student"],
                    "Female": ["Zen", "Harmony", "Tranquil", "Qi", "Meditation", "Calm", "Wisdom", "Flow", "Balance", "Enlightenment", "Peace", "Serenity", "Brother", "Sister", "Silent", "Still", "Master", "Student"]}
Monk.lastNameList = ["of Harmony", "Peaceful", "Flowingstream", "Silentfoot", "Stillwind", "Tranquilheart", "Enlightened", "Calmwater", "Balancewalker", "Meditationcloud", "Serenityblossom", "Zenmind", "Qiwhisper", "Wisdomleaf", "Brotherhood", "Sisterhood", "MasterofChi", "StudentofPeace"]

Paladin.firstNameList = {"Male": ["Sir", "Valiant", "Noble", "Courageous", "Holy", "Divine", "Loyal", "Virtuous", "Zealous", "Radiant", "Honorable", "Brave", "Gallant", "Fearless", "Aegis", "Shield", "Sword"],
                       "Female": ["Lady", "Valiant", "Noble", "Courageous", "Holy", "Divine", "Loyal", "Virtuous", "Zealous", "Radiant", "Honorable", "Brave", "Gallant", "Fearless", "Aegis", "Shield", "Sword"]}
Paladin.lastNameList = ["the Valiant", "of Virtue", "Shieldbearer", "Swordsworn", "Holyheart", "Zealouslight", "Nobleblade", "Radiantglory", "Gallanthonor", "Honorbound", "Divinejustice", "Courageousheart", "Fearlessdefender", "Champion", "of the Faith", "the Brave"]

Mystic.firstNameList = {"Male": ["Arcane", "Mystical", "Enigmatic", "Diviner", "Seer", "Astral", "Sorcerer", "Oracle", "Psion", "Mindbender", "Telepath", "Dreamwalker", "Esoteric", "Illusionist", "Warp", "Realitybender", "Shadow", "Eldritch"],
                      "Female": ["Arcane", "Mystical", "Enigmatic", "Diviner", "Seer", "Astral", "Sorcerer", "Oracle", "Psion", "Mindbender", "Telepath", "Dreamwalker", "Esoteric", "Illusionist", "Warp", "Realitybender", "Shadow", "Eldritch"]}
Mystic.lastNameList = ["the Mystic", "Mindweaver", "Enchantedsoul", "Seeress", "Astralwalker", "Sorceress", "Oraclesight", "Psionicmind", "Dreamweaver", "Illusionist", "Realityshaper", "Shadowbinder", "Eldritchpower", "Arcane", "Esoteric", "Mystic"]

Sorcerer.firstNameList = {"Male": ["Arcane", "Mystical", "Enigmatic", "Diviner", "Seer", "Astral", "Sorcerer", "Mage", "Wizard", "Caster", "Warlock", "Enchanter", "Conjurer", "Summoner", "Elementalist", "Necromancer", "Illusionist", "Pyromancer", "Geomancer"],
                       "Female": ["Arcane", "Mystical", "Enigmatic", "Diviner", "Seer", "Astral", "Sorceress", "Mage", "Wizard", "Caster", "Warlock", "Enchantress", "Conjurer", "Summoner", "Elementalist", "Necromancer", "Illusionist", "Pyromancer", "Geomancer"]}
Sorcerer.lastNameList = ["the Sorcerer", "Mage", "Wizard", "Spellweaver", "Enchantedsoul", "Conjurer", "Summoner", "Elementalist", "Necromancer", "Illusionist", "Pyromancer", "Geomancer", "Arcanist", "Mystic", "Enigma"]

Wizard.firstNameList = {"Male": ["Arcane", "Mystical", "Enigmatic", "Diviner", "Seer", "Astral", "Sorcerer", "Mage", "Wizard", "Caster", "Enchanter", "Conjurer", "Summoner", "Elementalist", "Necromancer", "Illusionist", "Pyromancer", "Geomancer"],
                      "Female": ["Arcane", "Mystical", "Enigmatic", "Diviner", "Seer", "Astral", "Sorceress", "Mage", "Wizard", "Caster", "Enchantress", "Conjurer", "Summoner", "Elementalist", "Necromancer", "Illusionist", "Pyromancer", "Geomancer"]}
Wizard.lastNameList = ["the Wizard", "Mage", "Sorcerer", "Spellweaver", "Enchantedsoul", "Conjurer", "Summoner", "Elementalist", "Necromancer", "Illusionist", "Pyromancer", "Geomancer", "Arcanist", "Mystic", "Enigma"]

Warlock.firstNameList = {"Male": ["Cursed", "Hex", "Infernal", "Eldritch", "Dread", "Abyssal", "Fiendish", "Dark", "Shadow", "Spectral", "Demonic", "Otherworldly", "Malevolent", "Sinister", "Coven", "Mystic", "Occult", "Warlock", "Vile", "Nether"],
                      "Female": ["Cursed", "Hex", "Infernal", "Eldritch", "Dread", "Abyssal", "Fiendish", "Dark", "Shadow", "Spectral", "Demonic", "Otherworldly", "Malevolent", "Sinister", "Coven", "Mystic", "Occult", "Warlock", "Vile", "Nether"]}
Warlock.lastNameList = ["the Warlock", "Hexweaver", "Cursed", "Darkbinder", "Infernal", "Eldritch", "Dread", "Abyssal", "Fiendish", "Shadow", "Spectral", "Demonic", "Malevolent", "Sinister", "Nether", "Coven", "Mystic", "Occult", "Doombringer", "Vile"]

# end unchecked 'names'

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
