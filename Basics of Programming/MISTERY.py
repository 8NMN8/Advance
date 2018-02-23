import sys
count = 0
for line in sys.stdin:
    count = 0
    line = int(line)
    while line:
        line = line & (line - 1)
        count += 1
    print(count)
