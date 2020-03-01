# Search Algorithms Comparison
# Assignment 4
# By: Joshua Rifkin

import time
import random

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    return (time.time()-start)


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
#        print("After increments of size", sublist_count, "The list is", a_list)

        sublist_count = sublist_count // 2
    return (time.time()-start)


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def python_sort(a_list):
    start = time.time()
    a_list.sort()
    return (time.time()-start)

def main():
    tests = [500, 1000, 10000]
    times = {
        'insertionSort': 0,
        'shellSort': 0,
        'pythonSort': 0
    }
    runs = 0

    for test in tests:
        count = 0
        while count < 100:
            randomList = random.sample(range(0, 10000), test)

            # next three lines are to ensure that all 3 algs sort the same exact list for most precise comparison
            sortList = {1:[], 2:[], 3:[]}
            for list in sortList:
                sortList[list] = randomList.copy()

            times['insertionSort'] += insertion_sort(sortList[1])
            times['shellSort'] += shell_sort(sortList[2])
            times['pythonSort'] += python_sort(sortList[3])

            count += 1
            runs += 1

    print("Insertion Sort took {} seconds to run on average.".format(times['insertionSort'] / runs))
    print("Shell Sort Search took {} seconds to run on average.".format(times['shellSort'] / runs))
    print("Python Sort Iterative took {} seconds to run on average.".format(times['pythonSort'] / runs))


if __name__ == '__main__':
    main()


