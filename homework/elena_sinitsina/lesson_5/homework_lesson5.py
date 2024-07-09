#Task_1:
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)
print(f"name: {name}, last_name: {last_name}, city: {city}, phone: {phone}, country: {country}")
#Task_2:
string_1 = 'результат операции: 42'
string_2 = 'результат операции: 514'
string_3 = 'результат работы программы: 9'
len_1 = len(string_1)
index_1 = string_1.index(":") + 2
number_1 = int(string_1[index_1:len_1]) + 10
len_2 = len(string_2)
index_2 = string_2.index(":") + 2
number_2 = int(string_2[index_2:len_2]) + 10
len_3 = len(string_3)
index_3 = string_3.index(":") + 2
number_3 = int(string_3[index_3:len_3]) + 10
print(number_1, number_2, number_3)
#Task_3:
students = ['Ivanov', 'Petrov', 'Sidorov']
student_1, student_2, student_3 = students
subjects = ['math', 'biology', 'geography']
subject_1, subject_2, subject_3 = subjects
print(f'Students {student_1}, {student_2}, {student_3} study these subjects: {subject_1}, {subject_2}, {subject_3}')
