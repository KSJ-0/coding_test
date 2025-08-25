import sys
N, M = list(map(int,sys.stdin.readline().split()))
pocketmons = [sys.stdin.readline().strip() for _ in range(N)]

pocketmons_dict = {}
i = 1
for pocketmon in pocketmons:
    pocketmons_dict[pocketmon] = i
    i += 1

for _ in range(M):
    pocketmon = sys.stdin.readline().strip()
    if pocketmon.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
        print(pocketmons[int(pocketmon)-1])
    else:
        print(pocketmons_dict[pocketmon])