# Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(f'a = {a}, b = {b}, c = {c}')

print_params()
print_params(5)
print_params(10, 'текст')
print_params(c=False)
print_params(b=25) #работает
print_params(c=[1, 2, 3]) #работает

# Распаковка параметров:
values_list = [10, 'новая строка', False]
values_dict = {'a': 150, 'b': 'еще одна строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = [10, 'какая там по счету строка']

print_params(*values_list_2, 42) #работает