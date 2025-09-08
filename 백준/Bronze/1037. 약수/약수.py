import sys
N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
if N==1:
    print(num[0]**2)
else:
    print(num[0]*num[N-1])