import mysql.connector as mysql

db = mysql.connect(
    username='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

new_student = 'INSERT INTO students(name, second_name) VALUES (%s, %s)'
student_values = ('Mark', 'Markov')
cursor.execute(new_student, student_values)

new_student_id = cursor.lastrowid

new_book = 'INSERT INTO books(title, taken_by_student_id) VALUES(%s, %s)'
book_values = [
    ('English Listening', new_student_id),
    ('English Writing', new_student_id)
]
cursor.executemany(new_book, book_values)

new_group = 'INSERT INTO "groups"(title , start_date , end_date) VALUES(%s, %s, %s)'
group_values = ("English beginners", "Jan25", "March25")
cursor.execute(new_group, group_values)
new_group_id = cursor.lastrowid

update_student_group = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(update_student_group, (new_group_id, new_student_id))

new_subject1 = 'INSERT INTO `subjets`(title) VALUES(%s)'
subject_values1 = ('English General',)
cursor.execute(new_subject1, subject_values1)
subject_id1 = cursor.lastrowid
new_subject2 = 'INSERT INTO `subjets`(title) VALUES(%s)'
subject_values2 = ('English General',)
cursor.execute(new_subject2, subject_values2)
subject_id2 = cursor.lastrowid

new_lesson1 = 'INSERT INTO `lessons`(title, subject_id) VALUES(%s, %s)'
lesson_values1 = ('Monday 1 January', subject_id1)
cursor.execute(new_lesson1, lesson_values1)
lesson_id1 = cursor.lastrowid

new_lesson2 = 'INSERT INTO `lessons`(title, subject_id) VALUES(%s, %s)'
lesson_values2 = ('Tuesday 2 January', subject_id1)
cursor.execute(new_lesson2, lesson_values2)
lesson_id2 = cursor.lastrowid

new_lesson3 = 'INSERT INTO `lessons`(title, subject_id) VALUES(%s, %s)'
lesson_values3 = ('Wednesday 3 January', subject_id2)
cursor.execute(new_lesson3, lesson_values3)
lesson_id3 = cursor.lastrowid

new_lesson4 = 'INSERT INTO `lessons`(title, subject_id) VALUES(%s, %s)'
lesson_values4 = ('Thursday 4 January', subject_id2)
cursor.execute(new_lesson4, lesson_values4)
lesson_id4 = cursor.lastrowid

new_mark = 'INSERT INTO marks(value, lesson_id, student_id) VALUES(%s, %s, %s)'
mark_values = [
    ('Perfect', lesson_id1, new_student_id),
    ('Very good', lesson_id2, new_student_id),
    ('Not good', lesson_id3, new_student_id),
    ('Bad', lesson_id4, new_student_id)
]
cursor.executemany(new_mark, mark_values)

query = '''
SELECT 
   students.name, 
    students.second_name, 
    "groups".title AS group_title, 
    books.title AS book_title, 
    marks.value AS mark_value, 
    lessons.title AS lesson_title, 
    subjets.title AS subject_title
FROM
    students
JOIN "groups" ON students.group_id = "groups".id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON students.id = marks.student_id
JOIN lessons ON marks.lesson_id = lessons.id
JOIN subjets ON lessons.subject_id = subjets.id
WHERE 
students.id = %s;
'''
cursor.execute(query, (new_student_id,))
results = cursor.fetchall()

for row in results:
    print(row)

db.commit()
db.close()
