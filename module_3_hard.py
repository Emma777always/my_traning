def calc(*args):
    t = 0
    for element in args:
        if isinstance(element, (list, tuple, set)):
            t = t + calc(*element)
        elif isinstance(element, dict):
            t = t + calc(*element.items())
        elif isinstance(element,str):
            t = t + len(element)
        elif isinstance(element, (int, float)):
            t = t + element
        elif element is None:
            pass
    return t
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calc(data_structure)
print(result)
