def bubble_sort(arr: list[int]) -> list[int]:
    """Sort a list of integers using bubble sort algorithm

    The bubble sort algorithm repeatedly iterates through the list, compares
    adjacent elements and swaps them if they are in the wrong order until the
    list is sorted. In this way, in every iteration, the largest element
    'bubbles up' to the end of the list.

    Args:
        arr (list[int]): The list of integers to be sorted

    Returns:
        list[int]: The sorted list of integers

    Examples:
        >>> bubble_sort([7, 12, 9, 11, 3])
        [3, 7, 9, 11, 12]
    """

    n = len(arr) # Calculate the length of the list

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap the adjacent elements

    return arr

print(bubble_sort([7, 12, 9, 11, 3]))