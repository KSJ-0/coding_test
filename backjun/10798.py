# 글자는 영어 대문자 A부터 Z, 소문자 a부터 z, 숫자 0부터 9이다.
# 글자를 수평으로 일렬로 붙여서 단어를 만든다.
# 한 줄의 글자는 최대 15개
# 만드는 단어의 수는 5개
# 각 단어의 글자 개수는 다를 수 있다
# 만들어진 단어들을 세로로 읽는다
# 글자가 없으면 무시하고 다음 글자를 읽는다
# 읽은 문자들은 공백 없이 한 줄로 출력한다.



input_list = []
length_list = []
for _ in range(5):
    str=input()
    input_list.append(str)
    length_list.append(len(str))


result = ""
for i in range(max(length_list)):
    for j in range(5):
        if i < length_list[j]:
            result+=input_list[j][i]
print(result)
