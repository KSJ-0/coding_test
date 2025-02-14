# 문제
# 산타는 세계 곳곳의 거점에 방문하여 선물을 충전해 나간다.
# 착한 아이들을 만날 때마다 자신이 들고 있는 가장 가치가 큰 선물을 준다.
# 차례로 방문한 아이들과 거점지의 정보들이 주어졌을 때 아이들에게 준 선물의 가치들을 출력

# 입력
# 첫 번째 줄은 아이들과 거점지를 방문한 횟수 n
# 다음 n줄에는 a가 들어오고 그 다음 a개의 숫자가 들어온다 (e.g 3 1 2 3(3이 a))
# 이는 거점지에 a개의 선물을 충전한 것이고 숫자들이 선물의 가치이다.
# a가 0이라면 거점지가 아닌 아이들을 만난 것이다.
# 0<=선물<=100,000
# 1<=a<=100

# 출력
# a가 0일 때마다 아이들에게 준 선물의 가치를 출력한다.
# 줄 선물이 없으면 -1 출력

import sys
import heapq

n = int(sys.stdin.readline().strip())
present = []
heapq.heapify(present)

for _ in range(n):
    a = sys.stdin.readline().strip().split()
    a_copy = a.copy()
    a = [-int(i) for i in a_copy]

    if(int(a[0])==0):
        if (len(present)==0):
            print(-1)
        else:
            print(-heapq.heappop(present))
    else:
        for i in range(1,len(a)):
            heapq.heappush(present, int(a[i]))