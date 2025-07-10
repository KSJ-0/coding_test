#문제
#N*M 크기의 두 행렬 A와 B가 주어졌을 때 두 행렬을 더하는 프로그램

#입력
#첫째줄에 행렬의 크기 N과 M (N,M<=100)
#둘째줄부터 N개의 줄에 행렬 A의 원소 M개
#이어서 N개의 줄에 행렬 B의 원소 M개

#출력
#첫째줄부터 N개의 줄에 A와 B를 더한 행렬
#각 원소는 공백으로 구분

import sys
N, M = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
B = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    result = ""
    for j in range(M):
        sum = A[i][j]+B[i][j]
        result += (str(sum)+" ")
    print(result) 