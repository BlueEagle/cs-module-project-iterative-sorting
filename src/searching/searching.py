def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    viewing = int(len(arr)/2)
    for i in range(0, len(arr)):
        if target > arr[viewing]:
            viewing += 1
            arr = arr[viewing:]
        elif target < arr[viewing]:
            viewing -= 1
            arr = arr[:viewing+1]
        else:
            return viewing

    return -1  # not found
