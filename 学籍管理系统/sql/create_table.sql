DROP DATABASE if exists SchoolManagement;
CREATE DATABASE SchoolManagement;
USE SchoolManagement;
-- 创建院系表
CREATE TABLE Departments (
    department_id  VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    num	 INT default 0
);

-- 创建专业表
CREATE TABLE Majors (
    major_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    num INT default 0,
    department_id VARCHAR(50),
    CONSTRAINT fk_major_department FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);
-- 创建学生表
CREATE TABLE Students (
	username VARCHAR(50),
	password VARCHAR(50),
    student_id VARCHAR(50)  PRIMARY KEY,
    id_num	VARCHAR(50),
	gender VARCHAR(50),
    native_place VARCHAR(50), 
    nation 	VARCHAR(50),
    s_name VARCHAR(50) NOT NULL,
    enrollment_date VARCHAR(50),
    graduation_data VARCHAR(50),
	major_id VARCHAR(50),
    image varchar(50),
    new_major VARCHAR(50),
    CONSTRAINT fk_major FOREIGN KEY (major_id) REFERENCES Majors(major_id)
);

-- 创建教师表
CREATE TABLE Teachers (
	username VARCHAR(50),
	password VARCHAR(50),
    teacher_id VARCHAR(50) PRIMARY KEY,
	id_num	VARCHAR(50),
	gender VARCHAR(50),
    native_place VARCHAR(50), 
    nation 	VARCHAR(50),
    s_name VARCHAR(50) NOT NULL,
	department_id VARCHAR(50),
    image varchar(50),
    CONSTRAINT fk_teacher_department FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- 创建奖惩表
CREATE TABLE RewardsPunishments (
    rp_id VARCHAR(50) PRIMARY KEY,
    student_id VARCHAR(50),
    type ENUM('Reward', 'Punishment'),
    description TEXT,
    department_id  VARCHAR(50),
    CONSTRAINT fk_rp_student FOREIGN KEY (student_id) REFERENCES Students(student_id)
);



-- 创建课程表
CREATE TABLE Courses (
    course_id VARCHAR(50)  PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    credits VARCHAR(50),
    department_id VARCHAR(50),
    teacher_id VARCHAR(50),
    is_passed CHAR(1),
    CONSTRAINT fk_course_department FOREIGN KEY (department_id) REFERENCES Departments(department_id),
    CONSTRAINT fk_course_teacher FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

-- 创建成绩表
CREATE TABLE Grades (
    student_id VARCHAR(50),
    course_id VARCHAR(50),
    grade VARCHAR(50),
    PRIMARY KEY (student_id, course_id),
    CONSTRAINT fk_grade_student FOREIGN KEY (student_id) REFERENCES Students(student_id),
    CONSTRAINT fk_grade_course FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- 创建管理员表
CREATE TABLE Administrators (
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
     admin_id VARCHAR(50)  PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

INSERT INTO Administrators Values('1','1','1','f','r');