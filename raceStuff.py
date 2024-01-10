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


def raceLookup(nname):
    return Human
