if __name__ == "__main__":

    class Student:
        def __int__(self, name, age, grades):
            self.name = name
            self.age = age
            self.grades = grades


        def add_grade(self, grade):
            self.grades.append(grade)

        def avarage_grade(self):
            return sum(self.grades) / len(self.grades)


    students_info = [
    {"name": "Ana", "age": 20, "grades": [8, 7, 9]},
    {"name": "Juan", "age": 22, "grades": [6, 8, 7]},
    {"name": "Pedro", "age": 21, "grades": [9, 10, 9]},
    ]

    students = [Student(info["name"], info["age"], info["grades"]) for info in students_info]

    threshold = 8

    passed_students = [student for student in students if student.average_grade() >= threshold]

    passed_students_dict = {student.name: student for student in passed_students}


