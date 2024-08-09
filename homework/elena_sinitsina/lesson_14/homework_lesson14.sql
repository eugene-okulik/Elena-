
INSERT INTO students(name, second_name) VALUES('Petr','Ivanov')

INSERT INTO books(title, taken_by_student_id) VALUES('Math 5 Grade', 1873)

INSERT INTO books(title, taken_by_student_id) VALUES('Science 5 Grade', 1873)

INSERT INTO "groups"(title , start_date , end_date) VALUES('Beginners','June24','Sep24')

UPDATE students SET group_id = 1763 WHERE id = 1873

INSERT INTO subjets(title) VALUES('Math')

INSERT INTO subjets(title) VALUES('Science')

INSERT INTO lessons (title, subject_id) VALUES('Monday 01 August', 2465)

INSERT INTO lessons (title, subject_id) VALUES('Friday 05 August', 2466)

INSERT INTO lessons (title, subject_id) VALUES('Wednesday 03 August', 2465)

INSERT INTO lessons (title, subject_id) VALUES('Monday 08 August', 2466)

INSERT INTO marks (value, lesson_id, student_id) VALUES('5+', 5246, 1873)

INSERT INTO marks (value, lesson_id, student_id) VALUES('5-', 5247, 1873)

INSERT INTO marks (value, lesson_id, student_id) VALUES('4+', 5248, 1873)

INSERT INTO marks (value, lesson_id, student_id) VALUES('4-', 5249, 1873)

SELECT marks.value, marks.lesson_id FROM marks WHERE marks.student_id = 1873

SELECT books.title FROM books WHERE books.taken_by_student_id = 1873

SELECT * 
FROM students 
JOIN "groups" ON students.group_id = "groups".id 
JOIN books ON students.id = books.taken_by_student_id 
JOIN marks ON students.id = marks.student_id 
JOIN lessons ON marks.lesson_id = lessons.id 
JOIN subjets  ON lessons.subject_id = subjets.id
WHERE students.id = 1873