class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectore(self, lectore, course, grade):
        if isinstance(lectore, Lecturer) and course in self.courses_in_progress and course in lectore.courses_attached:
            lectore.grades[course] = lectore.grades.get(course, []) + [grade]

    def averange_score(self):
        summ = 0
        for b in self.grades.values():
            summ += sum(b) / len(b)
        res = summ / len(self.grades.values())
        return f'{res:0.1f}'

    def averange_score_of_course(self, course):
        if course in self.grades:
            return sum(self.grades.get(course)) / len(self.grades.get(course, 1))
        return 0

    def __str__(self):

        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.averange_score()}\n' \
               f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {" ".join(self.finished_courses)}'

    def __lt__(self, other):
        if self.averange_score() < other.averange_score():
            return True
        return False

    def __le__(self, other):
        if self.averange_score() <= other.averange_score():
            return True
        return False

    def __eq__(self, other):
        if self.averange_score() == other.averange_score():
            return True
        return False

    def __ne__(self, other):
        if self.averange_score() != other.averange_score():
            return True
        return False

    def __gt__(self, other):
        if self.averange_score() > other.averange_score():
            return True
        return False

    def __ge__(self, other):
        if self.averange_score() >= other.averange_score():
            return True
        return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def averange_score(self):
        summ = 0
        for b in self.grades.values():
            summ += sum(b) / len(b)
        res = summ / len(self.grades.values())
        return f'{res:0.1f}'

    def averange_score_of_course(self, course):
        if course in self.grades:
            return sum(self.grades.get(course)) / len(self.grades.get(course, 1))
        return 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.averange_score()}'

    def __lt__(self, other):
        if self.averange_score() < other.averange_score():
            return True
        return False

    def __le__(self, other):
        if self.averange_score() <= other.averange_score():
            return True
        return False

    def __eq__(self, other):
        if self.averange_score() == other.averange_score():
            return True
        return False

    def __ne__(self, other):
        if self.averange_score() != other.averange_score():
            return True
        return False

    def __gt__(self, other):
        if self.averange_score() > other.averange_score():
            return True
        return False

    def __ge__(self, other):
        if self.averange_score() >= other.averange_score():
            return True
        return False


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

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


def averange_score_students(list_of_students, name_course):
    return sum([i.averange_score_of_course(name_course) for i in list_of_students]) / len(list_of_students)


def averange_score_lecturer(list_of_lecturer, name_course):
    return sum([i.averange_score_of_course(name_course) for i in list_of_lecturer]) / len(list_of_lecturer)


student1 = Student('Ivan', 'Petrov', 'male')
student2 = Student('Svetlana', 'Ivanova', 'female')
reviewer1 = Reviewer('Sergey', 'Vasiliev')
reviewer2 = Reviewer('Petr', 'Sas')
lecturer1 = Lecturer('Vlad', 'Klop')
lecturer2 = Lecturer('Alisa', 'Voinova')

student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']
student1.finished_courses += ['C++']
student2.finished_courses += ['Goland']

reviewer1.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Java', 'Goland']
lecturer1.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Java', 'Goland']

student1.rate_lectore(lecturer1, 'Python', 10)
student1.rate_lectore(lecturer1, 'Python', 10)
student1.rate_lectore(lecturer1, 'Python', 9.8)

student2.rate_lectore(lecturer2, 'Java', 9.9)
student2.rate_lectore(lecturer2, 'Java', 9.9)
student2.rate_lectore(lecturer2, 'Java', 10)

reviewer1.rate_hw(student1, 'Python', 7.5)
reviewer1.rate_hw(student1, 'Python', 8.0)
reviewer1.rate_hw(student1, 'Python', 9.9)

reviewer2.rate_hw(student2, 'Java', 10)
reviewer2.rate_hw(student2, 'Java', 7)
reviewer2.rate_hw(student2, 'Java', 8.6)

print(lecturer1 > lecturer2)
print(lecturer1 >= lecturer2)
print(lecturer1 < lecturer2)
print(lecturer1 <= lecturer2)
print(lecturer1 != lecturer2)
print(lecturer1 == lecturer2)

print(student1 > student2)
print(student1 >= student2)
print(student1 == student2)
print(student1 != student2)
print(student1 < student2)
print(student1 <= student2)

print(student1)
print(lecturer1)
print(reviewer1)
