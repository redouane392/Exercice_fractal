# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:44:47 2020

@author: Redouane
"""

 
import matplotlib.pyplot as plt
import random
x,y=0.5,0.0

abscisse = list()
ordonne = list()
i=30000
while i:   
    p= random.uniform(0,1)
    if p<=0.1: 

        x,y= (0.05*x,0.6*y)
        
    elif 0.1<p<0.2:
      x,y=(0.05*x,-0.5*y+1.0)
        
    elif 0.2<p<0.4:
        x,y=(0.46*x -0.32*y,0.39*x +0.38*y+0.6)
        
    elif 0.4<p<0.6:
        x,y=(0.47*x -0.15*y,0.17*x +0.42*y+1.1)
        
    elif 0.6<p<0.8:
       x,y=(0.43*x+0.28*y,-0.25*x+0.45*y +1.0)
        
    elif p>=0.8:
        x,y=(0.42*x+0.26*y,-0.35*x+0.31*y+0.7)
       
    
    abscisse.insert(0,x)
    ordonne.insert(0,y)
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
plt.plot(abscisse , ordonne,'r.')
plt.show()