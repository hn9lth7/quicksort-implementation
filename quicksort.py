def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 22, 33, 44, 55, 66]

sorted_arr = quick_sort(arr)
    
print("Sorted massive:", sorted_arr)
