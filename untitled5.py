# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:09:14 2020

@author: Redouane
"""

import matplotlib.pyplot as plt
import random
x,y =5,4
a1,b1=1,2
a2,b2=8,3
a3,b3=4,6
abscisse=list()
ordonne=list()
i=50000
while i:
    p=random.uniform(0,1)
    if p<=0.333:
        x,y=(0.5*(x+a1),0.5*(y+b1))
    if 0.333<p<0.666:
        x,y=(0.5*(x+a2),0.5*(y+b2))
    elif p>=0.666:
        x,y=(0.5*(x+a3),0.5*(y+b3))
    abscisse.insert(0,x)
    ordonne.insert(0,y)
    i-=1
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
plt.plot(abscisse , ordonne,'r.')
plt.show()
