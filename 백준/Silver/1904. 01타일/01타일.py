import sys
N = int(sys.stdin.readline().strip())
    
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    result = 0
    present_2 = 1
    present_1 = 2
    for i in range(3, N+1):
        result = present_2 + present_1
        present_2 = present_1
        present_1 = result%15746
    print(present_1)    