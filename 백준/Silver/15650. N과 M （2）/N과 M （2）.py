import sys
N, M = map(int, sys.stdin.readline().split())
used = [False] * (N+1)
last_used = 0
result = []
output = []

def backtrack():
    global last_used
    if len(result) == M:
        output.append(' '.join(map(str,result)))
        return
    for i in range(1, N+1):
        if not used[i] and i > last_used:
            used[i] = True
            result.append(i)
            last_used = i
            backtrack()
            result.pop()
            used[i] = False
            last_used = 0

backtrack()
print('\n'.join(output))