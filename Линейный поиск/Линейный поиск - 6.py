N = int(input()) 
a = [int(i) for i in input().split()]
maximum = a[0]
ans = 1
for i in range(N):
    if a[i] > maximum:
        maximum = a[i]
        ans = i + 1
print(ans)