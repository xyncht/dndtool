class Spell:
    def __init__(self,nname,llevel,ttext='',hhigher=[]):
        self.name=nname
        self.level=llevel
        self.text=ttext
        self.higher=[]
class miniSpell:
    def __init__(self,sspell,nname,nnote,vvalue):
        self.spell=sspell
        self.name=nname
        self.note=nnote
        self.value=vvalue
        
spells={}
loader=[]

beastSense=Spell("Beast Sense",2,'''For concentration max 1 hour, you can see and hear through a willing beast
you touch during casting, using its senses rather than your own.''')
speakWithAnimals=Spell("Speak with Animals",1,'''You can verbally communicate with and understand beasts for the next 10 minutes''')

loader.append(beastSense)
loader.append(speakWithAnimals)

for i in loader:
    spells[i.name]=i
        
