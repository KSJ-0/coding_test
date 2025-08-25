import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
never_hear = [input().strip() for _ in range(N)]
never_hear_dict = {person: 0 for person in never_hear}

result = []
for _ in range(M):
    person = input().strip()
    if person in never_hear_dict:
        result.append(person)

result.sort()
print(len(result))
print('\n'.join(result))