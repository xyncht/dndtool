import sys
import random
import math
import numpy
import os
import classStuff

def getMod(stat):
    if stat<10:
        stat-=1
    return int((stat-10)/2)

class Property:
    def __init__(self,nname,ttext,vvalue=0):
        self.name=nname
        self.text=ttext
        self.value=vvalue


#Lists of proficiencies:
skillList=['Acrobatics','Animal Handling','Arcana','Athletics','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuasion','Religion','Sleight of Hand','Stealth','Survival']


artisanList=['Alchemist\'s Supplies','Brewer\'s Supplies','Caligrapher\'s Supplies','Carpenter\'s Tools','Cartographer\'s Tools','Cobbler\'s Tools','Cook\'s Tools','Glassblower\'s Tools','Jeweller\'s Tools','Leatherworker\'s Tools','Mason\'s Tools','Painter\'s Supplies','Potter\'s Tools','Smith\'s Tools','Tinker\'s Tools','Weaver\'s Tools','Woodcarver\'s Tools']
gamingList=['Dice Set','Chess Set','Playing Card Set']
trueToolsList=['Climber\'s Kit','Disguise Kit','Forgery Kit','Hacking Tools','Healer\'s Kit','Herbalism Kit','Mess Kit','Navigator\'s Tools','Poisoner\'s Kit','Thieves\' Tools']
musicList=['Bagpipes','Birdpipes','Drum','Dulcimer','Flute','Glaur','Hand Drum','Horn','Longhorn','Lute','Lyre','Pan Flute','Shawm','Songhorn','Tantan','Thelarr','Tocken','Viol','Wargong','Yarting','Zulkoon']

toolList=artisanList+gamingList+trueToolsList+musicList


simpleList=['Club','Dagger','Dart','Greatclub','Handaxe','Javelin','Light Crossbow','Light Hammer','Light Repeating Crossbow','Mace','Quarterstaff','Shortbow','Shortsword','Sickle','Sling','Spear','Staff','Yklwa']
martialList=['Battleaxe','Blowgun','Double-Bladed Scimitar','Flail','Glaive','Greataxe','Greatsword','Halberd','Hand Crossbow','Heavy Crossbow','Hooked Shortspear','Hoopak','Lance','Longbow','Longsword','Maul','Morningstar','Net','Oversized Longbow','Pike','Rapier','Scimitar','Shortsword','Trident','War Pick','Warhammer','Whip']
firearmList=['Antimatter Rifle','Automatic Pistol','Automatic Rifle','Hunting Rifle','Laser Pistol','Laser Rifle','Musket','Pistol','Revolver','Shotgun']
weaponList=simpleList+martialList+firearmList

blanketList=['All Simple Weapons','All Martial Weapons','All Firearms']
armorList=['Light Armor','Medium Armor','Heavy Armor','Shields']

languageList=['Auran','Aquan','Common','Dwarvish','Elvish','Giant','Gnomish','Goblin','Halfling','Ignan','Orc','Abyssal','Celestial','Draconic','Deep Speech','Infernal','Primordial','Sylvan','Undercommon','Aarokocra','Abanasinian','Abyssal','Alzhedo','Aven','Blink Dog','Bothli','Bullywug','Celestial','Chessentan','Chondathan','Coalition Pidgin','Common','Common Sign Language','Common Trade Pidgin','Daelkyr','Damaran','Dambrathan','Deep Speech','Demonic','Draconic','Dwarvish','Elvish','Ergot','Giant','Giant Eagle','Giant Elk','Giant Owl','Gith','Gnoll','Gnomish','Goblin','Grell','Grung','Guran','Halfling','Halruaan','Homarid','Hook Horror','Ice Toad','Illuskan','Infernal','Istarian','Itzocan','Ixitxachitl','Keldon','Kenderspeak','Kharolian','Khenra','Khur','Kothian','Kraul','Kruthik','Leonin','Loross','Loxodon','Merfolk','Midani','Minotaur','Modron','Mulhorandi','Naga','Nerakese','Netherese','Nordmaarian','Ogre','Olman','Orc','Otyugh','Primordial','Qualith','Quori','Rashemi','Riedran','Roushoum','Sahuagin','Shaaran','Shou','Siren','Slaad','Solamnic','Sphinx','Sylvan','Terran','Thayan','Thri-kreen','Tlincalli','Troglodyte','Tuigan','Turmic','Uluik','Umber Hulk','Undercommon','Untheric','Vampire','Vedalken','Vegepygmy','Waelan','Winter Wolf','Worg','Yeti','Yikaria']
