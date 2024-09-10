"""
1. Создайте список студентов. Каждый студент представлен словарём, содержащим имя и список его оценок.
2. Напишите цикл, который пройдётся по каждому студенту и рассчитает его средний балл.
3. Создайте функцию `calculate_average(grades)`, которая принимает список оценок и возвращает среднее значение.
Используйте эту функцию внутри цикла для вычисления среднего балла каждого студента.
4. Определите, является ли студент успешным или отстающим. Считайте, что студент успешен, если его средний балл выше
или равен 75. Добавьте логическое выражение, которое проверяет это условие, и выводит соответствующее сообщение.
5. Выведите для каждого студента сообщение следующего формата:
- Используйте f-строки для форматирования вывода.
6. Рассчитайте общий средний балл по всем студентам и выведите его.
7. Добавьте нового студента в список, используя метод `append`.
Удалите студента с самым низким средним баллом из списка.
"""


def calculate_average(grades):
    return sum(grades) / len(grades)


def successful_unsuccessful(average_score):
    return 'Успешен' if average_score >= 75 else 'Отстающий'


def expulsion_student(students_list_group):
    student_for_expulsion = {'average_score': 1_000_000}
    for student in students_list_group:
        if student['average_score'] < student_for_expulsion['average_score']:
            student_for_expulsion = student.copy()
    print(f'Студент {student_for_expulsion['name']}, со средним баллом {student_for_expulsion['average_score']:.2f} '
          f'отчислен!\n')
    students_list_group.remove(student_for_expulsion)
    return students_list_group


def enroll_student(students_list_group):
    name = input('Введите имя нового студента:')
    grades_student = []
    for i in range(1, 4):
        grades_student.append(int(input(f'Введите оценку № {i}: ')))
    students_list_group.append(
        {'name': name, 'grades': grades_student, 'average_score': calculate_average(grades_student)})
    print(f'Студент {name} успешно зачислен!\n')
    return students_list_group


def print_group_result(students_list_group):
    average_score_all = []
    print('Результаты успеваемости группы: ')
    for student in students_list_group:
        student['average_score'] = calculate_average(student['grades'])
        average_score_all.append(student['average_score'])
        print(f'Студент: {student['name']}\n'
              f'Средний балл: {student['average_score']:.2f}\n'
              f'Статус: {successful_unsuccessful(student['average_score'])}\n')
    print(f'Средний балл за группу: {calculate_average(average_score_all):.2f}\n')
    return students_list_group


students_list_group = [
    {'name': 'Yaroslav', 'grades': [80, 90, 100]},
    {'name': 'Alex', 'grades': [20, 30, 80]},
    {'name': 'Viktor', 'grades': [80, 85, 75]},
    {'name': 'Inna', 'grades': [10, 15, 12]},
]

if __name__ == '__main__':
    students_list_group = print_group_result(students_list_group)
    students_list_group = enroll_student(students_list_group)
    students_list_group = expulsion_student(students_list_group)
