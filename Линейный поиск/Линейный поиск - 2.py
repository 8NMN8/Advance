N = int(input()) 
a = [int(i) for i in input().split()] 
x = int(input()) 
ans = "NO"
for i in range(N):
    if a[i] == x:
        ans = "YES"
print(ans)