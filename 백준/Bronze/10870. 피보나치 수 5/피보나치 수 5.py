import sys
n = int(sys.stdin.readline().strip())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    k = 1
    k_1 = 1
    k_2 = 0
    for _ in range(n-1):
        k = k_1 + k_2
        k_2 = k_1
        k_1 = k
    print(k)