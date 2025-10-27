import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input().strip()) for _ in range(N)]
result = 0

for i in range(N):
    q = K//coins[N-i-1]
    if q > 0:
        result += q
        K -= (q*coins[N-i-1])

print(result)
