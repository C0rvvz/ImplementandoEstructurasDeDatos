if __name__ == "__main__":

    class Student:
        def __init__(self, name, age, grades):
            self.name = name
            self.age = age
            self.grades = grades


        def add_grade(self, grade):
            self.grades.append(grade)

        def avarage_grade(self):
            return sum(self.grades) / len(self.grades)


    students_info = [
        {"name": "juan", "age": 12, "grades":  [1, 2, 3]},
        {"name": "juliana", "age": 20, "grades": [3, 4, 5]},
        {"name": "jhon", "age": 19, "grades": [2, 5, 3]},
        {"name": "joaquin", "age": 21, "grades": [1, 4, 5]},
        {"name": "jose", "age": 18, "grades": [0, 2, 5]},
    ]
    students_list = [Student(datos["name"], datos["age"], datos["grades"])for datos in students_info]
    umbral = 3

    lista_estudiantes_ganados = [estudiante for estudiante in students_list if estudiante.avarage_grade() >= umbral]

    dict_estudiante = {estudiante.name: estudiante for estudiante in students_list if estudiante.avarage_grade()>umbral}



