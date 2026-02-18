#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def circle():
    radius = 42
    pi = 3.1415926
    area = pi * radius ** 2
    area_rounded = round(area, 4)
    
    point_1 = (23, 34)
    point_2 = (30, 30)
    
    distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
    distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
    
    return area_rounded, distance_1 <= radius, distance_2 <= radius