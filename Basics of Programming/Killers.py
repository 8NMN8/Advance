# Round Table Killers
N, K, X = map(int, input().split())  
people = [1 for i in range(N)]
while sum(people) != 1:
    for j in range((((X - 1) % N + 1) % K)):
        while people[X % N] == 0:
            X += 1
        people[X % N] = 0
        X += 1
    X += 1
    
for i in range(N):
    if people[i] == 1:
        print(i + 1)
        
        
     