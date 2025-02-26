# 문제
# 회전 초밥 가게에 N명의 손님이 있고 요리사는 M개의 초밥을 순서대로 만든다
# 손님들은 순서대로 초밥을 받는다.
# 먼저 초밥을 밥는 손님이 초밥을 먹으면 뒤의 손님들은 해당 초밥을 먹을 수 없다.
# 아무도 해당 초밥을 먹지 않으면 초밥은 버려진다.
# 손님은 각자 먹고 싶은 초밥이 적힌 주문목록을 가졌으며 목록의 순서와 상관없이 목록에 적혀있는 초밥이 오면 먹는다.
# 만약 목록에 적히지 않은 초밥을 받으면 먹지 않는다.
# 손님은 각 종류의 초밥을 한 개만 먹을 수 있다.

# 입력
# 첫 번째 줄에 손님의 수 N(1<=N<=100,000)과 초밥의 수 M(1<=M<=200,000)이 공백으로 구분되어 주어짐
# 두 번째 줄부터 N개의 줄에 걸쳐 각 손님에 대한 주문 목록을 나타내는 정수 k와 초밥 종류 k개가 공백으로 구분되어 순서대로 주어짐
# 1<=모든 손님의 k의 합<=200,000
# N+2번째 줄에는 요리되는 초밥의 종류를 나타내는 M개의 정수가 공백으로 구분되어 주어짐

# 출력
# 각 손님이 먹은 초밥의 개수를 공백으로 구분하여 순서대로 출력한다.

# 초밥의 수는 최대 200,000이므로 1~200,000의 초밥 번호를 key로, 빈 힙(주문한 손님 번호 저장)을 value로 갖는 딕셔너리 sushi_orders를 선언.
# 손님이 먹은 초밥의 수를 저장하는 배열 customer_eat을 선언.
# 손님 수만큼 for문을 돌면서 각 손님의 주문을 읽고, 딕셔너리에 해당하는 초밥 번호 key의 value에 손님 번호를 추가한다.
# 만든 초밥을 배열 made로 저장함.
# made를 for문 돌면서 sushi_orders[made]의 value의 길이가 0이 아니면(주문한 손님이 아무도 없는 게 아니면) value의 힙에서 가장 위에 있는 손님 번호를 pop한다.
#  customer_eat[pop한 번호]+=1로 먹은 초밥의 수를 표시한다.

import sys
import heapq

N, M = map(int, sys.stdin.readline().strip().split())


sushi_orders = {}

for i in range(200001):
    sushi_orders[i]=[]
    heapq.heapify(sushi_orders[i])

customer_eat = [0]*200001

for i in range(N):
    k, *orders = map(int, sys.stdin.readline().strip().split())
    for order in orders:
        heapq.heappush(sushi_orders[order],i)

made_sushi = map(int, sys.stdin.readline().strip().split())

for made in made_sushi:
    if len(sushi_orders[made]) != 0:
        customer_eat[heapq.heappop(sushi_orders[made])]+=1
    
print(' '.join(map(str, [customer_eat[i] for i in range(N)])))