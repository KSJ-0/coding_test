import sys
N, K = map(int, sys.stdin.readline().split())
from collections import deque

circle = deque(range(1, N + 1))
result = []

while circle:
    circle.rotate(-(K - 1))
    result.append(circle.popleft())

print("<"+", ".join(map(str, result))+">")