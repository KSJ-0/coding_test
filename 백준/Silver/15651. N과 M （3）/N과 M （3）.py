import sys
N, M = map(int, sys.stdin.readline().split())
result = []
output = []

def backtrack():
    if len(result) == M:
        output.append(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        result.append(i)
        backtrack()
        result.pop()

backtrack()
print('\n'.join(output))