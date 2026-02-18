#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distance import calculate_distances
from circleL import circle
from operationsL import operations
from favorite_movies import movies
from my_family import family
from zooL import zooF
from songs_list import songs
from secretL import secret
from gardenL import garden
from shopping import shops
from storeL import store


def main():
    print("Система модулей")

    # 1. Расстояния между городами
    print("1. РАССТОЯНИЕ:")
    distances = calculate_distances()
    for route, distance in distances.items():
        print(f"{route}: {distance:.2f}")

    # 2. Вычисления с кругом
    print("\n2. КРУГ:")
    area, point1_check, point2_check = circle()
    print(f"Площадь: {area}")
    print(f"Точка (23, 34) в круге: {point1_check}")
    print(f"Точка (30, 30) в круге: {point2_check}")

    # 3. Математические головоломки
    print("\n3. РАССТАНОВКА ОПЕРАЦИЙ МЕЖДУ ЧИСЛАМИ:")
    expression, result = operations()
    print(f"1 2 3 4 5 = {expression} = {result}")

    # 4. Фильмы
    print("\n4. ФИЛЬМЫ:")
    first, last, second, second_last = movies()
    print(f"Первый фильм: {first}")
    print(f"Последний фильм: {last}")
    print(f"Второй фильм: {second}")
    print(f"Второй с конца: {second_last}")

    # 5. Семья
    print("\n5. СЕМЬЯ:")
    father_height, total_height = family()
    print(f"Рост отца: {father_height} см")
    print(f"Общий рост: {total_height} см")

    # 6. Зоопарк
    print("\n6. ЗООПАРК:")
    zoo1, zoo2, zoo3, lion_pos, lark_pos = zooF()
    print(f"После медведя: {zoo1}")
    print(f"После птиц: {zoo2}")
    print(f"После удаления слона: {zoo3}")
    print(f"Позиция льва: {lion_pos}")
    print(f"Позиция жаворонка: {lark_pos}")

    # 7. Песни
    print("\n7. ПЕСНИ:")
    time1, time2 = songs()
    print(f"Три песни: {time1} мин")
    print(f"Другие три: {time2} мин")

    # 8. Секретное сообщение
    print("\n8. СЕКРЕТ:")
    secret_message = secret()
    print(f"Сообщение: {secret_message}")

    # 9. Сад
    print("\n9. САД:")
    flowers_all, flowers_common, garden_only, meadow_only = garden()
    print(f"Все цветы: {flowers_all}")
    print(f"Общие цветы: {flowers_common}")
    print(f"Только в саду: {garden_only}")
    print(f"Только на лугу: {meadow_only}")

    # 10. Магазины
    print("\n10. ПОКУПКИ")
    sweets = shops()
    for sweet, prices in sweets.items():
        print(f"{sweet}:")
        for shop_info in prices:
            print(f"  {shop_info['shop']}: {shop_info['price']} руб")

    # 11. Магазин
    print("\n11. МАГАЗИН:")
    store_items = store()
    for item in store_items:
        print(item)


if __name__ == "__main__":
    main()

