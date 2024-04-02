from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {(lambda self:mean([mean(self.grades[course]) for course in self.grades]))(self) if len(self.grades) != 0  else "None"}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def rate_lecturer(self, lecturer, course, grade):
        if int(grade) >= 0 and int(grade) <= 10:
            if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'оценка должна быть от 0 до 10'

    def __lt__(self, other):
        if isinstance(other, Student):
            return (lambda self:mean([mean(self.grades[course]) for course in self.grades]))(self) <  (lambda self:mean([mean(self.grades[course]) for course in self.grades]))(other)
        else:
            return "Ошибка сравнения"

    def __gt__(self, other):
        if isinstance(other, Student):
            return (lambda self:mean([mean(self.grades[course]) for course in self.grades]))(self) >  (lambda self:mean([mean(self.grades[course]) for course in self.grades]))(other)
        else:
            return "Ошибка сравнения"
        
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
 
class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {(lambda self:mean([mean(self.grades[course]) for course in self.grades]))(self)}'
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return (lambda self:mean([mean(self.grades[course]) for course in self.grades]))(self) <  (lambda self:mean([mean(self.grades[course]) for course in self.grades]))(other)
        else:
            return "Ошибка сравнения"
    
    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return (lambda self:mean([mean(self.grades[course]) for course in self.grades]))(self) >  (lambda self:mean([mean(self.grades[course]) for course in self.grades]))(other)
        else:
            return "Ошибка сравнения"
            
          
class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def avarage_grade_hw(student_list: list, course):
    if len(student_list)!= 0:
        return (lambda student_list:mean([mean(student_list[i].grades[course]) for i in range(len(student_list))]))(student_list)
    else:
        return "Ошибка"

def avarage_grade_lecturer(lecturer_list: list, course):
    if len(lecturer_list)!= 0:
        return (lambda lecturer_list: mean([mean(lecturer_list[i].grades[course]) for i in range(len(lecturer_list))]))(lecturer_list)
    else:
        return "Ошибка"
student_1 = Student('Иван', 'Иванов', 'М')
student_2 = Student('Артем', 'Артемов', 'М')

student_1.courses_in_progress.append('Python')
student_1.courses_in_progress.append('Java')
student_2.courses_in_progress.append('Java')
student_2.courses_in_progress.append('HTML')

student_1.finished_courses.append('C')
student_2.finished_courses.append('C++')

lecturer_1 = Lecturer('Владимир', 'Владимиров')
lecturer_2 = Lecturer('Александр', 'Александров')

lecturer_1.courses_attached.append('Java')
lecturer_1.courses_attached.append('Python')
lecturer_2.courses_attached.append('Java')
lecturer_2.courses_attached.append('HTML')

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Java', 8)
student_2.rate_lecturer(lecturer_2, 'HTML', 9)
student_1.rate_lecturer(lecturer_2, 'Java', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 6)
student_2.rate_lecturer(lecturer_1, 'Java', 7)

reviewer_1 = Reviewer('Ибрагим', 'Ибрагимов')
reviewer_2 = Reviewer('Алексей', 'Алексеев')

reviewer_1.courses_attached.append('Python')
reviewer_2.courses_attached.append('Java')
reviewer_2.courses_attached.append('HTML')

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Java', 5)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'HTML', 9)

print(f'{student_2}\n')
print(f'{lecturer_2}\n')
print(f'{reviewer_2}\n')

print(student_1 < student_2)
print(student_1 > student_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)

print(f'\n{avarage_grade_hw([student_1, student_2], 'Java')}\n')
print(f'{avarage_grade_lecturer([lecturer_2, lecturer_1], 'Java')}\n')
