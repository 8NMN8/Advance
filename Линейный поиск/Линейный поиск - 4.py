N = int(input())
a = [int(i) for i in input().split()] 
x = int(input()) 
for i in range(N):
    if a[i] == x:
        print(i + 1)
      