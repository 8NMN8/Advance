a = [int(x) for x in input().split()]
n = a.pop(0)
maximum = minimum = a[0]

for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
    if a[i] < minimum:
        minimum = a[i]
        
for i in range(n):
    if a[i] == maximum:
        a[i] = minimum
print(*a)