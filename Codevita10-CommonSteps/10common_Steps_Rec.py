def ways(n):
    if (n == 1 or n == 0):
        return 1
    elif (n == 2):
        return 2

    else:
        return ways(n - 3) + ways(n - 2) + ways(n - 1)


n = int(input())
print(findStep(n))
