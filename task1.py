class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
            and course in student.courses_in_progress):

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 

class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    pass


lecturer = Lecturer('Ivan', 'Ivanov')
lecturer.courses_attached += ['Java-fullstack', 'Python-backend']
assert (f"Lecturer {lecturer.name} {lecturer.surname} teaches the following courses: {', '.join(lecturer.courses_attached)}."
    == "Lecturer Ivan Ivanov teaches the following courses: Java-fullstack, Python-backend.")

reviewer = Reviewer('Petr', 'Petrov')
reviewer.courses_attached += ['Python-backend', 'C++', 'C#']
assert (f"Reviewer {reviewer.name} {reviewer.surname} checks the following courses: {', '.join(reviewer.courses_attached)}."
    == "Reviewer Petr Petrov checks the following courses: Python-backend, C++, C#.")