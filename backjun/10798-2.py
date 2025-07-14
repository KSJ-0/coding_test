#입력: 다섯줄 1개에서 15개 글자들이 빈칸없이 연속으로
#출력: 세로로 읽은 순서대로 글자 출력
import sys
words = [sys.stdin.readline().strip() for _ in range(5)]
result = ""

for j in range(15):
    for i in range(5):
        if len(words[i])<=j:
            continue
        result += words[i][j]

print(result)
