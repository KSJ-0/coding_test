# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

# 입력: 3개의 줄에 걸쳐 삼각형의 각의 크기 주어짐 0<= <=180

import sys
angles = [int(sys.stdin.readline().strip()) for _ in range(3)]

if angles[0]+angles[1]+angles[2]!=180:
    print("Error")
elif angles[0]==60 and angles[1]==60 and angles[2]==60:
    print("Equilateral")
elif (angles[0]==angles[1]) or (angles[0]==angles[2]) or (angles[1]==angles[2]):
    print("Isosceles")
else:
    print("Scalene")