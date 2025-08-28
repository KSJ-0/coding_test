import sys
input = sys.stdin.readline

N = int(input().strip())
stack = []
result = []

for _ in range(N):
    order = input().split()
    order_num = order[0]
    if order_num == '1':
        stack.append(order[1])
    elif order_num == '2':
        if len(stack) != 0:
            result.append(stack.pop())
        else:
            result.append('-1')
    elif order_num == '3':
        result.append(str(len(stack)))
    elif order_num == '4':
        if len(stack) != 0:
            result.append('0')
        else:
            result.append('1') 
    elif order_num == '5':
        if len(stack) != 0:
            result.append(stack[-1])    
        else:
            result.append('-1')
            
sys.stdout.write('\n'.join(result))            
       