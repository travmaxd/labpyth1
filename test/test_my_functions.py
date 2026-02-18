# test/test_my_functions.py
import pytest
import sys
import os

# Добавляем корневую директорию в путь
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from my_functions import *

def test_calculate_distances():
    """Тест функции calculate_distances из distance.py"""
    result = calculate_distances()
    assert isinstance(result, dict)
    assert 'Moscow-London' in result
    assert 'Moscow-Paris' in result
    assert 'London-Paris' in result
    # Проверяем что расстояния положительные числа
    assert result['Moscow-London'] > 0
    assert result['Moscow-Paris'] > 0
    assert result['London-Paris'] > 0

def test_circle():
    """Тест функции circle из circleL.py"""
    area, point1_in, point2_in = circle()
    assert isinstance(area, float)
    # Проверяем площадь круга (π * r²)
    expected_area = round(3.1415926 * 42 ** 2, 4)
    assert area == expected_area
    # Точка (23, 34) должна быть внутри круга
    assert point1_in == True
    # Точка (30, 30) должна быть  круга  
    assert point2_in == False

def test_movies():
    """Тест функции movies из favorite_movies.py"""
    first, last, second, second_last = movies()
    assert first == 'Терминатор'
    assert last == 'Назад в будущее'
    assert second == 'Пятый элемент'
    assert second_last == 'Чужие'

def test_garden():
    """Тест функции garden из gardenL.py"""
    flowers_all, flowers_common, garden_only, meadow_only = garden()
    # Проверяем типы
    assert isinstance(flowers_all, set)
    assert isinstance(flowers_common, set)
    assert isinstance(garden_only, set)
    assert isinstance(meadow_only, set)
    # Проверяем содержание
    assert 'ромашка' in flowers_common
    assert 'роза' in garden_only
    assert 'клевер' in meadow_only
    assert 'одуванчик' in flowers_common

def test_family():
    """Тест функции family из my_family.py"""
    heightPapa, total_height = family()
    assert heightPapa == 180
    assert total_height == 167 + 180 + 165

def test_operations():
    """Тест функции operations из operationsL.py"""
    expression, result = operations()
    assert expression == '((1 + 2) * 3 - 4) * 5'
    assert result == 25

def test_secret():
    """Тест функции secret из secretL.py"""
    result = secret()
    assert isinstance(result, str)
    assert len(result) > 0
    # Должны быть пробелы между словами
    assert ' ' in result

def test_shops():
    """Тест функции shops из shopping.py"""
    result = shops()
    assert isinstance(result, dict)
    # Проверяем наличие всех категорий сладостей
    assert 'печенье' in result
    assert 'конфеты' in result
    assert 'карамель' in result
    assert 'пирожное' in result
    # Проверяем структуру данных
    for sweet, shops_list in result.items():
        assert isinstance(shops_list, list)
        for shop_info in shops_list:
            assert 'shop' in shop_info
            assert 'price' in shop_info

def test_songs():
    """Тест функции songs из songs_list.py"""
    time1, time2 = songs()
    assert isinstance(time1, float)
    assert isinstance(time2, int)
    # Время должно быть положительным
    assert time1 > 0
    assert time2 > 0

def test_store():
    """Тест функции store из storeL.py"""
    results = store()
    assert isinstance(results, list)
    assert len(results) == 4  # Лампа, Стол, Диван, Стул
    # Проверяем что все товары присутствуют в выводе
    items_found = {
        'Лампа': False,
        'Стол': False, 
        'Диван': False,
        'Стул': False
    }
    for result in results:
        for item in items_found:
            if item in result:
                items_found[item] = True
    # Все товары должны быть найдены
    assert all(items_found.values())

def test_zoo():
    """Тест функции zooF из zooL.py"""
    zoo1, zoo2, zoo3, lion_idx, lark_idx = zooF()
    # Проверяем типы
    assert isinstance(zoo1, list)
    assert isinstance(zoo2, list) 
    assert isinstance(zoo3, list)
    assert isinstance(lion_idx, int)
    assert isinstance(lark_idx, int)
    # Проверяем содержание
    assert 'bear' in zoo1  # Медведь добавлен
    assert 'rooster' in zoo2  # Птицы добавлены
    assert 'elephant' not in zoo3  # Слон удален
    # Индексы должны быть положительными
    assert lion_idx > 0
    assert lark_idx > 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])