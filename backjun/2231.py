# 분해합
# 자연수N의 분해합은 N과 N을 이루는 각 자리수의 합
# 자연수M의 분해합이 N인 경우 M을 N의 생성자라고 한다

# 입력
# N(1<=N<=1,000,000)

# 출력
# N의 가장 작은 생성자. 없는 경우 0

import sys
N = int(sys.stdin.readline().strip())
num = len(str(N))

start_num = max(0, N - 9 * num)
start = str(start_num)
result = 0

for _ in range(max(0,N-9*num),N):
    productor = int(start)
    for i in range(len(start)):
        productor += int(start[i])
    if productor==N:
        result = start
        break
    start = str(int(start)+1)

print(result)