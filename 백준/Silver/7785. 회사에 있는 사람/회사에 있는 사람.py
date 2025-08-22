import sys
n = int(sys.stdin.readline().strip())

log_dict = {}
name_list = []

for _ in range(n):
    name, log = sys.stdin.readline().split()
    if name not in log_dict:
        name_list.append(name)
    log_dict[name] = log 
   
name_list.sort(reverse=True)
for name in name_list:
  if log_dict[name] == "enter":
    print(name)