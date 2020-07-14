l = 0
space = 0
N = int(input())

def christmas_tree(a, N):
    global space
    for row in range(a, N + 1):
        # Blank Space
        for sp in range(1, N + space - row + 1):
            print(" ", end='')
        # Star Printing
        for Stars in range(1, 2 * row):
            print("*", end='')
        print()
    space += 1

if (N <= 1):
    print("You cannot generate Christmas tree")
elif (N > 20):
    print("The Tree is no More")
else:
    # First One pyramid
    christmas_tree(1, N + 1)
    # Others pyramid (Branches)
    for i in range(2, N ):
        christmas_tree(2, N - l)
        l += 1

    # Stand of the Tree
    print(' ' * N + '*')
    print(' ' * N + '*')