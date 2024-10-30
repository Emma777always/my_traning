
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list_2 = [7, 'spider']
values_list = [5, 'puppy', True]
values_dict = {'a': 6,'b': 'snake', 'c': 6}
print_params()
print_params(2, True)
print_params(True, 'kitty')
print_params('kitty', True)
print_params('kitty')
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)



