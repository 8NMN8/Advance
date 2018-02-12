import math
w, h, n = map(int, input().split()) # ширина, высота, количество 

lo = -1                         
hi = n * h                         
while hi - lo > 1:              
    mid = (lo + hi) // 2        
    if math.floor(mid / w) * math.floor(mid / h) < n:
        lo = mid
    if math.floor(mid / w) * math.floor(mid / h) >= n:
        hi = mid
print(hi)
