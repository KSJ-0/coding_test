import sys

n = int(sys.stdin.readline().strip())
num_list = list(map(int,sys.stdin.readline().split()))

for i in num_list:
    if (i==1):
        n-=1
        continue
  
    for j in range(2,i):
        if(i%j==0):
            n-=1
            break

print(n) 