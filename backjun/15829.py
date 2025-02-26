# 문제
# 입력으로 들어오는 문자열은 영문 소문자로만 구성되어 있음.
# 알파벳 a~z는 1~26의 고유한 번호로 치환할 수 있음. 
# 따라서 문자열을 수열로 변환할 수 있음. e.g)abba->1,2,2,1
# 해시값을 계산하기 위해서 문자열, 즉 수열을 하나의 정수로 치환할 것임.
# 수열을 모두 더하고 M으로 나눌 것임
# 수열의 각 항의 번호에 해당 하는 만큼 특정한 숫자를 거듭제곱해서 곱해준 다음 더함.
# 특정한 숫자 r은 31이며 M은 1234567891임.

# 입력
# 첫 줄에는 문자열의 길이 L이 들어옴
# 둘째 줄에는 영문 소문자로 이루어진 문자열이 들어옴

# 출력
# 문자열을 해시값으로 계산하여 정수로 출력함.

# 풀이 방법
# 문자열을 한글자씩 읽으면서 아스키코드로 변환하여 1~26의 수로 치환함
# for문 돌면서 계산

#개선한 코드
import sys

L = int(sys.stdin.readline().strip()) #문자열의 길이 
string = sys.stdin.readline().strip()
result = 0

#2
for i in range(L): #문자열 길이만큼 반복
    number = ord(string[i])-96
    result+=number*pow(31,i)

print(result%1234567891)

#처음 코드
# import sys

# #1
# str = []

# L = int(sys.stdin.readline().strip()) #문자열의 길이 
# string = sys.stdin.readline().strip()

# #2
# for i in range(L): #문자열 길이만큼 반복
#     number = ord(string[i])-96 #아스키코드로 변환하고 1~26에 맞게 계산
#     str.append(number)

# n=0
# result=0

# #3
# for i in str:
#     result+=i*pow(31,n) #31을 거듭제곱해서 곱해주고 더함
#     n+=1

# print(result%1234567891)