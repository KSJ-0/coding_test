# 문제
# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어질 때 섬의 개수를 세는 프로그램을 작성하라.
# 가로, 세로, 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.


# 입력
# 테스트 케이스 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다.
# (1<=w,h<=50)
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 출력
# 각 테스트 케이스에 대해서 섬의 개수를 출력한다.

import sys
sys.setrecursionlimit(10**5)#재귀 깊이 제한 증가

while True:
    w, h = map(int,input().split())
    if w==0 and h==0:
        break

    maps = []

    for i in range(h):
        maps.append(list(map(int,input().split())))

    def dfs(x,y):
        if x<=-1 or y<=-1 or x>=h or y>=w:
            return False
        
        if maps[x][y]==1: #땅인 경우
            maps[x][y]=2 #방문 처리: 방문한 경우 값을 2로 변경한다
            dfs(x,y-1)
            dfs(x,y+1)
            dfs(x+1,y)
            dfs(x+1,y-1)
            dfs(x+1,y+1)
            dfs(x-1,y)
            dfs(x-1,y-1)
            dfs(x-1,y+1)
            return True
        
        #바다인 경우 종료
        return False

    result = 0
    for i in range(h):
        for j in range(w): #가로줄 모두 방문 후 다음 줄로 넘어감
            if dfs(i,j)==True:
                result+=1

    print(result)