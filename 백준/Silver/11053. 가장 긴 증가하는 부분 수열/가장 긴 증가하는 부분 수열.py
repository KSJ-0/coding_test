import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
result = [1]*n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            result[i] = max(result[i], result[j]+1)

print(max(result))