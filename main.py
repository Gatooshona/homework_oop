def average_grade(self, course):
    res = sum(self.grades[course]) / len(self.grades[course])
    return res


def average_grades(self):
    grades = []
    for key, value in self.grades.items():
        grades += value
    return sum(grades) / len(grades)


def avg_grade_in_course_students(students, course):
    all_grades_in_course = []
    for student in students:
        all_grades_in_course += student.grades[course]
    avg_grade_in_course = round(sum(all_grades_in_course) / len(all_grades_in_course), 1)
    return avg_grade_in_course


def avg_grade_in_course_lect(lecturers, course):
    all_grades_in_course = []
    for lecturer in lecturers:
        all_grades_in_course += lecturer.grades[course]
    avg_grade_in_course = round(sum(all_grades_in_course) / len(all_grades_in_course), 1)
    return avg_grade_in_course


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (
                course in self.finished_courses or self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    student_grade = average_grade
    student_grades = average_grades

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.student_grades()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self):
        print('Лекторы не могут выставлять оценки студентам!')

    lecturer_grade = average_grade
    lecturer_grades = average_grades

    def __str__(self):
        grades = self.lecturer_grades()
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {grades}'
        return some_lecturer


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_reviewer


student_female = Student('Anna', 'Petrova', 'female')
student_male = Student('Ivan', 'Ivanov', 'male')
reviewer_female = Reviewer('Olga', 'Belova')
reviewer_male = Reviewer('Oleg', 'Belov')
lecturer_female = Lecturer('Max', 'Petruhin')
lecturer_male = Lecturer('Marina', 'Petruhin')

reviewer_female.courses_attached += ['Git', 'Python', 'Введение в программирование']
reviewer_male.courses_attached += ['Git', 'Python']

lecturer_female.courses_attached += ['Git', 'Python', 'Введение в программирование']
lecturer_male.courses_attached += ['Git', 'Python']

student_female.courses_in_progress += ['Git', 'Python', 'Введение в программирование']
student_male.courses_in_progress += ['Git', 'Python']

reviewer_female.rate_hw(student_female, 'Git', 10)
reviewer_male.rate_hw(student_female, 'Git', 8)
reviewer_male.rate_hw(student_male, 'Git', 8)
reviewer_male.rate_hw(student_male, 'Git', 4)
print(student_female)
print()
student_male.rate_lecturer(lecturer_female, 'Python', 9)
student_female.rate_lecturer(lecturer_female, 'Python', 10)
student_male.rate_lecturer(lecturer_male, 'Python', 7)
student_female.rate_lecturer(lecturer_male, 'Python', 8)
print(lecturer_female)
print()
print(reviewer_female)
print()

# print(lecturer_female.lecturer_grades() > lecturer_male.lecturer_grades())
print(lecturer_female.lecturer_grades().__gt__(lecturer_male.lecturer_grades()))
# print(student_female.student_grades() > student_male.student_grades())
print(student_female.student_grades().__gt__(student_male.student_grades()))
print()
print(avg_grade_in_course_students([student_male, student_female], 'Git'))
print(avg_grade_in_course_lect([lecturer_female, lecturer_male], 'Python'))