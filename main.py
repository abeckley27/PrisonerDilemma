# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:39:28 2023

@author: Aidan
"""

import time
import random as rd
import numpy as np
import prison_strats
from player import *

t0 = time.time()
starting_population = 1000
points_for_survival = 500
points_for_reproduction = 2000
num_strategies = len(prison_strats.strategies)

stratlist = []

for i in range(num_strategies):
    stratlist.append( strategy(prison_strats.names[i], i, prison_strats.strategies[i]) )

poplist = []
for i in range(starting_population):
    s = rd.randint(0, num_strategies - 1)
    poplist.append(player( stratlist[s] ))
    stratlist[s].count += 1

population_counts = []

daycount = []
for s in stratlist:
    daycount.append(s.count)

population_counts.append(daycount)

def day():
    x1 = prison_strats.run_game(poplist[0].strat.play, poplist[-1].strat.play, 50)
    poplist[0].points += x1[0]
    poplist[-1].points += x1[1]
    
    for j in range(1, len(poplist) - 1):
        result0 = prison_strats.run_game(poplist[j].strat.play, poplist[j-1].strat.play, 50)
        poplist[j].points += result0[0]
        poplist[j-1].points += result0[1]
        
        result1 = prison_strats.run_game(poplist[j].strat.play, poplist[j+1].strat.play, 50)
        poplist[j].points += result1[0]
        poplist[j+1].points += result1[1]
    
    p = 0
    while (p < len(poplist)):
        if (poplist[p].points < points_for_survival):
            poplist[p].strat.count -= 1
            q = poplist.pop(p)
            
        elif (poplist[p].points > points_for_reproduction):
            poplist.insert( p, player(poplist[p].strat) )
            poplist[p].strat.count += 1
            p += 2
        
        else:
            p += 1
    
    daycount = []
    for s in stratlist:
        daycount.append(s.count)
    
    population_counts.append(daycount)
            
    
num_days = 10
x = range(num_days + 1)
y = []

for k in range(num_days):
    day()

for j in range(num_strategies):
    y.append([])
    for k in range(num_days+1):
        y[-1].append(population_counts[k][j])


print("time: %.3f s" %(time.time() - t0))


from matplotlib import pyplot as plt


plt.plot(x, y[7])












