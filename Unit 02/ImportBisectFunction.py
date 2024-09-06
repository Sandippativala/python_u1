import bisect

arr = [1, 3, 4, 4, 4, 6, 8,5,10,50,26]
x = 10

# Using bisect_left
left_index = bisect.bisect_left(arr, x)
print("Bisect Left Index:", left_index)  # Output: 2

# Using bisect_right
right_index = bisect.bisect_right(arr, x)
print("Bisect Right Index:", right_index)  # Output: 5