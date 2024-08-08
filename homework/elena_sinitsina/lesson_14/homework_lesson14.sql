INSERT INTO students(name, second_name, group_id) VALUES('Ivan','Ivanov', 179)

INSERT INTO "groups"(title , start_date , end_date) VALUES('Beginners','June24','Sep24')

INSERT INTO books(title, taken_by_student_id) VALUES('Math 5 Grade', 264)

INSERT INTO books(title, taken_by_student_id) VALUES('Science 5 Grade', 264)

INSERT INTO subjets(title) VALUES('Math')

INSERT INTO subjets(title) VALUES('Science')

INSERT INTO lessons (title, subject_id) VALUES('Monday 01 August', 278)

INSERT INTO lessons (title, subject_id) VALUES('Friday 05 August', 279)

INSERT INTO lessons (title, subject_id) VALUES('Wednesday 03 August', 278)

INSERT INTO lessons (title, subject_id) VALUES('Monday 08 August', 279)

INSERT INTO marks (value, lesson_id, student_id) VALUES('5+', 633, 264)

INSERT INTO marks (value, lesson_id, student_id) VALUES('5-', 634, 264)

INSERT INTO marks (value, lesson_id, student_id) VALUES('4+', 635, 264)

INSERT INTO marks (value, lesson_id, student_id) VALUES('4-', 636, 264)

SELECT marks.value, marks.lesson_id FROM marks WHERE marks.student_id = 264

SELECT books.title FROM books WHERE books.taken_by_student_id = 264

SELECT * 
FROM students 
JOIN "groups" ON students.group_id = "groups".id 
JOIN books ON students.id = books.taken_by_student_id 
JOIN marks ON students.id = marks.student_id 
JOIN lessons ON marks.lesson_id = lessons.id 
JOIN subjets  ON lessons.subject_id = subject_id
WHERE students.id = 264