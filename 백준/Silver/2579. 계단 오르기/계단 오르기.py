import sys
input = sys.stdin.readline
n = int(input().strip())
stair = [int(input().strip()) for _ in range(n)]
result = [0] * n


if n >= 1:
    result[0] = stair[0]
if n >= 2:
    result[1] = stair[0]+stair[1]
if n >= 3:
    result[2] = max(stair[0], stair[1]) + stair[2]

for i in range(3, n):
    result[i] = max(result[i-2], result[i-3] + stair[i-1]) + stair[i]

print(result[n-1])