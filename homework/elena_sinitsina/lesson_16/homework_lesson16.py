import mysql.connector as mysql
import os
import csv
from dotenv import load_dotenv


load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASSW = os.getenv('DB_PASSW')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

db = mysql.connect(
    user=DB_USER,
    passwd=DB_PASSW,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname((os.path.dirname(base_path)))
csv_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

csv_data = []
with open(csv_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        csv_data.append(row)
print("csv data:")
for row in csv_data:
    print(row)

cursor = db.cursor()

query = '''
SELECT
    students.name,
    students.second_name,
    "groups".title AS group_title,
    books.title AS book_title,
    subjets.title AS subject_title,
    lessons.title AS lesson_title,
    marks.value AS mark_value
FROM students
JOIN "groups" ON students.group_id = "groups".id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON students.id = marks.student_id
JOIN lessons ON marks.lesson_id = lessons.id
JOIN subjets ON lessons.subject_id = subjets.id
ORDER BY students.name, students.second_name, group_title, book_title, subject_title, lesson_title, mark_value;
;
'''
cursor.execute(query)

db_data = cursor.fetchall()

db_data_set = set(tuple(row) for row in db_data)

#print("\nsql data:")
#for row in db_data_set:
#    print(row)

print("\nmissing data:")
for row in csv_data:
    if tuple(row) not in db_data_set:
        print(row)

cursor.close()
db.close()
