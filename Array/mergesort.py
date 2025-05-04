def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    pivot = len(arr) // 2
 
    left =  merge_sort(arr[:pivot]) #[x for x in arr if x < povit]
    right = merge_sort(arr[pivot:]) #[x for x in arr if x >= povit]
    # return merge(left, right)
    print("print", left, right)
    # return left + right

def merge(l, r) :
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result = result.append(l[i])
        else: 
            result = result.append(r[j])
        
        return result

arr = [3, 6, 8, 10, 4, 2, 1] 
print(merge_sort(arr)) 
