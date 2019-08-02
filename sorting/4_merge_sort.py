from algorithms.sort import merge_sort as merge_sort_base


def merge_sort(arr):
    return arr


print("\nMy code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Input array: ", arr)
print("Sorted array: ", merge_sort(arr))

print("\nBase code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Input array: ", arr)
print("Sorted array: ", merge_sort_base(arr))
