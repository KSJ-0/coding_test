import sys
N = sys.stdin.readline().strip()
result = ''.join(sorted(N, reverse=True))
print(result)