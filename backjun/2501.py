import sys
N, K = list(map(int, sys.stdin.readline().split()))
num = 1
num_list = []

for _ in range(1, N+1):
    if (N%num==0):
        num_list.append(num)
    num+=1

if(len(num_list)<K):
    print(0)
else:
    print(num_list[K-1])