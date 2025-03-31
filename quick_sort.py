def partition(arr: list[int], low: int, high: int) -> list[int]:
    """Partition a list of integers for quick sort

    Args:
        arr (list[int]): The list of integers to be partitioned
        low (int): The starting index of the partition
        high (int): The ending index of the partition

    Returns:
        int: The final index of the pivot after partitioning
    """

    pivot = arr[low] # Assume first element as pivot
    start = low + 1
    end = high

    while start <= end:
        while start <= high and arr[start] <= pivot:
            start += 1
        while end >= low and arr[end] > pivot:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        else:
            break

    arr[low], arr[end] = arr[end], arr[low]

    return end

def quick_sort(arr: list[int], low: int, high: int):
    """Sort a list of integers using quick sort algorithm

    Quick sort algorithm consider any element as a pivot.
    The main target is to partition the array in such a way, 
    partition 1 elements are less or equal than pivot and partition 2 elements are greater than pivot.

    Args:
        arr (list[int]): The list of integers to be sorted
        low (int): The starting index of the sub-array
        high (int): The ending index of the sub-array
    """

    if low < high:
        lock = partition(arr, low, high)
        quick_sort(arr, low, lock - 1)
        quick_sort(arr, lock + 1, high)

arr = [7, 6, 7, 5, 9, 2, 1, 15, 10]
low = 0
high = len(arr) - 1

quick_sort(arr, low, high)
print(arr)