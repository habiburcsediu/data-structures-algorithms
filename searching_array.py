def linear_search(arr: list[int], target: int) -> int:
    """Search an element from array using linear search algorithm"""

    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

result = linear_search([5, 3, 2, 4, 1], 5)
if result != -1:
    print("Found at index:", result)
else:
    print("Not Found!")


def binary_search_recursively(arr, target, low, high):
    """Search an element from an array using binary search algorithm recursively"""
    if low > high:
        return -1 # Target is not found
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursively(arr, target, low, mid - 1)
    else:
        return binary_search_recursively(arr, target, mid + 1, high)
    

arr = [1, 2, 3, 4, 5]
target = 6
low = 0
high = len(arr) - 1

result = binary_search_recursively(arr, target, low, high)
if result != -1:
    print("Found at index:", result)
else:
    print("Not found!")


def binary_search_iteratively(arr: list[int], target: int, low: int, high: int) -> int:
    """Search an element from an array using binary search algorithm iteratively"""
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1
    
arr = [1, 2, 3, 4, 5]
target = 4
low = 0
high = len(arr) - 1

result = binary_search_iteratively(arr, target, low, high)
if result != -1:
    print("Found at index:", result)
else:
    print("Not found!")