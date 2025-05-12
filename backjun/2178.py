# 문제
# NxM 미로가 있다
# 미로에서 1은 이동할 수 있는 칸이고 0은 이동할 수 없는 칸이다.
# (1,1)에서 출발하여 (N,M)의 위치로 이동할 때 지나야 하는 최소 칸 수를 구하는 프로그램을 작성해라.
# 입력 
# 첫째줄에 두 정수 N,M(2<=N,M<=100)이 주어진다.
# 다음 N개의 줄에는 M개의 정수가 미로로 주어진다.
# 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소 칸 수를 출력한다
# 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().strip().split()))
move = [(0,1),(0,-1),(1,0),(-1,0)] #움직일 수 있는 방향
maze = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)] #방문 기록

queue = deque()
queue.append((0,0,1)) #시작 지점 삽입
visited[0][0] = True #시작 지점 방문 처리

while queue:
    x, y, distance = queue.popleft() #현재 위치와 거리 꺼내기

    if x==N-1 and y==M-1: #도착하면 지나온 칸 수 출력
        print(distance)

    for nx,ny in move: #갈 수 있는 방향 모두 시도
        mx, my = x+nx, y+ny #현재 위치+갈 방향

        if 0<=mx<N and 0<=my<M: 
            if maze[mx][my] == 1 and not visited[mx][my]:
                visited[mx][my] = True
                queue.append((mx,my,distance+1))