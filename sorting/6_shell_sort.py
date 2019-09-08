from algorithms.sort import shell_sort as shell_sort_base
from utils.timeit import timeit


@timeit
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        y_idx = gap
        while y_idx < n:
            y = arr[y_idx]
            x_idx = y_idx - gap
            while x_idx >= 0 and y < arr[x_idx]:
                arr[x_idx+gap] = arr[x_idx]
                x_idx -= gap
            arr[x_idx+gap] = y
            y_idx += 1
        gap //= 2

    return arr


arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Base: ", timeit(shell_sort_base)(arr))
print("")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
# arr = [5, 4, 3, 2, 1]
print("Mine: ", shell_sort(arr))
