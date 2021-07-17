
f = open('Example2.txt', 'r')

for i, line in enumerate(f):
    line = line.split()
    print(f'Количество слов в данной строке: {len(line)}')

print(f'Всего строк в файле: {i + 1}')

f.close()