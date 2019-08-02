from algorithms.sort import insertion_sort as insertion_sort_base
"""
0, 7
0, 7, 9
0, 4, 7, 9
0, 2, 4, 7, 9
0, 2, 4, 5, 7, 9
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        e = arr[i]

        k = j
        while j > 0:
            j -= 1
            if e < arr[j]:
                k -= 1
                arr[j+1] = arr[j]
            else:
                break
        arr[k] = e
    return arr


print("\nMy code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Input array: ", arr)
print("Sorted array: ", insertion_sort(arr))

print("\nBase code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Input array: ", arr)
print("Sorted array: ", insertion_sort_base(arr))
