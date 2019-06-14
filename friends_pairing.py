def friends_pairing_naive(n):
    if n <= 1:
        return 1

    return friends_pairing_naive(n - 1) + (n - 1) * friends_pairing_naive(n - 2)

print(friends_pairing_naive(3))