import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0] * (N+1)

#누적합 계산
for i in range(1, N+1):
	sums[i] = nums[i-1] + sums[i-1]
    
for _ in range(M):
	num1, num2 = map(int, input().split())
	print(sums[num2] - sums[num1-1])