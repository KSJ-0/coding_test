# 문제
# 정수를 저장하는 스택을 구현하고 입력으로 주어지는 명령을 처리하라
# 명령은 총 5가지이다.
# push X: 정수 X를 스택에 넣음
# pop: 스택의 가장 위에 있는 정수를 빼고 출력함. 스택이 비어있으면 -1 출력.
# size: 스택에 들어있는 정수의 개수를 출력함.
# empty: 스택이 비어있으면 1, 아니면 0을 출력함.
# top: 스택의 가장 위에 있는 정수를 출력함. 비어있으면 -1 출력.

# 입력
# 첫째 줄에 주어지는 명령의 수 N(1<=N<=10,000)
# 둘째 줄부터 N개의 줄에 명령이 하나씩 주어짐.
# 주어지는 정수는 1<=정수<=100,000

# 출력 명령이 주어질 때마다 한 줄에 하나씩 출력


# 풀이방법
# 명령의 수를 저장
# if문으로 각자의 명령 처리

#두번째 코드
import sys

N = int(sys.stdin.readline().strip())
stack = []

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    if (command[0]=="push"): #push
        stack.append(command[1])
    elif (command[0]=="pop"): #pop
        if (len(stack)!=0):
            print(stack.pop())
        else:
            print(-1)
    elif (command[0]=="top"): #top
        if (len(stack)!=0):
            print(stack[-1])
        else:
            print(-1)
    elif (command[0]=="size"): #size
        print(len(stack))
    elif (command[0]=="empty"): #empty
        if (len(stack)==0):
            print(1)
        else:
            print(0)



