from algorithms.sort import shell_sort as shell_sort_base


def shell_sort(arr):
    return arr


print("\nMy code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Input array: ", arr)
print("Sorted array: ", shell_sort(arr))

print("\nBase code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Input array: ", arr)
print("Sorted array: ", shell_sort_base(arr))
