import sys

N = int(sys.stdin.readline().strip())
numbers = []

[numbers.append(int(sys.stdin.readline().strip())) for i in range(N)]
numbers.sort()

for number in numbers:
    print(number)