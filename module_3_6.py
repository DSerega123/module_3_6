def calculate_structure_sum(*data):
    global res
    for i in data:
        if isinstance(i, dict):
            for key, value in i.items():
                res = res + len(key) + int(value)
        else:
            for j in i:
                if isinstance(j, int):
                    res = res + j
                else:
                    if isinstance(j, float):
                        res = res + j
                    else:
                        if isinstance(j, str):
                            res = res + len(j)
                        else:
                            calculate_structure_sum(j)
    return res

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

res = 0
result = calculate_structure_sum(data_structure)
print(result)
