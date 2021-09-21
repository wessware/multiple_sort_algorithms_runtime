from heapq import merge
from math import e
import matplotlib
import matplotlib.pyplot as plt
from random import randint, randrange


def create_array(size=10, max=50):
    return [randint(0, max)
            for _ in range(size)]


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1], arr[i]
                swapped = True
    return arr


def three_way_merge_sort_1(a):
    if len(a) == 1:
        return a
    if len(a) <= 10:
        return insertion_sort(a)
    else:
        n = len(a)
        n1 = n//3
        n2 = n//2

        l = a[0:n1]
        m = a[n1:n2+1]
        r = a[n2+1:n]

    three_way_merge_sort_1(l)
    three_way_merge_sort_1(m)
    three_way_merge_sort_1(r)

    k = 0
    p = 0
    j = 0

    for i in range(n):
        if k < len(l) and p < len(m) and j < len(r):
            x = l[k]
            z = m[p]
            y = r[j]

            if x < y and x < z:
                a[i] = x
                k += 1
            elif y < x and y < z:
                a[i] = y
                p += 1
            elif z < y and z < x:
                a[i] = z
                p += 1
            elif y == x or y == z:
                a[i] = y
                j += 1
            elif x == z:
                a[i] = z
                k += 1
        elif k == len(l):
            if p < len(m) and j < len(r):
                z = m[p]
                y = r[j]

                if z < y:
                    a[i] = z
                    p += 1
                elif y < z:
                    a[i] = y
                    j += 1
                elif z == y:
                    a[i] = y
                    j += 1
            elif p == len(m):
                while j < len(r):
                    a[i] = r[j]
                    j += 1
                    i += 1
            elif j == len(r):
                a[i] = r[j]
                j += 1
                i += 1
            elif j == len(r):
                while p < len(m):
                    a[i] = m[p]
                    p += 1
                    i += 1
        elif p == len(m):
            if k < len(l) and j < len(r):
                x = l[k]
                y = r[j]

                if x < y:
                    a[i] = x
                    k += 1
                elif y < x:
                    a[i] = y
                    j += 1
                elif x == y:
                    a[i] = y
                    j += 1
            elif k == len(l):
                while j < len(r):
                    a[i] = r[j]
                    j += 1
                    i += 1
            elif j == len(r):
                while k < len(l):
                    a[i] = l[k]
                    k += 1
                    i += 1
        elif j == len(r):
            if k < len(l) and p < len(m):
                x = l[k]
                z = m[p]

                if x < z:
                    a[i] = x
                    k += 1
                elif z < x:
                    a[i] = z
                    p += 1
                elif x == z:
                    a[i] = z
                    p += 1
            elif k == len(l):
                while p < len(m):
                    a[i] = m[p]
                    p += 1
                    i += 1
            elif p == len(m):
                a[i] = l[k]
                k += 1
                i += 1
    return a


def two_way_merge_sort(a):
    if len(a) <= 1:
        return a

    middle = len(a)//2
    left = a[:middle]
    right = a[middle:]

    left = two_way_merge_sort(left)
    right = two_way_merge_sort(right)

    return list(merge(left, right))


def three_way_merge_sort(a):
    if len(a) > 1:
        if len(a) == 2:
            n = len(a)
            l = [a[0]]
            m = [a[1]]
            r = []

        else:
            n = len(a)
            n1 = n//3
            n2 = n//2

            l = a[0:n1]
            m = a[n1:n2+1]
            r = a[n2+1:n]
        three_way_merge_sort(l)
        three_way_merge_sort(m)
        three_way_merge_sort(r)

        k = 0
        p = 0
        j = 0
        for i in range(n):
            if k < len(l) and p < len(m) and j < len(r):
                x = l[k]
                z = m[p]
                y = r[j]

                if x < y and x < z:
                    a[i] = x
                    k += 1
                elif y < x and y < z:
                    a[i] = y
                    j += 1
                elif z < y and z < x:
                    a[i] = z
                    p += 1
                elif y == x and y == z:
                    a[i] = y
                    j += 1
                elif x == z:
                    a[i] = x
                    k += 1
            elif k == len(l):
                if p < len(m) and j < len(r):
                    z = m[p]
                    y = r[j]

                    if z < y:
                        a[i] = z
                        p += 1
                    elif y < z:
                        a[i] = y
                        j += 1
                    elif z == y:
                        a[i] = y
                        j += 1
                elif p == len(m):
                    while j < len(r):
                        a[i] = r[j]
                        j += 1
                        i += 1
                elif j == len(r):
                    while p < len(m):
                        a[i] = m[p]
                        p += 1
                        i += 1
            elif p == len(m):
                if k < len(l) and j < len(r):
                    x = l[k]
                    y = r[j]

                    if x < y:
                        a[i] = x
                        k += 1
                    elif y < x:
                        a[i] = y
                        j += 1
                    elif x == y:
                        a[i] = y
                        j += 1
                elif k == len(l):
                    while j < len(r):
                        a[i] = r[j]
                        j += 1
                        i += 1
                elif j == len(r):
                    while k < len(l):
                        a[i] = l[k]
                        k += 1
                        i += 1
            elif j == len(r):
                if k < len(l) and p < len(m):
                    x = l[k]
                    z = m[p]

                    if x < z:
                        a[i] = x
                        k += 1
                    elif z < x:
                        a[i] = z
                        p += 1
                    elif x == z:
                        a[i] = z
                        p += 1
                elif k == len(l):
                    while p < len(m):
                        a[i] = m[p]
                        p += 1
                        i += 1
                elif p == len(m):
                    while k < len(l):
                        a[i] = l[k]
                        k += 1
                        i += 1
    return a


def selection_sort(a):
    sort_len = 0
    while sort_len < len(a):
        min_idx = None
        for i, elem in enumerate(a[sort_len]):
            if min_idx == None or elem < a[min_idx]:
                min_idx = i+sort_len
        a[sort_len], a[min_idx] = a[min_idx], a[sort_len]
        sort_len += 1


def insertion_sort(a):
    for sort_len in range(1, len(a)):
        cur_item = a[sort_len]
        insert_idx = sort_len
        while insert_idx > 0 and cur_item < a[insert_idx]:
            a[insert_idx] = a[insert_idx-1]
            insert_idx += -1

        a[insert_idx] = cur_item


def benchmark(n=[50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 1000, 5000, 10000]):
    from time import time

    insertion_times = []
    bubble_times = []
    selection_times = []
    three_way_merge_sort_times = []
    three_way_merge_sort_1_times = []
    two_way_merge_sort_times = []

    for size in n:
        m = create_array(size, size)
        t0 = time()
        bubble_sort(m)
        t1 = time()
        bubble_times.append(t1-t0)

        m = create_array(size, size)
        t0 = time()
        insertion_sort(m)
        t1 = time()
        insertion_times.append(t1-t0)

        m = create_array(size, size)
        t0 = time()
        selection_sort(m)
        t1 = time()
        selection_times.append(t1-t0)

        m = create_array(size, size)
        t0 = time()
        three_way_merge_sort(m)
        t1 = time()
        three_way_merge_sort_times.append(t1-t0)

        m = create_array(size, size)
        t0 = time()
        three_way_merge_sort_1(m)
        t1 = time()
        three_way_merge_sort_1_times.append(t1-t0)

        m = create_array(size, size)
        t0 = time()
        two_way_merge_sort(m)
        t1 = time()
        two_way_merge_sort_times.append(t1-t0)

    print('\n\tInsertion \tBubble \tMerge_sort \tMerge_sort_Hybrid \tTwo_way_merge_sort \tThree_way_merge_sort')
    print(50*'_')

    for i, size in enumerate(n):
        print('%d \t%0.5f \t%0.5f \t%0.5f \t%0.5f \t%0.5f \t%0.5f' % (
            size,
            insertion_times[i],
            bubble_times[i],
            selection_times[i],
            three_way_merge_sort_times[i],
            three_way_merge_sort_1_times[i],
            two_way_merge_sort_times[i]
        ))
    print('\n')
    plt.plot(n, insertion_times, color='blue', label='insertion_sort')
    plt.plot(n, bubble_times, color='red', label='bubble_sort')
    plt.plot(n, selection_times, color='green', label='selection_sort')
    plt.plot(n, three_way_merge_sort_1_times,
             color='violet', label='merge_sort_hybrid')
    plt.plot(n, two_way_merge_sort_times,
             color='cyan', label='two_way_merge_sort')
    plt.plot(n, three_way_merge_sort_times,
             color='yellow', label='three_way_merge_sort')

    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.show()


benchmark()
