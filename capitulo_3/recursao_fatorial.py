def fat(x):
    if x == 1:
        return 1
    return x * fat(x - 1)


print(fat(4))
