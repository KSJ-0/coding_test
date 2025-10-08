import sys
input = sys.stdin.readline
n = int(input().strip())
r, g, b = map(int, input().split())

for i in range(1, n):
    curr, curg, curb = map(int, input().split())
    cur0 = curr + min(g, b)
    cur1 = curg + min(r, b)
    cur2 = curb + min(r, g)
    
    r, g, b = cur0, cur1, cur2

print(min(r, g, b))
   