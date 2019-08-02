from algorithms.sort import bubble_sort as bubble_sort_base


def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        swapped = False
        for j in range(0, len(arr)-1):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break
    return arr


print("\nMy code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Input array: ", arr)
print("Sorted array: ", bubble_sort(arr))

print("\nBase code: ")
arr = [7, 0, 9, 4, 2, 5, 1, 6, 3, 8]
print("Input array: ", arr)
print("Sorted array: ", bubble_sort_base(arr))
