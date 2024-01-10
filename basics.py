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
    def __init__(self,nname,kkind,vvalue=0,llevel=1):
        self.name=nname
        self.kind=kkind
        self.value=vvalue
        self.llevel=1
