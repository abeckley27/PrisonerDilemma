# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:39:40 2023

@author: Aidan
"""


class strategy(object):
    
    def __init__(self, name_, ID_, play_):
        self.name = name_
        self.ID = ID_
        self.play = play_
        self.count = 0
    
    def __repr__(self):
        return self.name


class player(object):
    
    def __init__(self, strat_):
        self.strat = strat_
        self.points = 0
    
    def __repr__(self):
        return self.strat.name + " player with %d points" %self.points
        
    
    
        