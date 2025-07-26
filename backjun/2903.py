import sys
N =  int(sys.stdin.readline().strip())
k = 3
kn = 1
if(N==1):
    print(k*k)
else:
    for _ in range(N-1):
        kn *=2
        k += kn
    print(k*k)

