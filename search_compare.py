#!user/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 4"""

import time, random

def sequential_search(alist, item):
    alist.sort() 
    start = time.time()
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    endtime = time.time()
    elapsed = endtime - start
    return { "found": found, "difference": elapsed}

def ordered_sequential_search(alist, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1
    endtime = time.time()
    elapsed = endtime - start
    return { "found": found, "difference": elapsed}

def binary_search_iterative(alist, item):
    alist.sort()
    start = time.time()
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    endtime = time.time()
    elapsed = endtime - start
    return { "found": found, "difference": elapsed}

def binary_search_recursive(alist, item):
    alist.sort()
    start = time.time()
    if len(alist) == 0:
        found = False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                return binary_search_recursive(alist[:midpoint], item)
            else:
                return binary_search_recursive(alist[midpoint + 1:], item)
            
    endtime = time.time()
    elapsed = endtime - start
    return { "found": found, "difference": elapsed}

def rndlist(limit):  
    tmplist = random.sample(xrange(1, (limit+1)), 100)  
    return tmplist

def main():
    test_list = [500,1000,10000]

    for test in test_list:
        search_types = {
            'Sequential': 0.0, 
            'Ordered Sequential':0.0, 
            'Iterative Binary': 0.0, 
            'Recursive Binary': 0.0
        }
        i = 0

        while i < 100:
            tmplist = rndlist(test)

            search_types['Sequential'] += sequential_search(tmplist, -1)["difference"]
            search_types['Ordered Sequential'] += ordered_sequential_search(tmplist, -1)["difference"]
            search_types['Iterative Binary'] += binary_search_iterative(tmplist, -1)["difference"]
            search_types['Recursive Binary'] += binary_search_recursive(tmplist, -1)["difference"]
            i += 1

        for search_type in search_types:
            print "%s Search took %10.7f seconds to run, on average %s" % (search_type, search_types[search_type] / 100, test)


if __name__ == "__main__":
    main()
