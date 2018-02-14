N = int(input()) 
a = [int(i) for i in input().split()] 
x = int(input()) 
diff = 2000
ans = a[0]
for i in range(N):
    if abs(a[i] - x) < diff:
        diff = abs(a[i] - x)
        ans = a[i]
print(ans)