N, K = map(int, input().split())
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]

for number in a2:
    lo = 0
    hi = len(a1)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if a1[mid] <= number:
            lo = mid
        else:
            hi = mid
    if lo + 2 <= N  and number - a1[lo] > a1[lo + 1] - number:
        print(a1[lo + 1])
    else:
        print(a1[lo])   