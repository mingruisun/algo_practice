'''
Input:
2
5
4 1 3 9 7
10
10 9 8 7 6 5 4 3 2 1

Output:
1 3 4 7 9
1 2 3 4 5 6 7 8 9 10

Explanation:
Testcase 1: The array after performing mergesort is: 1 3 4 7 9.
'''


def merge(arr_1, arr_2):
    temp_arr = []
    arr_1_idx = 0
    arr_2_idx = 0

    while arr_1_idx < len(arr_1) or arr_2_idx < len(arr_2):
        if arr_1_idx >= len(arr_1):
            temp_arr.extend(arr_2[arr_2_idx:])
            break
        elif arr_2_idx >= len(arr_2):
            temp_arr.extend(arr_1[arr_1_idx:])
            break
        elif arr_1[arr_1_idx] <= arr_2[arr_2_idx]:
            temp_arr.append(arr_1[arr_1_idx])
            arr_1_idx += 1
        else:
            temp_arr.append(arr_2[arr_2_idx])
            arr_2_idx += 1

    return temp_arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    left_idx = 0
    right_idx = len(arr) - 1
    mid = int((left_idx + right_idx) / 2) + 1

    arr_1 = arr[:mid]
    arr_2 = arr[mid:]

    return merge(merge_sort(arr_1), merge_sort(arr_2))



# arr = [4, 1, 3, 9, 7]
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(merge_sort(arr))

