#time=o(n^2)
#space = o(1)
a = [-13, 4, -3, 3, 6, 2]

def insert(arr):
    n = len(arr);
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else: 
                break


insert(a)
print(a)