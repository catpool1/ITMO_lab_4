from timeit import timeit


def fibonachi(idx):
    if idx <= 1:
        return idx

    return fibonachi(idx - 1) + fibonachi(idx - 2)


cashe = {}

def fibonachi_cashed(idx):
    if idx in cashe:
        return cashe[idx]

    if idx <= 1:
        return idx

    res = fibonachi_cashed(idx - 1) + fibonachi_cashed(idx - 2)
    cashe[idx] = res

    return res


def fibonachi_bt(idx):
    cashe = [0] * (idx + 1)
    cashe[1] = 1
    cashe[0] = 0

    for i in range(2, idx+1):
        res = cashe[i-1] + cashe[i-2]

        cashe[i] = res

    return cashe[-1]


idx = 0
if __name__ == '__main__':
    while True:
        idx = int(input('index: '))
        if idx >= 100:
            break
        res = timeit("fibonachi_bt(idx)", number=1, globals=globals())
        print(res, fibonachi_bt(idx))