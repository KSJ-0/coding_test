import sys
p = sys.stdin.readline().split("-")
result = sum(map(int, p[0].split("+")))

for i in range(1, len(p)):
    values = p[i].split("+")
    result -= sum(map(int, values))

print(result)