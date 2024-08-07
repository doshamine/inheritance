class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
            and course in student.courses_in_progress):

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


lecturer = Lecturer('Ivan', 'Ivanov')
lecturer.courses_attached += ['Java-fullstack', 'Python-backend']

reviewer = Reviewer('Petr', 'Petrov')
reviewer.courses_attached += ['Python-backend', 'C++', 'C#']

student = Student('Sidor', 'Sidorov', 'M')
student.courses_in_progress += ['Python-backend', 'C++']

assert student.rate_lecture(reviewer, 'Python-backend', 8) == 'Ошибка'
assert student.rate_lecture(lecturer, 'C++', 9) == 'Ошибка'
assert (student.rate_lecture(lecturer, 'Python-backend', 146)
    == 'Ошибка. Оценка 146 не соответствует десятибалльной шкале')

student.rate_lecture(lecturer, 'Python-backend', 10)
assert lecturer.grades['Python-backend'] == [10]