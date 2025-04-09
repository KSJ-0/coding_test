# 문제
# 패턴과 파일 이름이 주어졌을 때 각각의 파일 이름이 패턴과 일치하는지 아닌지

# 입력
# 첫째 줄에 파일의 개수 N이 주어진다.(1<=N<=100)
# 둘째 줄에는 패턴이 주어진다.
# -패턴은 알파벳 소문자와 별표 한 개로 이루어져 있다.
# -문자열의 길이는 100을 넘지 않으며 별표는 문자열의 시작과 끝에 있지 않다.
# 세번째줄부터는 N줄동안 파일 이름이 주어진다.
# 파일 이름은 알파벳 소문자로만 이루어져 있다.(1<=파일이름길이<=100)

# 출력
# 패턴과 일치하면 DA, 일치하지 않으면 NE

#문자열 풀이
import sys
N = int(sys.stdin.readline().strip())
pattern = sys.stdin.readline().strip()
start, end = pattern.split("*")

for _ in range(N):
    sen = sys.stdin.readline().strip()
    if (sen.startswith(start) and sen.endswith(end) and len(sen) >= len(start) + len(end)):
        print("DA")
    else:
        print("NE")


#정규식 풀이
# import sys
# import re
# N = int(sys.stdin.readline().strip())
# pattern = sys.stdin.readline().strip().replace("*",".*")
# pattern = re.compile(f"^{pattern}$")

# for _ in range(N):
#     file_name=sys.stdin.readline().strip()
#     if(pattern.fullmatch(file_name)):
#         print("DA")
#     else:
#         print("NE")
