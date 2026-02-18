#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def zooF():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    
    zoo.insert(1, 'bear')
    zoo1 = zoo.copy()
    
    birds = ['rooster', 'ostrich', 'lark']
    zoo.extend(birds)
    zoo2 = zoo.copy()
    
    zoo.remove("elephant")
    zoo3 = zoo.copy()
    
    lion = zoo.index('lion') + 1
    lark = zoo.index('lark') + 1
    
    return zoo1, zoo2, zoo3, lion, lark