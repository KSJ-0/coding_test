# 문제
# 학교 식당에서 두 가지 메뉴가 제공되고 각각의 학생이 좋아하는 메뉴를 선택한 상태이다.
# 학생이 학교 식당에 도착하고 식사가 준비되는 n개의 정보가 저장된 S가 주어짐
# S에 저장된 정보를 순서대로 처리한 뒤 좋아하는 메뉴를 먹은 학생 목록 A,
# 좋아하지 않는 메뉴를 먹은 학생 목록 B, 식당에 도착했으나 식사하지 못한 학생 목록 C를 출력

# 입력
# 첫 번째 줄에 N (1<=N<=500,000)
# 두 번째 줄부터 한 줄에 유형 1 또는 유형 2가 저장되어 있음
# 유형 1은 1 a b 형태로 a는 양의 정수인 학생 번호, b는 좋아하는 메뉴 번호인 학생 한 명이 식당에 도착하여 맨 뒤에 줄을 서는 것
# 유형 2는 2 b 형태로 메뉴 번호가 양의 정수 b인 식사 1인분이 준비되어 맨 앞에서 대기 중인 학생 1명이 식사를 시작하는 것
# b는 1 또는 2이다.

# 출력
# 첫 번째 줄: 좋아하는 메뉴를 먹은 학생 목록 A에 있는 학생 번호를 빈칸 공백을 두고 오름차순으로 출력
# 두 번째 줄: 좋아하지 않는 메뉴를 먹은 학생 목록 B에 있는 학생 번호를 빈칸 공백을 두고 오름차순으로 출력
# 세 번째 줄: 식당에 도착했으나 식사하지 못한 학생 목록 C에 있는 학생 번호를 빈칸 공백을 두고 오름차순으로 출력

# 학생 목록에 학생이 없으면 None 출력

# 풀이 방법
# FIFO이므로 큐 사용
# 스택으로 유형 1을 넣을 학생 큐를 구현한다.
# 학생 목록 A, B, C를 배열로 선언한다.
# 유형 2가 입력될 때마다 학생 큐의 앞에서 하나씩 pop하고 서로 비교한다,
# A, B 혹은 C에 알맞게 학생번호를 넣는다.


import sys
from collections import deque

N = int(sys.stdin.readline().strip())
students = deque()
like = []
dont_like = []
dont_eat = []

for i in range(N):
    student = sys.stdin.readline().strip().split()
    if (student[0]=='1'):
        students.append(student)
    else:
        if (len(students)!=0):
            eat = students.popleft()
            if (eat[2]==student[1]):
                like.append(int(eat[1]))
            else:
                dont_like.append(int(eat[1]))

if (len(students)!=0):
    dont_eat = [int(i[1]) for i in students]

like.sort()
dont_like.sort()
dont_eat.sort()

print(' '.join(map(str,like)) if like else "None")
print(' '.join(map(str,dont_like)) if dont_like else "None")  
print(' '.join(map(str,dont_eat)) if dont_eat else "None") 

