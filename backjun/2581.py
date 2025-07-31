#소수의 합과 최소값 찾기

import sys

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
prime_num_list = []

for i in range(M, N+1):
    if i==1:
        continue
    prime_num = True
    for j in range(2,i):
        if i%j==0:
            prime_num = False
            break
    if prime_num==True:
        prime_num_list.append(i)
    

if len(prime_num_list)==0:
     print(-1)
else:
    total = 0
    for k in prime_num_list:
        total += k
    print(total)
    print(prime_num_list[0])
