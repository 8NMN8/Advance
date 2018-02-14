n = int(input())
a = [int(x) for x in input().split()]
maximum1 = -1
maximum2 = -1
for i in range(n):
    if a[i] > maximum1:
        maximum1, maximum2 = a[i], maximum1
    if a[i] > maximum2 and a[i] != maximum1:
        maximum2 = a[i]
print(maximum2)