#time=o(n^2)
#space = o(1)
a = [-13, 4, -3, 0, 6, 7]
b = [-5, 3, 1, -3, -3, 7, 2]
def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
            


selection(b)
print(b)