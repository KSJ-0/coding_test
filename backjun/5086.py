#두 수의 관계
#첫 번째 수가 두 번째 수의 약수이면 factor
#배수이면 multiple
#둘 다 아니면 neither

import sys

while True:
    n1, n2 = list(map(int, sys.stdin.readline().strip().split()))
    
    if(n1==0 and n2==0):
        break

    if(n1>n2 and n1%n2==0):
        print("multiple")
    elif(n1<n2 and n2%n1==0):
        print("factor")
    else:
        print("neither")
        
