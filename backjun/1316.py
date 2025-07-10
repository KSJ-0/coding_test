#문제
#그룹 단어란 존재하는 모든 문자에 대해서 각 문자가 연속해서 나타나는 경우이다
#e.g) ccazzzb면 c,a,z,b가 그룹 단어
#aabbbccb는 b가 떨어져서 나와서 그룹 단어X
#단어 N개를 입력받아 그룹 단어의 개수를 출력

#입력
#첫째 줄에 단어의 개수 N<=100
#둘째 줄부터 N개의 줄에 단어. 알파벳 소문자,<=100

#출력: 그룹 단어의 수

import sys
word_count = int(sys.stdin.readline().strip())
group_word = word_count

for i in range(word_count):
    word = sys.stdin.readline().strip()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+1:]: #j+1 이후에 해당 알파벳 있는지 체크
            group_word -= 1
            break

print(group_word)            
