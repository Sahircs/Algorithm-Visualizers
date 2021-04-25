import pygame
import random
from random import randrange, randint

pygame.init()

max_height = 550
max_width = 1100
window = pygame.display.set_mode((max_width, max_height))
pygame.display.set_caption(
    "Sorting Algorithm Visualiser                             Generate random array: Press Space     "
    "                       Press __ for __ Sort: b (Bubble)  m (Merge)  q (Quick)  r (Radix)")

background_color = (211, 211, 211)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

ratio = 1000 / 25
x = 140

array = []

# Function for User to generate a random array
def random_display():
    array.clear()
    while len(array) <= ratio:
        items = random.randrange(0, 450)
        if items not in array:
            array.append(items)

    for i in range(len(array) - 1):
        pygame.draw.rect(window, blue, (x + 20 * i, 550 - array[i], 10, array[i]))
        pygame.display.update()
    return array

# Helper Method used in a unique way by each Algorithm to visualise the progression of the array being sorted
def highlight(arr, colour_arr, delay=0, idx1=None, colour1=None, idx2=None, colour2=None):
    window.fill(background_color)
    for i in range(len(arr) - 1):
        colour = colour_arr
        if i == idx1:
            colour = colour1
        elif i == idx2:
            colour = colour2
        pygame.time.delay(delay)  # for speed - fast/medium/slow
        pygame.draw.rect(window, colour, (x + 20 * i, 550 - arr[i], 10, arr[i]))
    pygame.display.update()

# Helper Method specifically for Bubble Sort
def bubble_swap(arr, swap1, swap2):
    idx1 = arr.index(swap1)
    idx2 = arr.index(swap2)
    arr[idx1] = swap2
    arr[idx2] = swap1

def bubble_sort(arr, delay=0):
    for i in range(len(arr) - 1):
        for idx in range(len(arr) - i - 1):
            highlight(arr, blue, delay, idx, red)  # For faster algorithm comment line out
            if arr[idx] > arr[idx + 1]:
                bubble_swap(arr, arr[idx], arr[idx + 1])
                highlight(arr, blue, delay, idx, green)

    for idx in range(len(arr) - 1):
        highlight(arr, blue, delay)

def merge_sort(arr, delay=0):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        lhs = merge_sort(left)
        rhs = merge_sort(right)

        arr = []

        while len(lhs) > 0 and len(rhs) > 0:
            ar = lhs + rhs
            # Through each iteration, values added to list are sorted.
            if lhs[0] < rhs[0]:
                idx1 = ar.index(lhs[0])
                idx2 = ar.index(rhs[0])
                highlight(ar, blue, delay, idx1, red, idx2, red)
                arr.append(lhs[0])

                i1 = arr.index(lhs[0])
                highlight(arr, blue, delay, i1, green)
                lhs.pop(0)
            else:
                idx1 = ar.index(lhs[0])
                idx2 = ar.index(rhs[0])
                highlight(ar, blue, delay, idx1, red, idx2, red)
                arr.append(rhs[0])

                i2 = arr.index(rhs[0])
                highlight(arr, blue, delay, i2, green)
                rhs.pop(0)

        for i in lhs:
            arr.append(i)
            highlight(arr, blue, delay, -1, green)

        for i in rhs:
            arr.append(i)
            highlight(arr, blue, delay, -1, green)

        highlight(arr, blue, delay)
    return arr

def quick_sort(arr, start, end, delay=0):
    if start >= end:
        return arr

    pivot_idx = randrange(start, end)
    pivot_element = arr[pivot_idx]
    highlight(arr, blue, delay, pivot_idx, red, end, red)
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]
    highlight(arr, blue, 5, end, green, pivot_idx, green)

    lesser_than_pointer = start
    highlight(arr, blue, delay, start, red)
    for idx in range(start, end):
        if arr[idx] < pivot_element:
            highlight(arr, blue, delay, idx, red, pivot_idx, red)
            arr[idx], arr[lesser_than_pointer] = arr[lesser_than_pointer], arr[idx]
            highlight(arr, blue, delay, idx, green, lesser_than_pointer, green)
            lesser_than_pointer += 1
    arr[end], arr[lesser_than_pointer] = arr[lesser_than_pointer], arr[end]
    highlight(arr, blue, delay, end, green, lesser_than_pointer, green)

    quick_sort(arr, start, lesser_than_pointer - 1)
    quick_sort(arr, lesser_than_pointer + 1, end)

    highlight(arr, blue, delay)

def radix_sort(to_be_sorted, delay):
    maximum_value = str(max(to_be_sorted))
    max_exponent = len(maximum_value)
    being_sorted = to_be_sorted[:]

    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position
        digits = [[] for i in range(10)]

        for number in being_sorted:
            highlight(being_sorted, blue, delay * 2, number, red)
            number_as_a_string = str(number)
            try:
                digit = int(number_as_a_string[index])
            except IndexError:
                digit = 0
            digits[digit].append(number)

            values = []
            for d in digits:
                values.extend(d)
            highlight(values, blue, delay, number, green)

        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)
            highlight(being_sorted, blue, delay, numeral, green)

    highlight(being_sorted, blue, delay)

# How User can interact with the GUI - with buttons representing a certain algorithm that the user has chosen to visualise.
def main():  
    window.fill(white)
    running = True
    while running:
        window.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            random_display()

        if keys[pygame.K_b]:
            bubble_sort(array, 5)

        if keys[pygame.K_m]:
            merge_sort(array, 20)

        if keys[pygame.K_q]:
            quick_sort(array, 0, len(array) - 1, 5)

        if keys[pygame.K_r]:
            radix_sort(array, 7)

    pygame.quit()


main()
