import sys

w = [[[0]*(21) for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        for l in range(21):
            if i == 0 or j == 0 or l == 0:
                w[i][j][l] = 1
            elif i < j and j < l:
                w[i][j][l] = w[i][j][l-1] + w[i][j-1][l-1] - w[i][j-1][l]
            else:
                w[i][j][l] = w[i-1][j][l] + w[i-1][j-1][l] + w[i-1][j][l-1] - w[i-1][j-1][l-1]

def func(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        return w[20][20][20]
    
    return w[a][b][c]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    result = func(a, b, c)
    print(f"w({a}, {b}, {c}) = {result}" )