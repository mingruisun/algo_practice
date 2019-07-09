def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)

        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]

    low_wall = low
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[low_wall], arr[i] = arr[i], arr[low_wall]
            low_wall += 1
    arr[low_wall], arr[high] = arr[high], arr[low_wall]
    return low_wall

# arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr = [4,1, 3, 9, 7]

quick_sort(arr, 0, len(arr) - 1)
print(arr)