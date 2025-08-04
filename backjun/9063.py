# 입력 
# 첫째줄에 점의 개수 N(1<=N<=100,000)
# N줄에 각 점의 좌표가 두 개의 정수로 하나씩

# 출력
# N개의 점을 둘러싸는 최소 크기의 직사각형의 넓이

import sys
N = int(sys.stdin.readline().strip())
x_points = []
y_points = []

for _ in range(N):
    a,b = map(int, sys.stdin.readline().split())
    x_points.append(a)
    y_points.append(b)

result = (max(x_points)-min(x_points))*(max(y_points)-min(y_points))

if N<=1:
    print(0)
else: print(result)
