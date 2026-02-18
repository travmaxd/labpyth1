#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def family():
    my_family = ['Мама', 'Папа', 'Оля']

    my_family_height = [
        [my_family[0], 167], 
        [my_family[1], 180], 
        [my_family[2], 165]
    ]
    
    heightPapa = my_family_height[1][1]
    height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
    
    return heightPapa, height