N, K = map(int, input().split())         
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]
ans1 = [0 for x in range(K)]
ans2 = [" " for x in range(K)]

def bin_search(a1, a2, ans):
    date = 0
    for number in a2:
        lo = 0
        hi = N
        while hi - lo > 1:
            mid = (lo + hi) // 2       
            if a1[mid] <= number:
                lo = mid
            else:
                hi = mid      
        if a1[lo] == number:
            ans[date] = lo + 1
        date += 1
    return ans2
           
def bin_search2(a1, a2, ans):
    date = 0
    for number in a2:
        lo = -1
        hi = N - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2       
            if a1[mid] < number:
                lo = mid
            else:
                hi = mid     
        if a1[hi] == number:
            ans[date] = hi + 1
        date += 1
    return ans1

bin_search(a1, a2, ans2)
bin_search2(a1, a2, ans1)

for i in range(K):
    print(ans1[i], ans2[i])
