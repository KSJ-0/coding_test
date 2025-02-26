# 문제
# 정수를 저장하는 큐를 구현하고 입력으로 주어지는 명령을 처리해라.
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력
# 첫째 줄에는 주어지는 명령의 수 N (1<=N<=10,000)
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어짐
# 주어지는 정수 M은 (1<=M<=100,000)

# 출력
# 출력하는 명령이 주어질 때마다 한 줄씩 출력

# 문제 풀이 방법
# deque로 큐 구현

import sys
from collections import deque

que = deque()
N = int(sys.stdin.readline().strip())

for _ in range(N):
    command = sys.stdin.readline().strip().split()

    if (command[0]=='push'):
        que.append(command[1])
    elif (command[0]=='pop'):
        if (len(que)>0):
            print(que.popleft())
        else:
            print(-1)
    elif (command[0]=='size'):
        print(len(que))
    elif (command[0]=='empty'):
        if(len(que)==0):
            print(1)
        else:
            print(0)
    elif (command[0]=='front'):
        if(len(que)==0):
            print(-1)
        else:
            print(que[0])
    elif (command[0]=='back'):
        if(len(que)==0):
            print(-1)
        else:
            print(que[-1])    
