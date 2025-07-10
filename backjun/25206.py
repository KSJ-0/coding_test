#문제
#전공 평점>=3.3
#전공 평점 계산하는 프로그램
#등급이 P인 과목은 계산에서 제외

#입력
#20줄에 걸쳐 과목명, 학점, 등급이 공백으로 구분되어 주어짐

#출력
#전공 평점

import sys
total_credit=0
total_grade=0.0
criteria = {"A+":4.5, "A0": 4.0, "B+":3.5, "B0": 3.0, "C+":2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for i in range(20):
    subject = sys.stdin.readline().strip().split()
    if subject[2]=='P':
        continue
    else:
        total_credit += float(subject[1])
        total_grade += criteria[subject[2]]*float(subject[1])

print(total_grade/total_credit)

