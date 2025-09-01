import sys
from collections import deque
N = int(sys.stdin.readline().strip())
queue = deque()
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        queue.append(order[1])
    elif order[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print("-1")
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if queue:
            print("0")
        else:
            print("1")
    elif order[0] == "front":
        if queue:
            top = queue.popleft()
            queue.appendleft(top)
            print(top)
        else:
            print("-1")
    elif order[0] == "back":
        if queue:
            bottom = queue.pop()
            queue.append(bottom)
            print(bottom)
        else:
            print("-1")
