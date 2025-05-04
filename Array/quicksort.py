# a= [3, 6, 8, 10, -1, 2, 1]
a= [-5, 3, 2, 1, -3, -9, 7, 2, 2, 0]
def quicksort(arr):
    if len(arr) <= 1: 
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    # center = [x for x in arr if x == pivot]

    left = quicksort(left)

    right = quicksort(right)

    return left + [pivot] + right

result = quicksort(a)
print(result)