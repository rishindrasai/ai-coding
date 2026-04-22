DROP TABLE IF EXISTS students;
-- create table with student id(primary key), name , subject name  , marks , grades and semester --
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    subject_name VARCHAR(100) NOT NULL,
    marks INT,
    grades VARCHAR(2),
    semester VARCHAR(20)
);
-- insert some sample data into the  students table --
INSERT INTO students (student_id, name, subject_name, marks, grades, semester) VALUES
(2297,'Chowdary','Devops',85,'A','3-2'),
(2216,'Ashwitha','Python',78,'B+','3-2'),
(2382,'Veda','Data Science',92,'A+','3-2'),
(2438,'Rishitha','Machine Learning',88,'A','3-2'),
(2505,'Meghana','Cloud Computing',80,'B+','3-1');
-- query to select all students who scored above 80 marks --
SELECT * FROM students WHERE marks > 80;
-- query to update the grade of a student based on marks --
UPDATE students SET grades = 'A+' WHERE marks >= 90;
-- query to delete a student record based on student id --
DELETE FROM students WHERE student_id = 2297;
-- query to select all students in a specific semester --
SELECT * FROM students WHERE semester = '3-2';