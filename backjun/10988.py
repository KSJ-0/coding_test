#단어가 앞으로 읽을 때와 뒤로 읽을 때가 똑같은지 확인
#입력: 1<= <=100 알파벳 소문자만
#출력: 똑같으면 1 아니면 0

import sys
word = sys.stdin.readline().strip()

if (word==word[::-1]): print(1)
else: print(0)

# import sys
# word = sys.stdin.readline().strip()
# length = len(word)
# word2 = ""

# for i in range(length):
#     word2.join(word[length-1-i])

# if (word==word2): print(1)
# else: print(0)