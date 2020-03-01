# Search Algorithms Comparison
# Assignment 4
# By: Joshua Rifkin

import random
import time

def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found, (time.time()-start)



def ordered_sequential_search(a_list, item):
    start = time.time()
    a_list.sort()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found, (time.time()-start)



def binary_search_iterative(a_list, item):
    start = time.time()
    a_list.sort()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found, (time.time()-start)


def binary_search_recursive(a_list, item):
    a_list.sort()
    if len(a_list) == 0:
        return False, time.time()
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True, time.time()
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)


def main():
    tests = [500, 1000, 10000]
    times = {
        'seqSearch': 0,
        'ordSeqSearch': 0,
        'binSearchIt': 0,
        'binSearchRe': 0
    }
    runs = 0

    for test in tests:
        count = 0
        while count < 100:
            randomList = random.sample(range(0, 10000), test)

            times['seqSearch'] += sequential_search(randomList, -1)[1]
            times['ordSeqSearch'] += ordered_sequential_search(randomList, -1)[1]
            times['binSearchIt'] += binary_search_iterative(randomList, -1)[1]
            start = time.time()
            times['binSearchRe'] += (binary_search_recursive(randomList, -1)[1]-start)

            count += 1
            runs += 1

    print("Sequential Search took {} seconds to run on average.".format(times['seqSearch']/runs))
    print("Ordered Sequential Search took {} seconds to run on average.".format(times['ordSeqSearch']/runs))
    print("Binary Search Iterative took {} seconds to run on average.".format(times['binSearchIt']/runs))
    print("Binary Search Recursive took {} seconds to run on average.".format(times['binSearchRe']/runs))

if __name__ == '__main__':
    main()




