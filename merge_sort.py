def merge_sort(arr: list[int | float]) -> list[int | float]:
    """Sort a list of numbers using the merge sort algorithm.

    Merge sort algorithm follows a divide and conquer strategy. It recursively divides the array
    into smaller sub-arrays until each sub-array contains only one element, then merges the
    sub-arrays in a sorted manner.

    Args:
        arr (list[int | float]): The list of numbers to be sorted.

    Returns:
        list[int | float]: The sorted list of numbers.

    Examples:
        >>> merge_sort([-13, -10, 3, 6, 7, 15, 23.5, 55])
        [-13, -10, 3, 6, 7, 15, 23.5, 55]
    """

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left: list[int | float], right: list[int | float]) -> list[int | float]:
    """Merge two sorted sub-arrays into a single sorted array.

    Args:
        left (list[int | float]): The sorted left sub-array.
        right (list[int | float]): The sorted right sub-array.

    Returns:
        list[int | float]: The merged sorted array.
    """

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(merge_sort([-13, -10, 3, 6, 7, 15, 23.5, 55]))