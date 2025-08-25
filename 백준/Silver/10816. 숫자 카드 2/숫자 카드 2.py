import sys
N = int(sys.stdin.readline().strip())
have_num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
target_num = list(map(int, sys.stdin.readline().split()))

have_num_dict = {}
for num in have_num:
    if num in have_num_dict:
        have_num_dict[num] += 1
    else:
        have_num_dict[num] = 1

result = []
for num in target_num:
    if num in have_num_dict:
        result.append(str(have_num_dict[num]))
    else:
        result.append('0')

sys.stdout.write(' '.join(result)) 