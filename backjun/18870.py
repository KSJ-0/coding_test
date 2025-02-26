# 문제
# 수직선 위의 n개의 좌표에 좌표 압축을 적용한다.
# Xi를 좌표 압축한 결과의 값은 Xi<Xj를 만족하는 서로 다른 Xj의 좌표의 개수와 같아야 한다.
# X1~Xn에 좌표 압축을 적용한 결과를 출력하라.

# 입력
# 첫째 줄에 N이 주어짐.
# 둘째 줄에 공백 한 칸으로 구분된 X1,X2~Xn이 주어짐.

# 출력
# 첫째 줄에 좌표 압축을 적용한 결과를 공백 한 칸으로 구분하여 출력한다.

# 좌표 압축이란
# 주어진 숫자의 상대적인 크기 순서만 유지하면서 그 숫자들을 0부터 시작하는 연속된 정수로 변환하는 것

# 문제 풀이 방법
# N을 변수에 저장한다
# X1~Xn을 리스트에 입력 순서대로 저장한다.
# 리스트를 정렬하여 X1~Xn을 딕셔너리의 key로 넣는다.
# value는 0부터 순차적으로 1씩 증가시켜 넣는다.
# 입력받은 순서대로 좌표 압축한 값을 리스트에 넣고 출력한다.

import sys

N = int(sys.stdin.readline().strip()) #1
coordinate = list(map(int,sys.stdin.readline().strip().split())) #2

coordinates = {}
num = 0

for coor in sorted(coordinate): #3
    if coor not in coordinates.keys():
        coordinates[coor] = num #4
        num+=1

result = [coordinates[coor] for coor in coordinate] #5

print(' '.join(map(str,result)))
#print(*result)도 가능

