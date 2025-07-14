#문제
#9x9격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때
#최대값을 찾고 몇행 몇열에 위치한 수인지 구하는 프로그램

#입력
#첫째 줄에서 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어짐 
# 0<= <100

#출력
#첫째 줄에 최댓값
#둘째 줄에 최댓값이 위치한 행, 열
#최대값이 2개 이상인 경우 그 중 한 곳의 위치 출력
import sys
arr = [list(map(int, input().split())) for _ in range(9)]
max=0
maxi=0
maxj=0
for i in range(9):
    for j in range(9):
        if (arr[i][j]>=max):
            max=arr[i][j]
            maxi=i+1
            maxj=j+1

print(max)
print(maxi,maxj)