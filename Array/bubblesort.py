#time=o(n^2)
#space = o(1)
a = [-13, 4, -3, 0, 6, 7]

def bubble(arr):
    n = len(arr)
    start = True
    while start:
        start = False
        for i in range(1, n):
            if arr[i - 1] > a[i]:
                arr[i - 1], arr[i] = arr[i], arr[i-1]
                start = True

bubble(a)
print(a)