# Time: o(n)
# space: o(1)

# this method uses to numbers to find it sum, using number from the array
def two_pointer(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [arr[left], arr[right]]
        elif sum < target:
            left += 1
        else: 
            right -= 1
    return None

# Example usage 
arr = [1, 2, 4, 5, 8, 9, 14] 
target = 19
print(two_pointer(arr, target)) 

# find the square of an array and sorting it using twopointer
r = [-4, -5, 0, 2, -3, 1]

def square_sort(arr):
    n = len(arr)
    l = 0
    r = n - 1
    result = []

    while l <= r:
        if abs(arr[l]) > abs(arr[r]):
            result.append(arr[l] ** 2)
            l += 1
        else: 
            result.append(arr[r] ** 2)
            r -= 1
    result.reverse()
    return result

result = square_sort(r)
print(result)
