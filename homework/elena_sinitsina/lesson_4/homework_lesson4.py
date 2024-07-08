my_dict = {'tuple': (3, 100, 4, 90, 8, 4),
           'list': [4, 678, 900, 'rrr', 777],
           'dict': {'one': 1, 'two': 'two'},
           'set': {1, False, 7, 'text'}}
tuple_value = my_dict['tuple']
print(tuple_value[-1])
my_dict['list'].append('text')
my_dict['list'].pop(1)
tuple_value_new = (1)
key_new = ('i am a tuple',)
my_dict['dict'][key_new] = tuple_value_new
popped_value = my_dict['dict'].pop('two')
my_dict['set'].add('timeflies')
popped_value_2 = my_dict['set'].pop()
print(my_dict)
