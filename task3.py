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
petr.courses_attached += ['Python-backend', 'C++', 'C#']
petr.rate_hw(mike, 'Python-backend', 2)
petr.rate_hw(mike, 'C++', 8)
petr.rate_hw(mike, 'Python-backend', 5)
petr.rate_hw(mike, 'C++', 9)
petr.rate_hw(mike, 'C++', 7)

assert str(petr) == "Имя: Petr\nФамилия: Petrov"
assert str(mitch) == "Имя: Mitch\nФамилия: Marconi\nСредняя оценка за лекции: 7.75"
assert (str(mike) == "Имя: Mike\nФамилия: Smith\nСредняя оценка за домашние задания: 5.75\n"
    "Курсы в процессе изучения: Python-backend, C++, DevOps engineering\n"
    "Завершенные курсы: Введение в программирование")

marie = Lecturer('Marie', 'Saddley')
marie.courses_attached += ['Java-fullstack', 'C#']

anna = Student('Anna', 'Plum', 'F')
anna.courses_in_progress += ['Python-backend', 'C#']
anna.finished_courses += ['Frontend-разработчик']
anna.rate_lecture(mitch, 'Python-backend', 3)
anna.rate_lecture(marie, 'C#', 8)
anna.rate_lecture(mitch, 'Python-backend', 6)
anna.rate_lecture(marie, 'C#', 7)

petr.rate_hw(anna, 'Python-backend', 4)
petr.rate_hw(anna, 'C#', 6)
petr.rate_hw(anna, 'C#', 2)
petr.rate_hw(anna, 'C#', 3)
petr.rate_hw(anna, 'Python-backend', 8)

assert mitch != marie
assert mitch < marie
assert mitch <= marie

assert mike != anna
assert mike >= anna
assert mike > anna