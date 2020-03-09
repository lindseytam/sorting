#!/bin/python3


'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.
Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''

    sorted_list = []
    end_xs = len(xs)
    end_ys = len(ys)
    i = 0 # iterator for xs
    j = 0 # iterator for ys

    while i != end_xs and j != end_ys:

        # if elem in xs is smaller than elem in ys
        if (cmp == cmp_standard and xs[i] < ys[j]) or (cmp == cmp_reverse and xs[i] > ys[j]):
            sorted_list.append(xs[i])
            i += 1

        # if elem in ys is smaller than elem in xs
        elif (cmp == cmp_standard and xs[i] >= ys[j]) or (cmp == cmp_reverse and xs[i] <= ys[j]):
            sorted_list.append(ys[j])
            j += 1

    # nothing left in xs or ys
    if i == end_xs and j == end_ys:

        return sorted_list

    # nothing left in xs
    elif i == end_xs:

        for k in range(j, end_ys):
                sorted_list.append(ys[k])

        return sorted_list

    # nothing left in ys
    elif j == end_ys:

        for k in range(i, end_xs):
            sorted_list.append(xs[k])

        return sorted_list


def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:
        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves
    You should return a sorted version of the input list xs
    '''

    if len(xs) <= 1:
        return xs

    else:

        middle = len(xs)//2
        left = xs[:middle]
        right = xs[middle:]

        merge_sorted(left, cmp=cmp)
        merge_sorted(right, cmp=cmp)

        return _merged(merge_sorted(left, cmp=cmp), merge_sorted(right, cmp=cmp), cmp=cmp)

def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected,
    and the list is split into a "less than" sublist and a "greater than" sublist.
    The pseudocode is:
        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)
    You should return a sorted version of the input list xs
    '''

    tmp_low = []
    tmp_high = []
    pivot = []

    if len(xs) <= 1:
        return xs

    else:
        pivot_val = xs[0] # pivot is the first elem
        for elem in xs:

            if elem > pivot_val:
                tmp_high.append(elem)
            elif elem < pivot_val:
                tmp_low.append(elem)
            else:
                pivot.append(elem)

        low = quick_sorted(tmp_low, cmp=cmp)
        high = quick_sorted(tmp_high, cmp=cmp)

    if cmp == cmp_reverse:
        return high + pivot + low
    if cmp == cmp_standard:
        return low + pivot + high



def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented in-place,
    i.e. with O(1) memory requirement.
    Merge sort, on the other hand, has an O(n) memory requirement.
    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs variable instead of returning a copy of the list.
    '''

    def _qs_standard(xs, lo, hi):

        if lo < hi:
            p = _partition(xs, lo, hi)
            _qs_standard(xs, lo, p-1)
            _qs_standard(xs, p+1, hi)
            return xs

    def _qs_reverse(xs, lo, hi):

        if lo < hi:
            p = _partition_rev(xs, lo, hi)
            print("p=",p, "hi=", hi, "low=", lo)
            _qs_reverse(xs, lo, p-1)
            _qs_reverse(xs, p+1, hi)

            return xs

    if cmp == cmp_standard:
        return _qs_standard(xs, 0, len(xs)-1)

    else:
        return _qs_reverse(xs, 0, len(xs) - 1)


def _partition(xs, low, high):
    i = (low - 1)  # index of smaller element #i = -1
    pivot = xs[high]  # pivot # 1 bc high = 1

    for j in range(low, high):
        # print("xs[j] <= pivot=", xs[j] <= pivot, "xs[j]=", xs[j], "j=", j)
        if xs[j] < pivot:

            # increment index of smaller element
            i += 1
            xs[i], xs[j] = xs[j], xs[i]

    xs[i + 1], xs[high] = xs[high], xs[i + 1]
    return (i + 1)

def _partition_rev(xs, low, high):
    i = (low - 1)  # index of smaller element #i = -1
    pivot = xs[high]  # pivot # 1 bc high = 1

    for j in range(low, high):
        # print("xs[j] <= pivot=", xs[j] <= pivot, "xs[j]=", xs[j], "j=", j)
        if xs[j] > pivot:

            # increment index of smaller element
            i += 1
            xs[i], xs[j] = xs[j], xs[i]

    xs[i + 1], xs[high] = xs[high], xs[i + 1]
    return (i + 1)

xs=[1, 3, 2, 4, 0]
ys=[3, 4]
print(quick_sort(xs, cmp_reverse))
