# DFS 문제
# NxM 크기의 얼음 틀이 있을 때 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
# 얼음 틀의 모양이 주어졌을 때 생성되는 아이스크림의 개수를 구하시오.

# 입력
# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1<=N,M<=1,000)
# 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

# 출력
# 아이스크림 개수

import sys

N, M = map(int,input().split())

ice_maker = [] #얼음 틀 저장

for i in range(N):
    ice_maker.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or y<=-1 or x>=N or y>=M:
        return False
    
    if ice_maker[x][y]==0: #뚫려있는 칸인 경우에는
        ice_maker[x][y]=31 #해당 칸 방문 처리
        dfs(x-1,y) #상,하,좌,우 모두 재귀 호출
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1) 
        return True #상,하,좌,우의 뚫려있는 칸 모두 방문 처리한 후 True 리턴
    
    return False #뚫려있는 칸 아니면 종료

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j)==True:
            result+=1

print(result)

