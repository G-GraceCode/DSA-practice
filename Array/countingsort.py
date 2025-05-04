a = [3, 40, 6, 8, 10, 11, 1, 2, 1, 9, 0]

def count_sort(arr):
    # n = len(arr)
    max_num = max(arr)
    counts = [0] * (max_num + 1)

    for x in arr:
        print(x)
        counts[x] += 1

    i = 0

    for c in range(max_num + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1
    return arr

result = count_sort(a)
print(result)