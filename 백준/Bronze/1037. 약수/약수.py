import sys
input = sys.stdin.readline
N = int(input().strip())
num = list(map(int, input().split()))

print(min(num)*max(num))