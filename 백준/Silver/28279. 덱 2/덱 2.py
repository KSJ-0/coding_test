import sys
from collections import deque

N = int(sys.stdin.readline().strip())
dq = deque()
result = []

for _ in range(N):
    orders = list(sys.stdin.readline().split())
    order = orders[0]
    if order == "1":
        dq.appendleft(orders[1])
    elif order == "2":
        dq.append(orders[1])
    elif order == "3":
        if dq:
            result.append(dq.popleft())
        else:
            result.append("-1")
    elif order == "4":
        if dq:
            result.append(dq.pop())
        else:
            result.append("-1")
    elif order == "5":
        result.append(str(len(dq)))
    elif order == "6":
        if dq:
            result.append("0")
        else:
            result.append("1")
    elif order == "7":
        if dq:
            result.append(dq[0])
        else:
            result.append("-1")
    elif order == "8":
        if dq:
            result.append(dq[-1])
        else:
            result.append("-1")

sys.stdout.write("\n".join(result))