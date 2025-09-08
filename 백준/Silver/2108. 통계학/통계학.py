import sys
import math
input = sys.stdin.readline

N = int(input().strip())
num = []
num_dic = {}
sum = 0
for _ in range(N):
    n = int(input().strip())
    num.append(n)
    sum += n
    if n not in num_dic:
        num_dic[n] = 1 
    else:
        num_dic[n] += 1

maximum = max(list(num_dic.values()))
max_nums = []
for i in num:
    if num_dic[i] == maximum:
        if i not in max_nums:
            max_nums.append(i)

mean = sum/N
if mean >= 0:
    mean = math.floor(mean + 0.5)
else:
    mean = math.ceil(mean - 0.5)
max_nums.sort()
num.sort()

print(mean)
print(num[N//2])
print(max_nums[1] if len(max_nums)>1 else max_nums[0])
print(max(num)-min(num))