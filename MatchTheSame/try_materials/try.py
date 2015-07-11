a = [
    [2, 2, 2, 5],
    [None, None, 2, 3],
    [5, None, None, 3],
    [4, 4, 4, 3]
]

for i in range(3, -1, -1):
    # print(i)
    for j in range(3, -1, -1):
        if a[i][j] is None and i > 0:
            print(i, j)
            k = 1
            while a[i][j] is None and (i - k > -1):
                a[i][j] = a[i - k][j]
                # print("a[i][j] =", a[i - k][j])
                k += 1
                if i - k <= -1:
                    break
            # print("i-k: ", i, k, i - k + 1)
            a[i - k + 1][j] = None

print(a)