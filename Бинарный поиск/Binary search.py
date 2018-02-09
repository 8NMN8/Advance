# a = [1, 1, 1, 1, 0, 0, 0, 0]   хотим найти последнюю единичку

a = [int(x) for x in input().split()]
lo = 0                           
hi = len(a) 

while hi - lo > 1:               
    mid = (lo + hi) // 2         
    if a[mid]:
        lo = mid
    else:
        hi = mid
    
print(lo)   

'''
bool check(int x);

int l = 0, r = n + 1;
while (r - l > 1) {
   int m = (l + r) / 2;
   if (check(m))
      l = m;
   else
      r = m;
}
return l;
'''