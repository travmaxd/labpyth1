#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def store():
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store_data = {
        '12345': [{'quantity': 27, 'price': 42}],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }

    results = []
    
    # Лампа
    lamp_code = goods['Лампа']
    lamp_quantity = store_data[lamp_code][0]['quantity']
    lamp_price = store_data[lamp_code][0]['price']
    lamp_cost = lamp_quantity * lamp_price
    results.append(f'Лампа - {lamp_quantity}шт, стоимость {lamp_cost}руб')
    
    # Стол
    table_code = goods['Стол']
    table_quantity1 = store_data[table_code][0]['quantity']
    table_price1 = store_data[table_code][0]['price']
    table_quantity2 = store_data[table_code][1]['quantity']
    table_price2 = store_data[table_code][1]['price']
    table_total_quantity = table_quantity1 + table_quantity2
    table_total_cost = table_quantity1 * table_price1 + table_quantity2 * table_price2
    results.append(f'Стол - {table_total_quantity}шт, стоимость {table_total_cost}руб')
    
    # Диван
    sofa_code = goods['Диван']
    sofa_quantity1 = store_data[sofa_code][0]['quantity']
    sofa_price1 = store_data[sofa_code][0]['price']
    sofa_quantity2 = store_data[sofa_code][1]['quantity']
    sofa_price2 = store_data[sofa_code][1]['price']
    sofa_total_quantity = sofa_quantity1 + sofa_quantity2
    sofa_total_cost = sofa_quantity1 * sofa_price1 + sofa_quantity2 * sofa_price2
    results.append(f'Диван - {sofa_total_quantity}шт, стоимость {sofa_total_cost}руб')
    
    # Стул
    chair_code = goods['Стул']
    chair_quantity1 = store_data[chair_code][0]['quantity']
    chair_price1 = store_data[chair_code][0]['price']
    chair_quantity2 = store_data[chair_code][1]['quantity']
    chair_price2 = store_data[chair_code][1]['price']
    chair_quantity3 = store_data[chair_code][2]['quantity']
    chair_price3 = store_data[chair_code][2]['price']
    chair_total_quantity = chair_quantity1 + chair_quantity2 + chair_quantity3
    chair_total_cost = chair_quantity1 * chair_price1 + chair_quantity2 * chair_price2 + chair_quantity3 * chair_price3
    results.append(f'Стул - {chair_total_quantity}шт, стоимость {chair_total_cost}руб')
    
    return results