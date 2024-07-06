my_dict = {'tuple': (3, 100, 6, 78, 8, 4),
           'list': [4, 678, 900, 'rrr', 777],
           'dict': {'one': 1, 'two': 'two'},
           'set': {1, False, 7, 'text'}}
print(my_dict['set'])
my_dict['list'].append('text')
my_dict['list'].pop(1)
my_dict['i am a tuple'] = 'ilovemylife'
del_el = my_dict.pop('list')
my_dict['set'].add('timeflies')
del_el_2 = my_dict['set'].pop()
print(my_dict)
