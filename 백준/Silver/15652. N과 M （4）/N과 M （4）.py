import sys
N, M = map(int, sys.stdin.readline().split())
result = []
output = []

def backtrack(start):
    global last_used
    if len(result) == M:
        output.append(' '.join(map(str, result)))
        return
    for i in range(start, N+1):
        result.append(i)
        backtrack(i)
        result.pop()

backtrack(1)
print('\n'.join(output))