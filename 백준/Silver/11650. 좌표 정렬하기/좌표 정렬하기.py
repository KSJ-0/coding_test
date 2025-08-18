import sys

N = int(sys.stdin.readline().strip())
points = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

sorted_points = sorted(points)

for x, y in sorted_points:
    sys.stdout.write(f"{x} {y}\n")