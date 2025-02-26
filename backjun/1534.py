# 문제
# 세준과 세비는 전쟁 게임을 한다.
# 세준은 N명의 병사가 있고, 세비는 M명의 병사가 있다.
# 전쟁은 여러번의 전투로 이루어진다. 
# 전투에서는 살아있는 병사중 가장 약한 병사가 죽는다.
# 제일 약한 병사가 여러명이고 그들이 같은 편에 있으면 그 중 한 명이 임의로 죽는다.
# 제일 약한 병사가 여러명이고 그들이 양쪽 편에 모두 있으면 세비의 제일 약한 병사 중 한 명이 임의로 죽는다.
# 전쟁은 한 명의 병사를 제외하고 모두 죽었을 때 끝난다.

# 입력 
# 첫째 줄에 테스트 케이스 개수 T가 주어진다.(T<=100)
# 각 테스트 케이스는 첫째 줄에 N과 M이 들어오고, (1<=N,M<=1,000,000)
# 둘째 줄에 세준이의 병사들의 힘이 들어오고
# 셋째 줄에 세비의 병사들의 힘이 들어온다.
# 힘은 정수이며 값이 클수록 강하다.

# 출력
# 각 테스트 케이스에 대해서 한 줄에 하나씩 차례로 승자를 출력한다.
# 세준이 이기면 S를 세비가 이기면 B를 둘 다 아니면 C를 출력한다.


import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    sys.stdin.readline()
    sys.stdin.readline()

    sejun = list(map(int,sys.stdin.readline().strip().split()))
    sebie = list(map(int,sys.stdin.readline().strip().split()))

    if(max(sejun)>=max(sebie)):
       print('S')
    else:
       print('B')

# 처음 작성한 코드

# 문제 풀이 방법
# T를 변수에 저장한다.
# for문을 T동안 돈다.
# N, M을 각각의 변수에 저장한다.
# 세준이와 세비의 병사들을 각각 리스트에 넣는다.
# 리스트를 내림차순으로 정렬한다.
# 맨 첫번째 값을 비교하고 둘 중 작은 거를 지운다.
# 두 값이 같은 경우 세비의 리스트에서 지운다.
# 두 리스트 중 하나라도 0이 되면 끝낸다.
# 세준이 이겼으면 S, 세비가 이겼으면 B, 둘 다 아니면 C를 출력한다.
# import sys

# T = int(sys.stdin.readline().strip())

# for _ in range(T):
#     sys.stdin.readline()
#     N, M = map(int, sys.stdin.readline().strip().split())
    
#     sejun = []
#     sebie = []

#     sejun = list(map(int,sys.stdin.readline().strip().split()))
#     sebie = list(map(int,sys.stdin.readline().strip().split()))

#     sejun.sort(reverse=True)
#     sebie.sort(reverse=True)

#     while True:
#         if(len(sejun)==0 and len(sebie)>=1):
#             print('B')
#             break
#         elif(len(sejun)>=1 and len(sebie)==0):
#             print('S')
#             break

#         if(sejun[0]>=sebie[0]):
#             sebie.pop()
#         else:
#             sejun.pop()