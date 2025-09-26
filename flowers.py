# G Герань
# C Крокусv
# V фиалка
n = int(input("Введите Кол-во дней: "))

letf = 'G'
central = 'C'
right = 'V'


for i in range(n):
    # действия Маши
    right, central = central, right
    # действия Тани
    letf, central = central, letf
print(letf + central + right)
