#6.12.18.24
import sys
N = int(sys.stdin.readline().strip())
k = 1
count = 0

while True:
    k += 6*count
    count += 1
    if k>=N:
        print(count)
        break
    