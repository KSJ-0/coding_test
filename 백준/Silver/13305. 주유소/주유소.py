import sys
input = sys.stdin.readline
N = int(input().strip())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

cheapest = prices[0]
total = 0

for i in range(len(roads)):
    if prices[i] < cheapest:
        cheapest = prices[i]
    total += cheapest*roads[i]

print(total)