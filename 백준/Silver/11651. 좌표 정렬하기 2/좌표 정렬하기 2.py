import sys
N = int(sys.stdin.readline().strip())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

points.sort(key = lambda p: (p[1], p[0]))
for x,y in points:
    sys.stdout.write(f"{x} {y}\n")