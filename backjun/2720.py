import sys
N = int(sys.stdin.readline().strip())
Money = [25,10,5,1]

for _ in range(N):
    M = int(sys.stdin.readline().strip())
    result = [] 
    for i in Money:
        result.append(str(M//i))
        M %= i
    print(' '.join(result))

