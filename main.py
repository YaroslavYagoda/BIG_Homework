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
    global average_score_all
    average_score_all.append(sum(grades))
    return sum(grades) / len(grades)


def successful_unsuccessful(average_score):
    return 'Успешен' if average_score >= 75 else 'Отстающий'


def calculate_average_all(average_score_all):
    return sum(average_score_all) / len(average_score_all)


def expulsion_student(average_score_all):
    global students_list_group
    student_index = average_score_all.index(min(average_score_all))
    print(f'Студент {students_list_group[student_index]["name"]} изгнан!\n')
    students_list_group.pop(student_index)


def enroll_student():
    global students_list_group
    name = input('Введите имя нового студента:')
    grades_student = []
    for i in range(1, 4):
        grades_student.append(int(input(f'Введите оценку № {i}: ')))
    students_list_group.append({'name': name, 'grades': grades_student})
    print(f'Студент {name} успешно зачислен!\n')


def print_group_result():
    global average_score_all
    average_score_all = []
    for student in students_list_group:
        average_score = calculate_average(student['grades'])
        print(f'Студент: {student["name"]}\n'
              f'Средний балл: {average_score:.2f}\n'
              f'Статус: {successful_unsuccessful(average_score)}\n')
    print(f'Средний балл за группу: {calculate_average_all(average_score_all):.2f}\n')


average_score_all = []
students_list_group = [
    {'name': 'Yaroslav', 'grades': [80, 90, 100]},
    {'name': 'Alex', 'grades': [20, 30, 80]},
    {'name': 'Viktor', 'grades': [80, 85, 75]},
    {'name': 'Inna', 'grades': [10, 15, 12]},
]
if __name__ == '__main__':
    print_group_result()
    expulsion_student(average_score_all)
    enroll_student()
    print_group_result()
