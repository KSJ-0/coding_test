import sys
N = int(sys.stdin.readline().strip())
members = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    members.append([int(age), name])

members.sort(key= lambda k: (k[0]))
for age, name in members:
    sys.stdout.write(f"{age} {name}\n")