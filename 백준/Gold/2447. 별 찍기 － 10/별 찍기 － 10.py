import sys

def is_blank(i,j):
    while i > 0 and j > 0:
        if i % 3 == 1 and j % 3 == 1:
            return True
        i //= 3
        j //= 3
    return False

N = int(sys.stdin.readline().strip())
for i in range(N):
    row = []
    for j in range(N):
        if is_blank(i, j):
            row.append(" ")
        else:
            row.append("*")
    print("".join(row))