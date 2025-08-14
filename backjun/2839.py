# 3kg, 5kg 설탕이 있을 때 정확히 Nkg 배달하기
import sys
N=int(sys.stdin.readline().strip())

five = N//5

while five >= 0:
    rest = N - five * 5
    if rest % 3 == 0:
        print(five + rest // 3)
        break
    five -= 1

else:
    print(-1)


# least = float('inf')
# for i in range(0, N // 3 + 1):
#     for j in range(0, N // 3 + 1):
#         number = 3 * i + 5 * j
#         if N == number:
#             least = min(least,i+j)     
# if least == float('inf'):
#     print(-1)
# else:
#     print(least)