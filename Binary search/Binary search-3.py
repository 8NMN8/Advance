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
    if a1[lo] == number:
        print("YES")
    else:
        print("NO")