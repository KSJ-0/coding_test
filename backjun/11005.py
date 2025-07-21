import sys
N, B = map(int,sys.stdin.readline().split())
result = []

while (N>0):
    R = N % B
    if R<10:
        result.append(str(R))
    else:
        result.append(chr(R+55))
    
    N=N//B
print(''.join(reversed(result)))        