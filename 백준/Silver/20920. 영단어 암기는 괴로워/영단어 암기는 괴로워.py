import sys
input = sys.stdin.readline
N, M = map(int, input().split())
eng_dict = {}

for _ in range(N):
    word = input().strip()
    if len(word)>=M:
        eng_dict[word] = eng_dict.get(word, 0) + 1

word_list = list(eng_dict)
word_list.sort(key= lambda k: (-eng_dict[k], -len(k), k))     
print("\n".join(word_list))