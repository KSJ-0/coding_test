import sys
input = sys.stdin.readline
A, B = map(int, input().split())
A_set = set(input().split())
B_set = set(input().split())

print(len(A_set ^ B_set))
