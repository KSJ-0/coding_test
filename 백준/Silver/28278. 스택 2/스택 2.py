import sys
input = sys.stdin.readline

N = int(input().strip())
stack = []

for _ in range(N):
    order = input().split()
    if order[0]=='1':
        stack.append(order[1])
    elif order[0]=='2':
        if len(stack)!=0:
            print(stack.pop())
        else:
            print('-1')
    elif order[0]=='3':
        print(str(len(stack)))
    elif order[0]=='4':
        if len(stack)!=0:
            print('0')
        else:
            print('1') 
    elif order[0]=='5':
        if len(stack)!=0:
            top = stack.pop()
            print(top)
            stack.append(top)      
        else:
            print('-1')
       