class Unit:
    # В класс Unit перенес все методы сравнения для классов наследников,
    # что бы работало только на студентов и лекторов, сделал проверку на имя класса
    def __lt__(self, other):
        if self.__class__.__name__ == 'Student' and other.__class__.__name__ == 'Student' or \
                self.__class__.__name__ == 'Lecturer' and other.__class__.__name__ == 'Lecturer':
            if self.averange_score() < other.averange_score():
                return True
            return False

    def __le__(self, other):
        if self.__class__.__name__ == 'Student' and other.__class__.__name__ == 'Student' or \
                self.__class__.__name__ == 'Lecturer' and other.__class__.__name__ == 'Lecturer':
            if self.averange_score() <= other.averange_score():
                return True
            return False

    def __eq__(self, other):
        if self.__class__.__name__ == 'Student' and other.__class__.__name__ == 'Student' or \
                self.__class__.__name__ == 'Lecturer' and other.__class__.__name__ == 'Lecturer':
            if self.averange_score() == other.averange_score():
                return True
            return False

    def __ne__(self, other):
        if self.__class__.__name__ == 'Student' and other.__class__.__name__ == 'Student' or \
                self.__class__.__name__ == 'Lecturer' and other.__class__.__name__ == 'Lecturer':
            if self.averange_score() != other.averange_score():
                return True
            return False

    def __gt__(self, other):
        if self.__class__.__name__ == 'Student' and other.__class__.__name__ == 'Student' or \
                self.__class__.__name__ == 'Lecturer' and other.__class__.__name__ == 'Lecturer':
            if self.averange_score() > other.averange_score():
                return True
            return False

    def __ge__(self, other):
        if self.__class__.__name__ == 'Student' and other.__class__.__name__ == 'Student' or \
                self.__class__.__name__ == 'Lecturer' and other.__class__.__name__ == 'Lecturer':
            if self.averange_score() >= other.averange_score():
                return True
            return False

    def __str__(self):
        text = ''
        if self.__class__.__name__ == 'Student':
            text = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                   f'Средняя оценка за домашние задания всех курсов: {self.averange_score()}\n' \
                   f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n' \
                   f'Завершенные курсы: {" ".join(self.finished_courses)}'
        elif self.__class__.__name__ == 'Lecturer':
            text = f'Имя: {self.name}\n' \
                   f'Фамилия: {self.surname}\n' \
                   f'Средняя оценка за лекции всех курсов : {self.averange_score()}'
        elif self.__class__.__name__ == 'Reviewer':
            text = f'Имя: {self.name}\n' \
                   f'Фамилия: {self.surname}'
        return text

    # Так же, т.к. логика подсчета среднего балла ученика за 1 курс и за все курсы,
    # и оценок лекторов одинакова, вынес в методы в 1 класс.
    # Так же, что бы работало только на лекторов и студентов, сделал проверки на эти классы
    def averange_score(self):
        if self.__class__.__name__ == 'Student' or self.__class__.__name__ == 'Lecturer':
            lst_of_score = [self.averange_score_of_course(b) for b in self.grades.keys()]
            res = sum(lst_of_score) / len(self.grades.keys())
            return f'{res:0.1f}'

    def averange_score_of_course(self, course):
        if self.__class__.__name__ == 'Student' or self.__class__.__name__ == 'Lecturer':
            if course in self.grades:
                return sum(self.grades.get(course)) / len(self.grades.get(course, 1))
            return 0


class Student(Unit):
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
        else:
            return 'Ошибка'


class Mentor(Unit):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades[course] = student.grades.get(course, []) + [grade]
        else:
            return 'Ошибка'


def averange(lst, name_course):
    return sum([person.averange_score_of_course(name_course) for person in lst]) / len(lst)


student1 = Student('Ivan', 'Petrov', 'male')
student2 = Student('Svetlana', 'Ivanova', 'female')
student3 = Student('Ekaterina', 'Plotnikova', 'female')
student4 = Student('Georgiy', 'Kac', 'female')
reviewer1 = Reviewer('Sergey', 'Vasiliev')
reviewer2 = Reviewer('Petr', 'Sas')
lecturer1 = Lecturer('Vlad', 'Klop')
lecturer2 = Lecturer('Alisa', 'Voinova')
lecturer3 = Lecturer('Polina', 'Gagarina')

student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']
student3.courses_in_progress += ['Python']
student4.courses_in_progress += ['Python']
student1.finished_courses += ['C++']
student2.finished_courses += ['Goland']

reviewer1.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Java', 'Goland']
lecturer1.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Java', 'Goland']
lecturer3.courses_attached += ['Python']

student1.rate_lectore(lecturer1, 'Python', 10)
student1.rate_lectore(lecturer3, 'Python', 10)
student1.rate_lectore(lecturer1, 'Python', 9.8)
student3.rate_lectore(lecturer3, 'Python', 7)
student3.rate_lectore(lecturer1, 'Python', 6)
student3.rate_lectore(lecturer1, 'Python', 9)
student4.rate_lectore(lecturer3, 'Python', 9.9)

student2.rate_lectore(lecturer2, 'Java', 9.9)
student2.rate_lectore(lecturer2, 'Java', 9.9)
student2.rate_lectore(lecturer2, 'Java', 10)

reviewer1.rate_hw(student1, 'Python', 7.5)
reviewer1.rate_hw(student1, 'Python', 8.0)
reviewer1.rate_hw(student1, 'Python', 9.9)
reviewer1.rate_hw(student3, 'Python', 7.5)
reviewer1.rate_hw(student3, 'Python', 8.0)
reviewer1.rate_hw(student3, 'Python', 7.9)
reviewer1.rate_hw(student4, 'Python', 5.5)
reviewer1.rate_hw(student4, 'Python', 9.0)
reviewer1.rate_hw(student4, 'Python', 6.9)

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
print(student4)
list_of_lect = [lecturer1, lecturer3]
list_of_st = [student1, student3, student4]

print(f"Средний рейтинг лекторов курса Python: {(averange(list_of_lect, 'Python')):0.1f}")
print(f"Средний балл студентов курса Python: {(averange(list_of_st, 'Python')):0.1f}")
