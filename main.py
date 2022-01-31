import pygame as pg
import numpy as np
import random
import time, datetime

def init_array(min_value, max_value, number_of_items):
    return [random.randint(min_value, max_value) for i in range(0, number_of_items)]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                yield j, j + 1, 'red', 'red'
                array[j], array[j + 1] = array[j + 1], array[j]
                yield j, j + 1, 'green', 'green'
            else:
                yield j, j + 1, 'green', 'green'
    return

def selection_sort(array):
    n = len(array)
    for i in range(n):
        minimum_index = i
        for j in range(i+1, n):
            yield minimum_index, j, 'yellow', 'red'
            if array[minimum_index] > array[j]:
                minimum_index = j
                yield minimum_index, j, 'yellow', 'red'
        yield i, minimum_index, 'red', 'yellow'
        array[i], array[minimum_index] = array[minimum_index], array[i]
        yield i, minimum_index, 'green', 'green'
    return

def sort_update(window, array, number_of_elements, width, alg):
    alg_gen = alg(array)
    for i in range(number_of_elements):
        pg.draw.rect(window, 'magenta', ((width + 1)*i, 0, width, array[i]))
    pg.display.update()
    timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
    while True:
        if datetime.datetime.utcnow() > timer_stop:
            break
        yield
    yield
    while True:
        try:
            current_position = next(alg_gen)
        except StopIteration:
            for i in range(number_of_elements):
                pg.draw.rect(window, 'blue', ((width + 1)*i, 0, width, array[i]))
            pg.display.update()
            return
        window.fill('black')
        for i in range(number_of_elements):
            if i == current_position[0]:
                pg.draw.rect(window, current_position[2], ((width + 1)*i, 0, width, array[i]))
            elif i == current_position[1]:
                pg.draw.rect(window, current_position[3], ((width + 1)*i, 0, width, array[i]))
            else:
                pg.draw.rect(window, 'magenta', ((width + 1)*i, 0, width, array[i]))
        pg.display.update()
        # pg.time.wait(0)
        yield


def main():
    delay = 0
    number_of_elements = 200
    resolution = (1280, 720)

    pg.init()
    window = pg.display.set_mode(resolution)
    window.fill('black')

    running = True

    width = (resolution[0] - number_of_elements) / number_of_elements
    array = init_array(0, 700, number_of_elements)

    sort_update_gen = sort_update(window, array, number_of_elements, width, selection_sort)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        try:
            next(sort_update_gen)
        except StopIteration:
            pass
        

if __name__ == "__main__":
    main()