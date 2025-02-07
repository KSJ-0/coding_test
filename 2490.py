# 문제
# 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다.
# 도(배1, 등3), 개(배2, 등2), 걸(배3, 등1), 윷(배4), 모(등4)

# 입력
# 첫째 줄부터 셋째 줄까지 각 줄에 네 개의 정수(0 또는 1)이 빈칸을 사이에 두고 주어진다.

# 출력
# 첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를 출력하며
# 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력한다.

# 문제 풀이 방법
# 배의 개수를 key, 윷놀이 결과를 value로 하는 딕셔너리를 선언한다.
# 입력을 리스트에 int 타입으로 변환하여 한글자씩 넣는다.
# 딕셔너리에서 0의 개수를 key로 하는 value를 찾는다. 

import sys

sol = {0:"E", 1:"A", 2:"B", 3:"C", 4:"D"} #1

for i in range(3):
    data = [int(i) for i in sys.stdin.readline().strip().split()] #2
    print(sol[data.count(0)]) #3

# 두 번째 코드 - 딕셔너리 사용하여 비교 코드 단축
# import sys

# list=[]
# for i in range(3):
#     list.append([int(i) for i in sys.stdin.readline().strip().split()])

# sol = {0:"E", 1:"A", 2:"B", 3:"C", 4:"D"}
# result=[0,0,0]

# for i in range(3):
#     for j in range(4):
#         if(list[i][j]==0):
#             result[i]+=1

#     print(sol[result[i]])      


# 처음 짠 코드 - 일일이 if문으로 비교
# import sys

# list=[]
# for i in range(3):
#     list.append([int(i) for i in sys.stdin.readline().strip().split()])

# result=[0,0,0]

# for i in range(3):
#     for j in range(4):
#         if(list[i][j]==0):
#             result[i]+=1

#     if (result[i]==1):
#         print("A")
#     elif (result[i]==2):
#         print("B")
#     elif (result[i]==3):
#         print("C")
#     elif (result[i]==4):
#         print("D")    
#     else:
#         print("E")    