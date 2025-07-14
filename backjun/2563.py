#문제
#가로, 세로의 길이가 각각 100인 정사각형 모양의 도화지에
#가로, 세로의 크기가 10인 정사각형 모양의 검은색 색종이를 평행하게 붙인다
#색종이가 붙은 검은 영역의 넓이

#입력
#첫째 줄에 색종이의 수<=100
#둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치
#첫번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
#두번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리

import sys
white = [[0]*100 for _ in range(100)]
paper_num = int(sys.stdin.readline().strip())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(paper_num)]

for i in range(paper_num):
    for j in range(paper[i][0],paper[i][0]+10):
        for k in range(paper[i][1],paper[i][1]+10):
            white[j][k]=1

result = 0
for i in range(100):
    for j in range(100):
        if (white[i][j]==1):
            result+=1
            
print(result)