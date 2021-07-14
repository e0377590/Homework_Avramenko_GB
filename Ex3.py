

f = open('Example3.txt', 'r')
sum = 0
for i, line in enumerate(f):
    line = line.replace('\n', '')
    line = line.split(' ')
    line[1] = int(line[1])
    sum += line[1]
    if line[1] > 20000:
        print(line[0])

print(f'Средняя величина дохода сотрудников: {round(sum/(i + 1), 2)}')

f.close()