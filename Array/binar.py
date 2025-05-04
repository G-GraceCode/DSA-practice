#Tradition method
#Time: o(log n)
#space: o(1)
def binary_search(arr, target): 
    left, right = 0, len(arr) - 1 
    print("left", left, right)
    while left <= right: 
        mid = left + (right - left) // 2 
        if arr[mid] == target: 
            return mid 
        elif arr[mid] < target: 
            left = mid + 1 
        else: 
            right = mid - 1 
    return -1 
 
# Example usage 
arr = [1, 2, 4, 5, 8, 9, 14] 
target = 9
print(binary_search(arr, target)) 

b = [False, False, False, False, False, True]
#it's target for where index is true.

def binary_search_condition(arr):
    n = len(arr)
    l = 0
    r = n - 1

    while l < r:
        m = (r + l)//2

        if b[m]:
            r=m
        else: 
            l = m + 1
    return l

result = binary_search_condition(arr)
print(result)