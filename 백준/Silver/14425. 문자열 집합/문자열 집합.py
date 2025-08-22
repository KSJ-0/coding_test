import sys
N, M = map(int, sys.stdin.readline().split())
dict = {sys.stdin.readline().strip(): 0 for _ in range(N)}
count = 0
for _ in range(M):
    if sys.stdin.readline().strip() in dict:
        count += 1
sys.stdout.write(str(count))