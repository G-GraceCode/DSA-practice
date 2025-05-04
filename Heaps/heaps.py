# Heap/Priority queues:help to select element that has more priority than others. To make an array a heap we use a fxn , heapify()
# property: 
    #  Extract min: heap pop - time: o(log n)
    # Insert: heap push - time: o(log n)
    #heap peek: o(1)
# we can use tuple in heaps,

# 2 types: max/min heap
    #What is heapify:
    # To find Min heap -> Heapify (use heapify method to find min heap), time: o(n), space: o(1)

# Building a min heap, time: o(n), space: o(1)

A = [3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq

heapq.heapify(A)
print("heap", A)

#Insert, heap push, time: o(log n)
heapq.heappush(A, 4)
print("heapAdd", A)

#Extract, heap pop, time: o(log n)
min = heapq.heappop(A)

print(A, min)



# Heapsort, 
    #time: o(n log n) one of the best time complexity, space: o(n)
    #Note: o(1) space is possible via swapping, but it's complex

def heap_sort(arr):
    heapq.heapify(arr)
    n = len(arr)
    result = [0] * n

    for i in range(n):
        min = heapq.heappop(arr)
        result[i] = min
    return result
result = heap_sort([0, -4, 8, 5, 9, 10, 2, 1, 7])
print("heap sort", result)

#heap push pop, heapq.heappushpop(A)

# build heap from scratch - time: n(n log n)
C = [-5, 4, 2, 1, 2, 7, 0, 3]
heap = []
for x in C:
    heapq.heappush(heap, x)
print(heap)

#Tuples

from collections import Counter

list = "aabbbbcddddrrrtt"

counter = Counter(list)
heap = []

for k, v in counter.items():
    heapq.heappush(heap, (v, k))

print("heap-tuple", heap)
