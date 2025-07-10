#몇 개의 크로아티아 알파벳으로 구성되어 있는지 
#c=,c-,dz=,d-,lj,nj,s=,z=는 하나의 알파벳이다

#입력: 첫째 줄에 최대 100글자의 단어, 알파벳 소문자와 '-', '='만 있음
#출력: 몇 개의 크로아티아 알파벳으로 구성되어 있는지 

import sys
word = sys.stdin.readline().strip()
word_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in word_list:
    word = word.replace(i, "a")

print(len(word))