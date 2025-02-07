# 문제
# 노교수는 N개의 수업을 진행했고 자신의 수업을 M개 이상 들은 학생이 몇명인지 궁금했다.
# 수업의 들은 학생들의 학번이 주어질 때 조건을 만족하는 학생의 수를 구하자.

# 입력
# 첫 번째 줄에 N, M이 차례대로 주어진다.(1<=N<=100;1<=N<=M)
# 두 번째 줄부터 2xN개의 줄에 걸쳐 각 수업에 대한 정보 N개가 순서대로 주어진다.
# 수업의 정보는 두 개의 줄로 이뤄진다.
#     - 첫 번째 줄에 과목의 수강생 수
#     - 두 번째 줄에 수업을 들은 학생들의 학번이 공백으로 구분되어 주어진다.
# 학번은 숫자 8개로 구성되며 1로 시작한다. 한 수업에 동일한 학번의 중복은 없다.

# 출력
# M개 이상의 수업을 들은 학생의 수

# 풀이 방법
# sys.stdin.readline으로 N, M을 각각 저장한다.
# N번 for문 돌면서 수업을 들은 학생들의 학번을 모두 리스트에 담는다.
# 학번이 key, 들은 수업의 개수가 value인 딕셔너리를 만든다.
# value 리스트를 확인해서 M이상인 값이 몇 개 있는지 센다.
# 센 값을 출력한다.

import sys

N, M = map(int, sys.stdin.readline().strip().split()) #1
students = {}
student_list = []

for i in range(N): #2
    student_num = sys.stdin.readline().strip()
    student_list += sys.stdin.readline().strip().split()

for student in student_list: #3
    if student not in students.keys():
        students[student]=1
    else:
        students[student]+=1 

result = 0

for i in students.values(): #4
    if(i>=M):
        result+=1

print(result) #5


#처음 풀이 - 이중 for문
# import sys

# N, M = map(int, sys.stdin.readline().strip().split()) #1
# students = {} 

# for i in range(N): #2
#     student_num = sys.stdin.readline().strip()
#     student_list = sys.stdin.readline().strip().split()
#     for student in student_list:
#         if student not in students.keys():
#             students[student]=1
#         else:
#             students[student]+=1 

# result = 0

# for i in students.values(): #3
#     if(i>=M):
#         result+=1

# print(result) #4