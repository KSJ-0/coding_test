# 문제
# 높이만 다르고 모양이 같은 막대기를 일렬로 세운 후 왼쪽부터 차례로 번호를 붙인다.
# 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다.
# N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 몇 개가 보이는지 알아내라.

# 입력
# 첫 번째 줄에 막대기의 개수 N
# 이어지는 N줄에는 막대기의 높이를 나타내는 정수 h(1<=h<=100,000)

# 출력
# 오른 쪽에서 봤을 때 보이는 막대기의 수

import sys

N = int(sys.stdin.readline().strip())
sticks = [int(sys.stdin.readline().strip()) for _ in range(N)]
result = 0
biggest = 0


for _ in range(N):
    pop_stick=sticks.pop()
    if (pop_stick>biggest):
        biggest=pop_stick
        result+=1
    
print(result)