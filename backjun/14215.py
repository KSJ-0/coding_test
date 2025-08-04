# 각 막대의 길이는 양의 정수이다
# 세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다.
# 삼각형의 둘레를 최대로 해야 한다.

# 입력: 첫째 줄에 a, b, c (1 ≤ a, b, c ≤ 100)
# 만들 수 있는 가장 큰 삼각형의 둘레
import sys
a,b,c = sorted(map(int, sys.stdin.readline().split()))

if c >= a+b:
    c = a+b-1

print(a+b+c)


