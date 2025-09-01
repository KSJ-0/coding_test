import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    queue = deque()
    for _ in range(N):
        order = input().split()
        if order[0] == "push":
            queue.append(order[1])
        elif order[0] == "pop":
            print(-1 if not queue else queue.popleft())
        elif order[0] == "size":
            print(len(queue))
        elif order[0] == "empty":
            print(1 if not queue else 0)
        elif order[0] == "front":
            print(-1 if not queue else queue[0])
        elif order[0] == "back":
            print(-1 if not queue else queue[-1])

if __name__ == "__main__":
    solve()