#coding:utf-8

"""
desc: 使用collections模块
author: ben
time: 2018-05-10
"""

import collections
from collections import defaultdict

#defaultdict
test_data = (
    ('cat', 2),
    ('dog', 5),
    ('sheep', 3),
    ('cat', 1),
    ('sheep', 2)
)

test_data_dict = defaultdict(list)

for name, num in test_data:
    test_data_dict[name].append(num)

# print test_data_dict

#orderedDict
from collections import OrderedDict
original_dict = {'a': 2, 'b': 4, 'c': 5}
# for key, value in original_dict.items():
#     print key, value

ordered_dict = OrderedDict([('a', 2), ('b', 4), ('c', 5)])
# for key, value in ordered_dict.items():
#     print key, value

#counter
from collections import Counter

test_counter_data = ['cat', 'dog', 'sheep', 'cat', 'dog']
counter_data = Counter()

for item in test_counter_data:
    counter_data[item] += 1

# print counter_data

# deque
from collections import deque
d = deque([1,2,3,4,5])
d.extendleft([0])
# print d
d.extend([6,7])
d.popleft()
# print d

#namedtuple
from collections import namedtuple
animal = namedtuple('animal', 'type age')
mark = animal(type='dog', age=2)
print mark.type
