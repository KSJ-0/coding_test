import sys
N = int(sys.stdin.readline().strip())
number_cards = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
check = list(map(int,sys.stdin.readline().split()))

card_dic = {card: "0" for card in check}
for card in number_cards:
    if card in card_dic:
        card_dic[card] = "1"

sys.stdout.write(" ".join(list(card_dic.values())))