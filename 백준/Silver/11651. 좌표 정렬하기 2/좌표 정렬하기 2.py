import sys
N = int(sys.stdin.readline().strip())

points = []
for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    points.append([y,x])    

sorted_points = sorted(points)
for y,x in sorted_points:
    sys.stdout.write(f"{x} {y}\n")