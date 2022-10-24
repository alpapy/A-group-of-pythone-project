line = input("Введіть текст: ")
print(line[::-1])
line1 = input("Введіть рядок")
h = {'letters': 0, 'numbers': 0}
for i in line1:
    if i.isalpha():
        h['letters'] += 1
    elif i.isdigit():
        h['numbers'] += 1
print(h['numbers'], h['letters'])
print(len([i for i in line1 if i.isdigit()]))
print(len([i for i in line1 if i.isalpha()]))


line2 = input("Введіть текст: ")
line3 = input("Знайти символ: ")
line5 = line2.count(line3)
print(line5)


line4 = input(str("Введіть текст: "))
line6 = input(str("Знайти слово: "))
line7 = line4.count(line6)
print(line7)


line8 = input(str("Введіть текст: "))
line9 = input(str("Знайти слово: "))
line99 = input(str("Знамінити: "))
line44 = str(line8.replace((line9), (line99)))
print(line44)