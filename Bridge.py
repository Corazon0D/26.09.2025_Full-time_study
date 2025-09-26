
h_bus = 437
m = int(input('введи количество мостов: ')) # количество Мостов

count = 0
for i in range(m) :
    d = int(input('высоту мостов: '))
    if h_bus < d:
        count += 1

    if h_bus >= d:
        print(f'Crash {i + 1}')
        break
if h_bus < d:
    print('No chash')