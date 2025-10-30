import sys
input = sys.stdin.readline
 
N = int(input().strip())
P = list(map(int, input().split()))
P.sort()

result = 0
last = 0
for time in P:
    last += time
    result += last
  
print(result)