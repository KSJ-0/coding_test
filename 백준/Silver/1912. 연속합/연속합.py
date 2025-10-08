import sys
input = sys.stdin.readline
n = int(input().strip())
nums = list(map(int, input().split()))

current_sum = nums[0]
max_sum = nums[0]

for i in range(1, n): 
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(current_sum, max_sum)

print(max_sum)