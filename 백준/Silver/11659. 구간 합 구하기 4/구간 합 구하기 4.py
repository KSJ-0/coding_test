import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0] * N
sums[0] = nums[0]

for i in range(1, N):
    sums[i] = nums[i] + sums[i-1]

for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        print(sums[b-1])
    elif a == b:
        print(nums[a-1])
    else:
        print(sums[b-1]-sums[a-2])