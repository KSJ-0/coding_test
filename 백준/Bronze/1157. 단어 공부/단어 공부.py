import sys
word = sys.stdin.readline().strip().upper()
alphabet =  {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0,
             "G":0, "H":0, "I":0, "J":0, "K":0, "L":0,
             "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0,
             "S":0, "T":0, "U":0, "V":0, "W":0, "X":0,
             "Y":0, "Z":0}

for i in range(len(word)):
    alphabet[word[i]]+=1
    
value_list = list(alphabet.values())

largest = 0
num = 0
for i in range(len(value_list)):
    if value_list[i] > largest:
        largest = value_list[i]
        num = i

result = chr(65 + num) if value_list.count(largest)==1 else "?"
print(result)