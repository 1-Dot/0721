import itertools

digits = ['0', '7', '2', '1']
operators = ['+', '-', '*', '/', '']
results = {}

for ops in itertools.product(operators, repeat=3):
    expressions = [
        f"{digits[0]}{ops[0]}{digits[1]}{ops[1]}{digits[2]}{ops[2]}{digits[3]}",  # 0 O 7 O 2 O 1
        f"({digits[0]}{ops[0]}{digits[1]}){ops[1]}{digits[2]}{ops[2]}{digits[3]}",  # (0 O 7) O 2 O 1
        f"{digits[0]}{ops[0]}({digits[1]}{ops[1]}{digits[2]}){ops[2]}{digits[3]}",  # 0 O (7 O 2) O 1
        f"{digits[0]}{ops[0]}{digits[1]}{ops[1]}({digits[2]}{ops[2]}{digits[3]})",  # 0 O 7 O (2 O 1)
        f"({digits[0]}{ops[0]}{digits[1]}{ops[1]}{digits[2]}){ops[2]}{digits[3]}",  # (0 O 7 O 2) O 1
        f"{digits[0]}{ops[0]}({digits[1]}{ops[1]}{digits[2]}{ops[2]}{digits[3]})",  # 0 O (7 O 2 O 1)
        f"({digits[0]}{ops[0]}{digits[1]}){ops[1]}({digits[2]}{ops[2]}{digits[3]})",  # (0 O 7) O (2 O 1)
        f"(({digits[0]}{ops[0]}{digits[1]}){ops[1]}{digits[2]}){ops[2]}{digits[3]}",  # ((0 O 7) O 2) O 1
        f"{digits[0]}{ops[0]}(({digits[1]}{ops[1]}{digits[2]}){ops[2]}{digits[3]})",  # 0 O ((7 O 2) O 1)
    ]
    for expr in expressions:
        try:
            result = eval(expr)
            results[expr] = result
        except:
            continue

filtered_dict = {k: v for k, v in results.items() if v >= 0}

seen_values = set()
unique_dict = {}
for k, v in filtered_dict.items():
    if v not in seen_values:
        unique_dict[k] = v
        seen_values.add(v)

sorted_dict = dict(sorted(unique_dict.items(), key=lambda item: item[1], reverse=True))
swapped_dict = {v: k for k, v in sorted_dict.items()}

print(swapped_dict)
