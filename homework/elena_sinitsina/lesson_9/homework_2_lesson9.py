temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33,
                31, 30, 32, 30, 28, 24, 23]
new_list_temp = list(filter(lambda x: x > 28, temperatures))
print(list(new_list_temp))
print(max(list(new_list_temp)))
print(min(list(new_list_temp)))
print(int(sum(new_list_temp) / len(new_list_temp)))
