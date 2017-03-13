#!~/.pyenv/shims/python

import re
import collections

# Task 1
keys0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
list1 = ['a', 'b', 'c', 'd', 'e', 'f']

n_keys0 = len(keys0)
n_list0 = len(list0)
n_list1 = len(list1)

if n_keys0 > n_list1:
    for n in range(n_keys0):
        list1.append('None')

dict0 = dict(zip(keys0, list0))
dict1 = dict(zip(keys0, list1))

print(dict0)
print(dict1)

# Task 2

s1 = "vjuh"
s2 = "ololo"

if s1 == s1[::-1]:
    print(s1, 'is palindrome')
else:
    print(s1, 'is not palindrome')
if s2 == s2[::-1]:
    print(s2, 'is palindrome')
else:
    print(s2, 'is not palindrome')

# Task 3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a) & set(b)
print(c)

# Task 4

file = open('./access_log', 'r')
ip_addr = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', file.read())
for i in collections.Counter(ip_addr).most_common(10):
    print('IP %s, counter %d' % (i[0], i[1]))
