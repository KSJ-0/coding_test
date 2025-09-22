import sys
N, M = map(int, sys.stdin.readline().split())
result = []
output = []
last_used = 0

def backtrack():
    global last_used
    if len(result) == M:
        output.append(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        if last_used <= i:
            result.append(i)
            last_used = i
            backtrack()
            last_used = 0
            result.pop()

backtrack()
print('\n'.join(output))