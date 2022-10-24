import random 
w1 = 0
tr = 0

rnum = random.randint(0,500)
qnum = int(input("Вгадайте число від 1 до 500: "))
while w1 < 1:
    if rnum == qnum:
        print(f"Молодець \nКількість спроб: {tr}")
        input()
        w1 += 1 
    elif qnum > rnum:
        print("")
        qnum = int(input("Неправильно, число більше ніж загадане: "))
        tr += 1
    elif qnum < rnum:
        print()
        qnum = int(input("Неправильно, число менше ніж загадане: "))
        tr += 1