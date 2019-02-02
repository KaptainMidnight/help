n = 7
k = 2
# First && Second task
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if i + j == n + 1 or j - i == n - 1:
            print("*", end="")
        elif i == n and j != k:
            print("*", end="")
            k += 2
        else:
            print(end=" ")
    print()
print()


def count(n):
    if n == 0:
        print()
    elif n < 0:
        print("Error")
    else:
        print(n)
        count(n - 1)

count(-5)


def reverse(lst):
    if not lst:
        return lst
    return lst[-1:] + reverse(lst[:-1])


print(reverse([1, 2, 3, 4, 5]))

for i in reversed(range(1, n + 1)):
    for j in range(1, 2 * n):
        if i + j == n + 1 or j - i == n - 1:
            print("*", end="")
        elif i == n and j != k:
            print("*", end="")
            k += 2
        else:
            print(end=" ")
    print()
