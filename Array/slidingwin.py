
def max_sum_subarray(arr, k):
    max_sum = float("-inf")
    print(max_sum, "summax")
    start_point = 0
    current_sum = 0

    for i in range(k):
        current_sum += arr[i]
    max_avg = current_sum / k
    
    for x in range(k, n):
        current_sum += arr[x]
        current_sum -= arr[x - k]
        avg = current_sum / k
        max_avg = max(max_sum, avg)
        
    return max_sum

# Example usage 
arr = [1, 12, -5, -6, 50, 3] 
k = 4
print(max_sum_subarray(arr, k)) 



# def max_sum_subarray(arr, k):
#     max_sum = float("-inf")
#     print(max_sum, "summax")
#     start_point = 0
#     current_sum = 0
#     end_point = len(arr) - 1
    
#     for x in range(end_point):
#         current_sum += arr[x]
#         if x >= k - 1:
#             max_sum = max(max_sum, current_sum)
#             current_sum -= arr[start_point]
#             start_point += 1
#     return max_sum

# # Example usage 
# arr = [1, 12, -5, -6, 50, 3] 
# k = 4
# print(max_sum_subarray(arr, k)) 

