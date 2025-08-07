import sys
from itertools import combinations
N, M = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
total_max = 0

for i in combinations(cards,3):
    total = sum(i)
    if total>M:
        continue
    if total<=M and total_max<total:
        total_max=total

print(total_max)

