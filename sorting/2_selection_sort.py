from algorithms.sort import selection_sort as selection_sort_base


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


print("\nMy code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Input array: ", arr)
print("Sorted array: ", selection_sort(arr))

print("\nBase code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Input array: ", arr)
print("Sorted array: ", selection_sort_base(arr))
