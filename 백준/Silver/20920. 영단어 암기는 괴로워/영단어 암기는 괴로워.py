import sys
input = sys.stdin.readline
N, M = map(int, input().split())
eng_dict = {}

for _ in range(N):
    word = input().strip()
    if word not in eng_dict:
        if len(word)>=M:
            eng_dict[word] = 1
    else:
        eng_dict[word] += 1


word_list = list(eng_dict.keys())
word_list.sort(key= lambda k: (-eng_dict[k], -len(k), k))     
print("\n".join(word_list))