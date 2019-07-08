def binary_search(n, target, source):
    left_idx = 0
    right_idx = n - 1
    found = False
    loop_count = 0

    while left_idx <= right_idx:
        mid_idx = int((left_idx + right_idx) / 2)
        if source[mid_idx] == target:
            found = True
            break
        if target > source[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return found


# test case 1
n = 5
target = 6
source = [1, 2, 3, 4, 6]

# test case 2

# n = 5
# target = 2
# source = [1, 3, 4, 5, 6]

print("1" if binary_search(n, target, source) else "-1")


'''
driver code

for t in range(int(input())):
    [n, target] = [int(x) for x in input().split()]
    source = [int(x] for x in input().split()]
'''