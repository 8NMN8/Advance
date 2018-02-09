N = int(input()) 
a = [int(i) for i in input().split()] 
minimum1 = minimum2 = 2000
for i in range(N):
    if a[i] < minimum1:
        minimum2, minimum1 = minimum1, a[i]
    elif a[i] < minimum2:
        minimum2 = a[i]
print(minimum1, minimum2)