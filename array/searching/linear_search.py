def linear_search(arr: list[int], target: int) -> int:
    """Search an element from array using linear search algorithm"""

    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

arr = [1, 2, 3, 4, 5]
target = 6
low = 0
high = len(arr) - 1

result = linear_search([5, 3, 2, 4, 1], 5)
if result != -1:
    print("Found at index:", result)
else:
    print("Not Found!")