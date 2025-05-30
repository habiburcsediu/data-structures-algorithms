def selection_sort(arr: list[int]) -> list[int]:
    """Sorts a list of integers using selection sort algorithm

    The selection sort algorithm repeatedly iterates through the array, finds the minimum element in every iteration and move it to the in front of the list until the list is sorted.

    Args:
        arr (list[int]): The list of integers to be sorted

    Returns:
        list[int]: The sorted list of intergers
    
    Examples:
        >>> selection_sort([3, 7, 9, 11, 12])
        [3, 7, 9, 11, 12]
    """

    n = len(arr) # Calculate the length of the array

    for i in range(n):
        min_index = i # For every iteration, consider the first element is the minimum element

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]: # Compare to find the minimum element from the list
                min_index = j # Update the minimum element

        popped_item = arr.pop(min_index) # Remove the minimum element
        arr.insert(i, popped_item) # Push it in front of the list

    return arr

print(selection_sort([3, 7, 9, 11, 12]))

# We can optimize selection sort algorithm to use swapping insted of all shifting
def optimized_selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i] # Swap the minimum element with the first element of the list in every iteration

    return arr

print(optimized_selection_sort([3, 7, 9, 11, 12]))

