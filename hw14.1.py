class GroupFullException(Exception):
    def __init__(self, message="Група вже заповнена! Неможливо додати більше 10 студентів."):
        super().__init__(message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} років'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, Залікова книжка: {self.record_book}'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError('Можна додавати лише студентів')
        if len(self.group) >= 10:
            raise GroupFullException()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Група №{self.number}\n{all_students}'


students = [
    Student('Male', 20, f'Name{i}', f'Last{i}', f'RB{i}') for i in range(11)
]

group = Group('PD2')

for i, student in enumerate(students):
    try:
        group.add_student(student)
        print(f'✅ Студент {student.last_name} доданий.')
    except GroupFullException as e:
        print(f'❌ {e} (студент {student.last_name})')

# Вивід результату
print("\n=== Склад групи ===")
print(group)
