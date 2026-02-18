#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def songs():
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]

    halo_time = silence_time = clean_time = 0
    
    for song, time in violator_songs_list:
        if song == 'Halo':
            halo_time = time
        elif song == 'Enjoy the Silence':
            silence_time = time
        elif song == 'Clean':
            clean_time = time

    time1 = halo_time + silence_time + clean_time
    time1 = round(time1, 2)

    violator_songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }

    time2 = (violator_songs_dict['Sweetest Perfection'] + 
             violator_songs_dict['Policy of Truth'] + 
             violator_songs_dict['Blue Dress'])
    time2 = round(time2)
    
    return time1, time2