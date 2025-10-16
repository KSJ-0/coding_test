import sys
input = sys.stdin.readline
n = int(input().strip())
score = [0] * (n+1)
drinks = [0]
for _ in range(n):
    drinks.append(int(input().strip()))

if n >= 1:
    score[1] = drinks[1]
if n >= 2:
    score[2] = drinks[1] + drinks[2]
if n >= 3:
    score[3] = max(drinks[1] + drinks[2], drinks[1] + drinks[3], drinks[2] + drinks[3])

for i in range(4, n+1):
        score[i] = max(score[i-1], score[i-2] + drinks[i], score[i-3] + drinks[i-1] + drinks[i])

print(score[n])