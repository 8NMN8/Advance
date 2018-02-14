n, m = map(int, input().split())
num_minimum = []
a = []
count = 0
for i in range(n):
    a.append([int(x) for x in input().split()])  
    minimum = a[i][0]
    for j in range(m):
        if a[i][j] < minimum:
            minimum = a[i][j]
    num_minimum.append(minimum)   
            
for i in range(m):
    maximum = a[0][i]
    for j in range(n):
        if a[j][i] > maximum:
            maximum = a[j][i]
    for i in num_minimum:
        if maximum == i:
            count += 1
print(count)
    