from sys import argv

script_name, first_param, second_param, third_param = argv

print(f"Заработная плата сотрудника: {float(first_param) * float(second_param) + float(third_param)}")