import sys
N = int(sys.stdin.readline().strip())
members = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    num = i
    members.append([int(age), name, num])

members.sort(key= lambda k: (k[0], k[2]))
for member in members:
    print(member[0], member[1])