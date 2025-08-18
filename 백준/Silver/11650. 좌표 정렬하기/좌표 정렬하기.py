import sys

N = int(sys.stdin.readline().strip())
points = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

sorted_points = sorted(points)

for point in sorted_points:
    print(point[0], point[1])