import os


# Complete the birthday function below.
def birthday(s, d, m):
    possibility = 0
    length = len(s)
    limit = length - (m-1)
    for i in range(0, limit+1):
        day = s[i]
        for j in range(1, m-1):
            print(i, j, i+j)
            day += s[i+j]
        if day == d:
            possibility += 1
    return possibility


if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    print(result)
