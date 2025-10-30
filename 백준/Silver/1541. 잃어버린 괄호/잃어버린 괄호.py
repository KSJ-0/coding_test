import sys
p = sys.stdin.readline().split("-")
result = 0
values = p[0].split("+")
if len(p) == 1:
    result = sum(map(int,values))
else:
    for value in values:
            result += int(value)
    for i in range(1, len(p)):
        minus_values = p[i].split("+")
        result -= sum(map(int, minus_values))
print(result)