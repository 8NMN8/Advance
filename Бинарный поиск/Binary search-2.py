N = int(input())  
count = 0
lo = 0
hi = N
while hi - lo > 1:
    mid = (lo + hi) // 2
    lo = mid
    count += 1
print(count)    