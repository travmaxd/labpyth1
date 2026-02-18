#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def garden():
    garden_flowers = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow_flowers = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

    garden_set = set(garden_flowers)
    meadow_set = set(meadow_flowers)

    flowers_all = garden_set | meadow_set
    flowers_common = garden_set & meadow_set
    garden_only = garden_set - meadow_set
    meadow_only = meadow_set - garden_set
    
    return flowers_all, flowers_common, garden_only, meadow_only