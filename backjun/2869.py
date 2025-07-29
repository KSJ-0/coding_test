#높이가 V 미터인 나무 막대 오르기
#낮에 A미터 올라감, 밤에 B미터 미끄러짐

import sys
import math
A, B, V = list(map(int, sys.stdin.readline().split()))

day = (V-B)/(A-B)
print(math.ceil(day))


