#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def movies():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    
    first_comma = my_favorite_movies.find(',')
    first_movie = my_favorite_movies[:first_comma]

    last_comma = my_favorite_movies.rfind(',')
    last_movie = my_favorite_movies[last_comma + 2:]

    second_comma = my_favorite_movies.find(',', first_comma + 1)
    second_movie = my_favorite_movies[first_comma + 2:second_comma]

    prev_last_comma = my_favorite_movies.rfind(',', 0, last_comma)
    second_last_movie = my_favorite_movies[prev_last_comma + 2:last_comma]

    return first_movie, last_movie, second_movie, second_last_movie