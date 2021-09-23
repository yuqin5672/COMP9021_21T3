# COMP9021 21T3
# Quiz 1 *** Due Friday Week 3 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 4 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE
from collections import defaultdict
# 翻转的字典
reversed_dict = defaultdict(list)
visited = []
for key in keys:
    # 翻转字符串
    reversed_dict[mapping[key]].append(key)
    #  如果没有被记录
    if key not in visited:
        cycle = [key]
        while mapping[key] in mapping:
            # 重新将value设置为key
            key = mapping[key]
            if key == cycle[0]:
                # 最终要获取的结果在这里
                cycles.append(cycle)
                visited.extend(cycle)
                break
            elif key in cycle:
                # 如果已经存在的情况下：1:5,5:5这种情况
                break
            cycle.append(key)

# 获取最终的结果
for key, values in reversed_dict.items():
    # 没有字典就加一个
    if len(values) not in reversed_dict_per_length:
        reversed_dict_per_length[len(values)] = {}
    # 统一构造词典
    reversed_dict_per_length[len(values)][key] = values
    

print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)

