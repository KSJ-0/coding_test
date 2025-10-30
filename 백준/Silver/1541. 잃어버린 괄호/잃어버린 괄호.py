import sys
p = sys.stdin.readline().split("-")
result = 0
if len(p) == 1:
    values = p[0].split("+")
    result = sum(map(int,values))
else:
    values = p[0].split("+")
    for value in values:
            result += int(value)
    for i in range(1, len(p)):
        values = p[i].split("+")
        for value in values:
            result -= int(value)
print(result)