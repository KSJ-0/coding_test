# 문제
# f(n)=f(n-1)+f(n-3)인 수열
# f(1)=f(2)=f(3)=1
# 1, 1, 1, 2, 3, 4, 6, 9, 13, 19
# 자연수 n을 입력받고 n번째 값을 구할 것

import sys

n=int(sys.stdin.readline().strip())
nums = [1,1,1]

[nums.append(nums[count-1]+nums[count-3]) for count in range(3,n)]

print(nums[n-1])
