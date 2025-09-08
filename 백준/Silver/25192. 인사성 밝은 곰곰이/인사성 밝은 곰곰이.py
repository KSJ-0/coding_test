import sys
input = sys.stdin.readline
N = int(input().strip())
users = set()
count = 0
for _ in range(N):
    name = input().strip()
    if "ENTER" == name:
        count += len(users)
        users = set()
    else:
        users.add(name)

count += len(users)
print(count)