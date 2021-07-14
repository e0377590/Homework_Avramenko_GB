
f = open('Example2.txt', 'r')

for i, line in enumerate(f):
    line = line.replace('\n', '')
    print(f'{i} строка: {line}')
    print(f'Количество символов в данной строке: {len(line)}')

print(f'Всего строк в файле: {i + 1}')

f.close()