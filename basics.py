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
