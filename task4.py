def count_average_grade(grades: dict) -> float:
    if not grades:
        return 'Ошибка. Список оценок пуст'

    average_grade_list = []
    for course_grade_list in grades.values():
        if course_grade_list:
            average_grade_list += [sum(course_grade_list) / len(course_grade_list)]

    return sum(average_grade_list) / len(average_grade_list)


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __eq__(self, other):
        average_grade = count_average_grade(self.grades)
        other_average_grade = count_average_grade(other.grades)

        return average_grade == other_average_grade

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        average_grade = count_average_grade(self.grades)
        other_average_grade = count_average_grade(other.grades)

        return average_grade > other_average_grade

    def __lt__(self, other):
        average_grade = count_average_grade(self.grades)
        other_average_grade = count_average_grade(other.grades)

        return average_grade < other_average_grade

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not self > other

    def __str__(self):
        average_grade = count_average_grade(self.grades)
        
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}")

    def rate_lecture(self, lecturer, course, grade):
        if grade < 0 or grade > 10:
            return f"Ошибка. Оценка {grade} не соответствует десятибалльной шкале"

        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached 
            and course in self.courses_in_progress):

            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __eq__(self, other):
        average_grade = count_average_grade(self.grades)
        other_average_grade = count_average_grade(other.grades)

        return average_grade == other_average_grade

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        average_grade = count_average_grade(self.grades)
        other_average_grade = count_average_grade(other.grades)

        return average_grade > other_average_grade

    def __lt__(self, other):
        average_grade = count_average_grade(self.grades)
        other_average_grade = count_average_grade(other.grades)

        return average_grade < other_average_grade

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not self > other

    def __str__(self):
        average_grade = count_average_grade(self.grades)
        
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}"


class Reviewer(Mentor):

    def __str__(self):    
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
            and course in student.courses_in_progress):

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def hw_average_grade(students: list, course: str) -> float:
    average_grade_list = []

    for student in students:
        if course in student.courses_in_progress and student.grades[course]:
            average_grade_list += [sum(student.grades[course]) / len(student.grades[course])]

    if not average_grade_list:
        return f"Ошибка. На курсе {course} никто не учится"

    return sum(average_grade_list) / len(average_grade_list)


def course_average_grade(lectors: list, course: str) -> float:
    average_grade_list = []

    for lector in lectors:
        if course in lector.courses_attached and lector.grades[course]:
            average_grade_list += [sum(lector.grades[course]) / len(lector.grades[course])]

    if not average_grade_list:
        return f"Ошибка. Курс {course} никто не читает"

    return sum(average_grade_list) / len(average_grade_list)


mitch = Lecturer('Mitch', 'Marconi')
mitch.courses_attached += ['Java-fullstack', 'Python-backend', 'DevOps engineering']

mike = Student('Mike', 'Smith', 'M')
mike.courses_in_progress += ['Python-backend', 'C++', 'DevOps engineering']
mike.finished_courses += ['Введение в программирование']
mike.rate_lecture(mitch, 'Python-backend', 8)
mike.rate_lecture(mitch, 'DevOps engineering', 6)
mike.rate_lecture(mitch, 'DevOps engineering', 7)
mike.rate_lecture(mitch, 'Python-backend', 10)

petr = Reviewer('Petr', 'Petrov')
petr.courses_attached += ['Python-backend', 'C++']
petr.rate_hw(mike, 'Python-backend', 2)
petr.rate_hw(mike, 'C++', 8)
petr.rate_hw(mike, 'Python-backend', 5)
petr.rate_hw(mike, 'C++', 9)
petr.rate_hw(mike, 'C++', 7)

ivan = Reviewer('Ivan', 'Ivanov')
ivan.courses_attached += ['Java-fullstack', 'C#']

marie = Lecturer('Marie', 'Saddley')
marie.courses_attached += ['Java-fullstack', 'C#', 'Python-backend']

anna = Student('Anna', 'Plum', 'F')
anna.courses_in_progress += ['Python-backend', 'C#']
anna.finished_courses += ['Frontend-разработчик']
anna.rate_lecture(mitch, 'Python-backend', 3)
anna.rate_lecture(marie, 'C#', 8)
anna.rate_lecture(mitch, 'Python-backend', 6)
anna.rate_lecture(marie, 'C#', 7)
anna.rate_lecture(marie, 'Python-backend', 10)

petr.rate_hw(anna, 'Python-backend', 4)
ivan.rate_hw(anna, 'C#', 6)
ivan.rate_hw(anna, 'C#', 2)
ivan.rate_hw(anna, 'C#', 3)
petr.rate_hw(anna, 'Python-backend', 8)

assert hw_average_grade([mike, anna], 'Java-fullstack') == 'Ошибка. На курсе Java-fullstack никто не учится'
assert hw_average_grade([mike, anna], 'Python-backend') == 4.75
assert hw_average_grade([mike, anna], 'C++') == 8.0

assert course_average_grade([mitch, marie], 'C++') == 'Ошибка. Курс C++ никто не читает'
assert course_average_grade([mitch, marie], 'Python-backend') == 8.375
assert course_average_grade([mitch, marie], 'C#') == 7.5