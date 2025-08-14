import sys

total = 0
numbers = []

for _ in range(5):
    num = int(sys.stdin.readline().strip())
    total += num
    numbers.append(num)

numbers.sort()
print(total//5)
print(numbers[2])