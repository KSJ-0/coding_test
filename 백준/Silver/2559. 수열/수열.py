import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temps = list(map(int, input().split()))
prefix = [0] * (N+1)
prefix[1] = temps[0]

for i in range(1, N):
    prefix[i+1] = temps[i] + prefix[i]

K_sums = [0] * (N-K+1)
for j in range(0, N-K+1):
    K_sums[j] = prefix[K+j] - prefix[j]

print(max(K_sums))