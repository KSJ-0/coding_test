import sys
N, M = map(int, sys.stdin.readline().split())
used = [False] * (N+1)
result = []
output = []

def backtrack():
    if len(result) == M:
        output.append(' '.join(map(str, result)))
        return
    
    for i in range(1, N+1):
        if not used[i]:
            used[i] = True
            result.append(i)
            backtrack()
            result.pop()
            used[i] = False

backtrack()
output.sort()
print('\n'.join(output))