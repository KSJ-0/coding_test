import sys
from collections import Counter

input = sys.stdin.readline
N = int(input().strip())
have_num = list(map(int, input().split()))
M = int(input().strip())
target_num = list(map(int, input().split()))

count_dict = Counter(have_num)

result = [str(count_dict[num]) for num in target_num]

sys.stdout.write(" ".join(result))