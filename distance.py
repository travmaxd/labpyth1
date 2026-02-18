#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_distances():
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }
    
    distances = {}
    distances['Moscow-London'] = ((550 - 510) ** 2 + (370 - 510) ** 2) ** 0.5
    distances['Moscow-Paris'] = ((550 - 480) ** 2 + (370 - 480) ** 2) ** 0.5 
    distances['London-Paris'] = ((510 - 480) ** 2 + (510 - 480) ** 2) ** 0.5
    
    return distances