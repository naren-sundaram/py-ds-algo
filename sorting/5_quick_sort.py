from algorithms.sort import quick_sort as quick_sort_base
from utils.timeit import timeit


@timeit
def quick_sort(arr):
    length = len(arr)
    left, right = 0, length - 1
    return do_recursion(arr, left, right)


def do_recursion(arr, left, right):
    if left < right:
        position = do_partition(arr, right)
        do_recursion(arr, left, position-1)
        do_recursion(arr, position, right)
    return arr


def do_partition(arr, right):
    index_lowest = 0
    pivot = arr[right]

    for i in range(0, right):
        if arr[i] <= pivot:
            arr[index_lowest], arr[i] = arr[i], arr[index_lowest]
            index_lowest += 1
    arr[index_lowest], arr[right] = pivot, arr[index_lowest]
    return index_lowest


print("\nMy code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8] * 100
print("Input array: ", arr)
print("Sorted array: ", quick_sort(arr))

print("\nBase code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8] * 100
print("Input array: ", arr)
print("Sorted array: ", timeit(quick_sort_base)(arr))
