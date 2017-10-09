#!user/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 4"""

import time, random

def insertion_sort(alist):
    start = time.time()
    for index in range(1, len(alist)):
        cvalue = alist[index]
        position = index

        
        while position > 0 and alist[position - 1] > cvalue:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = cvalue
    end = time.time()
    elapsed = end - start
    return { "lsit": alist, "difference": elapsed}



def shell_sort(alist):
    start = time.time()
    start = time.time()
    sbcount = len(alist) // 2
    while sbcount > 0:
        for stposition in range(sbcount):
            gap_insertion_sort(alist, stposition, sbcount)
        sbcount = sbcount // 2
    end = time.time()
    elapsed = end - start
    return { "lsit": alist, "difference": elapsed}


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        cvalue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > cvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = cvalue


def python_sort(alist):
    start = time.time()
    alist = alist.sort()
    end = time.time()
    elapsed = end - start
    return { "lsit": alist, "difference": elapsed}

def random_list(limit):  
    tmplist = random.sample(xrange(1, (limit+1)), 100)  
    return tmplist

def main():
    tlist = [500,1000,10000]

    for test in tlist:
        sttypes = {
            'Insertion':0.0, 
            'Shell': 0.0, 
            'Python': 0.0
        }

        i = 0
        while i < 100:
            tmplist = random_list(test)
            sttypes['Insertion'] += insertion_sort(tmplist)["difference"]
            sttypes['Shell'] += shell_sort(tmplist)["difference"]
            sttypes['Python'] += python_sort(tmplist)["difference"]
            i += 1

        for sort_type in sttypes:
            print "%s Sort took %10.7f seconds to run, on average %s" % (sort_type, sttypes[sort_type] / 100, test)


if __name__ == "__main__":
    main()

