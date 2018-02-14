N = int(input()) 
a = [int(i) for i in input().split()] 
ans = a[0]
for i in range(N):
    if a[i] > ans:
        ans = a[i]
print(ans)