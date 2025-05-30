def insertion_sort(arr: list[int]) -> list[int]:
    """Sort a list of integers using insertion sort algorithm

    The insertion sort algorithm takes one element at a time from the unsorted part
    of the array and places it into the right place in the sorted part of the array
    until the array is fully sorted.

    Args:
        arr (list[int]): The list of integers to be sorted
    
    Returns:
        list[int]: The sorted list of integers

    Examples:
        >>> insertion_sort([7, 12, 9, 11, 3])
        [3, 7, 9, 11, 12]
    """

    n = len(arr) # Calculate the length of list

    for i in range(1, n):
        temp = arr[i] # Take one element at a time from the unsorted part of the array
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j] # Shift elements to the right
            j -= 1

        arr[j + 1] = temp

    return arr

print(insertion_sort([7, 12, 9, 11, 3]))