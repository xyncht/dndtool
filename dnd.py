import sys
import random
import math
import numpy
import os
from basics import *
import classStuff
import raceStuff
from character import *
import menu
from classStuff import classList


while True:
    x=input ("Welcome to the 5e Character Roller!  Would you like to (l)oad a character, (r)oll up a new one, (a)dd new data files, or (q)uit the game?\n")
    print("\n\n")
    if x in ['q','Q','quit','Quit']:
        sys.exit(0)
    if x in ['r','R','roll','Roll']:
        curfile=Character.generate()
        curfile.printOut()
        menu.subMenu(curfile)
    if x in ['l','L','load','Load']:
        menu.loadMenu()       
            
                
        
    else:
        print("Sorry, I didn't understand that.  Please try again.\n")
