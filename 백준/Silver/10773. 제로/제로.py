import sys
K = int(sys.stdin.readline().strip())
stack = []
for _ in range(K):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

result = 0
for num in stack:
    result += num
print(result)