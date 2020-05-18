def linear_search(arr, target):
    for val in arr:
        if(val == target):
            return arr.index(target)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1

        else:
            return mid

    return -1 
