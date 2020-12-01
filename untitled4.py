# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:09:08 2020

@author: Redouane
"""

import matplotlib.pyplot as plt
import random
x,y=0.05,0

abscisse = list()
ordonne = list()
i=30000
while i:   
    p= random.uniform(0,1)
    if p<=0.02: 

        x,y= (0.5,0.27*y)
        
    if 0.02<p<(0.02+0.15):
      x,y=(-1*0.139*x+0.263*y+0.57,0.246*x+0.224*y+(-1)*0.036)
        
    if (0.02+0.15)<p<(0.02+0.15+0.13):
        x,y=(0.17*x -1*0.215*y+0.408,0.222*x +0.176*y+0.0893)
        
    else 0.4<p<0.6:
        x,y=(0.781*x +0.034*y+0.1075,-1*0.032*x+0.739*y+0.27)
        
   
       
    i-=1
    abscisse.insert(0,x)
    ordonne.insert(0,y)
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
plt.plot(abscisse , ordonne,'r.')
plt.show()