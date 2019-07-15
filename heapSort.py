def heapify(arr, n, i):
    '''
    :param arr: original array
    :param n: size of original array
    :param i: subtree rooted at ith index
    :return:
    '''

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def buildHeap(arr,n):
    '''
    :param arr: given array
    :param n: size of array
    :return: None
    '''

#     build the max heap
    for i in range(n - 1, -1, -1):
        heapify(arr, n, i)

    while n > 1:
        arr[0], arr[n - 1] = arr[n - 1], arr[0]
        n = n - 1
        heapify(arr, n, 0)
# arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# n = 10

arr = [4, 1, 3, 9, 7]
n = 5

buildHeap(arr, n)
print(arr)