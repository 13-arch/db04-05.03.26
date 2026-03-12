
create table Subjects(
ID INT identity(1, 1) primary key,
Name_sub NVARCHAR(15),
Grade INT,
)

create table Teacher(
ID INT identity(1,1) primary key,
FIO NVARCHAR(30),
Grades INT,
Subjects INT,
constraint fk_subjects FOREIGN KEY (Subjects) REFERENCES Subjects(ID),
constraint fk_grades1 FOREIGN KEY (Grades) REFERENCES Subjects(ID)
)

create table Classes(
ID INT identity(1,1) primary key,
Grade INT,
Teacher INT,
constraint fk_teacher FOREIGN KEY (Teacher) REFERENCES Teacher(ID),
constraint fk_grades2 FOREIGN KEY (Grade) REFERENCES Teacher(ID)
)

create table Students(
ID INT identity(1,1) primary key,
FIO NVARCHAR(30),
BD NVARCHAR(10),
Grade INT,
constraint fk_grades3 FOREIGN KEY (Grade) REFERENCES Classes(ID)
)

insert into Subjects values ('Physics',9)
insert into Teacher values('jesica',3,3)
insert into Classes values (3,3)
insert into Students values ('man','22.11.2001',3)

select * from Students
select * from Subjects
select * from Classes
select * from Teacher

SELECT Students.FIO, Students.BD, Students.Grade, Teacher.FIO from Students
	JOIN Classes ON Students.Grade = Classes.Grade
	JOIN Teacher on Classes.Grade = Teacher.Grades
	where Teacher.FIO = 'jesica'

