lst1=[]
lst1 = [int(item) for item in input("Enter the list items : ").split()]
lst1.sort()
print(lst1)

def binary_search(arr, target):
    """
    Searches for the target element in the given sorted array.

    Args:
        arr (list): A sorted list of elements.
        target: The element to be searched.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
index = binary_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")