X = float(input())
N = int(input())
ans = ["NO" for i in range(N)]
for i in range(N):
    string = [int(i) for i in input().split()]
    for j in range(N):
        if string[j] == X:
            ans[j] = "YES"            
for i in range(N):
    print(ans[i])