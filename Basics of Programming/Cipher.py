s = [i for i in input()]
n = int(input())
ans = []
for i in s:
    if ord(i) in range(ord("0"), ord("9") + 1):
        ans.append(chr((ord(i) - ord("0") + n) % 10 + ord("0")))
    elif ord(i) in range(ord("A"), ord("Z") + 1):
        ans.append(chr((ord(i) - ord("A") + n) % 26 + ord("A")))
    elif ord(i) in range(ord("a"), ord("z") + 1):
        ans.append(chr((ord(i) - ord("a") + n) % 26 + ord("a")))
    else:
        ans.append(i)        
print("".join(ans))
