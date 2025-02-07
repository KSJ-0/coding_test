# 문제
# 높이만 다르고 모양이 같은 막대기를 일렬로 세우고 왼쪽부터 차례로 번호를 붙였다.
# 오른쪽에서 보면 보이는 막대기(보는 방향에서 맨 앞에 있는 막대기보다 뒤에 있고, 높이가 높은 것)가 있고 보이지 않는 막대기가 있다.
# N개의 막대기에 대한 높이 정보가 주어질 때 오른쪽에서 몇 개가 보이는지 알아내라.

# 입력
# 첫 번째 줄은 막대기의 개수 N(2<=N<=100,000)
# 두 번째 줄부터 N줄동안 막대기의 높이 h(1<=h<=100,000)

# 출력
# 보이는 막대기의 개수

# 풀이 방법
# 배열에 모든 막대기를 순서대로 넣는다.
# 맨 위에 것부터 한 개씩 빼면서 가장 높았던 막대기를 갱신하며 그 막대기보다 높이가 높은 것의 개수를 센다.

import sys
N = int(sys.stdin.readline().strip())
stick = []
count = 1

for _ in range(N):
    stick.append(sys.stdin.readline().strip())
    
origin = stick.pop()

for _ in range(N-1):
    present = stick.pop()
    if(present>origin):
        origin=present
        count+=1

print(count)