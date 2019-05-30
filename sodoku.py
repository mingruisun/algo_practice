def isSafe(x, y, v, s):
    for i in range(9):
        if i == x:
            pass
        elif s[y][i] == v:
            return False

        if i == y:
            pass
        elif s[i][x] == v:
            return False

    x_quad = int(x / 3)
    y_quad = int(y / 3)

    for i in range(3):  # y - axis
        for j in range(3):  # x - axis
            if y == i and x == j:
                continue
            if s[y_quad * 3 + i][x_quad * 3 + j] == v:
                return False

    return True


def printSol(s):
    # for i in range(len(s)):
    #     print(s[i])

    for i in range(len(s)):
        for j in range(len(s[i])):
            s[i][j] = str(s[i][j])
    sol = " ".join([" ".join(x) for x in s])
    print(sol)


def sodoku(x, y, s):
    new_x = x
    new_y = y

    while (s[new_y][new_x] != 0):
        if new_x + 1 == 9:
            new_x = 0
            new_y += 1
        else:
            new_x += 1
        if new_y > 8 or new_x > 8:
            break

    if new_y == 9:
        printSol(s)
        return True

    for i in range(1, 10):
        if isSafe(new_x, new_y, i, s):
            s[new_y][new_x] = i
            # print(new_y)
            if sodoku(new_x, new_y, s):
                return True
            s[new_y][new_x] = 0

    return False

#
for _ in range(int(input())):
    a = [int(x) for x in input().split()]

    s = []
    for i in range(9):
        s.append(a[i * 9:(i + 1) * 9])

    for i in range(len(s)):
        print(s[i])
    sodoku(0, 0, s)

