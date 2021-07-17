

f = open('Example3.txt', 'r')
sum = 0
for i, line in enumerate(f):
    line = line.split()
    line[1] = int(line[1])
    sum += line[1]
    if line[1] > 20000:
        print(line[0])

print(f'Средняя величина дохода сотрудников: {round(sum/(i + 1), 2)}')

f.close()

# with open('Example3.txt', 'r', encoding='utf-8') as f:
#     employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
#     print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
#           f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')