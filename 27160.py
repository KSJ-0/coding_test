import sys

N = int(sys.stdin.readline().strip())
a = {}

for _ in range(N):
    card = sys.stdin.readline().strip().split()
    card[1]=int(card[1])
    if(card[0] in a):
        a[card[0]]+=card[1]
    else :
        a[card[0]]=card[1]

bell = False

for i in a.keys():
    if(a[i]==5):
        bell = True

if(bell==True):
    print('YES')
else:
    print('NO')    
        

    