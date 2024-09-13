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
    if students_list_group:
        student_for_expulsion = {"average_score": 1_000_000}
        for student in students_list_group:
            if student["average_score"] < student_for_expulsion['average_score']:
                student_for_expulsion = student.copy()
        print(
            f'\nСтудент {student_for_expulsion["name"]}, со средним баллом {student_for_expulsion["average_score"]:.2f}'
            f' отчислен!\n')
        students_list_group.remove(student_for_expulsion)
    else:
        print('\nГруппа пустая (студенты не внесены в список)!!!\n')


def enroll_student(students_list_group):
    name = ''
    while not name.isalpha():
        name = input('\nВведите имя нового студента:')
    grades_student = []
    for i in range(1, 4):
        grade = ''
        while not grade.isdigit():
            grade = input(f'Введите оценку № {i}: ')
        grades_student.append(int(grade))
    students_list_group.append(
        {'name': name, 'grades': grades_student, 'average_score': calculate_average(grades_student)})
    print(f'\nСтудент {name} успешно зачислен!\n')


def print_group_result(students_list_group):
    if students_list_group:
        average_score_all = []
        print(f'\nСтудентов в группе: {len(students_list_group)}')
        print('\nРезультаты успеваемости группы: \n')
        for student in students_list_group:
            average_score_all.append(student["average_score"])
            print(f'Студент: {student["name"]}\n'
                  f'Средний балл: {student["average_score"]:.2f}\n'
                  f'Статус: {successful_unsuccessful(student["average_score"])}\n')
        print(f'Средний балл за группу: {calculate_average(average_score_all):.2f}\n')
    else:
        print('\nГруппа пустая (студенты не внесены в список)!!!\n')


def group_managment():
    print('*' * 100, '\nВы находитесь в разделе управления группой № 127/01\n')
    choice = ''
    while choice not in ['1', '2', '3', '4']:
        print('Необходимо выбрать действие введя его цифру:\n\n'
              '1. Просмотр результатов успеваемости группы.\n'
              '2. Добавить в группу нового студента.\n'
              '3. Убрать из группы студента с самым низким средним баллом.\n'
              '4. Завершить работу с группой (выход).\n')
        choice = input('Введите номер желаемого действия: ')
    if choice == '1':
        print_group_result(students_list_group)
    elif choice == '2':
        enroll_student(students_list_group)
    elif choice == '3':
        expulsion_student(students_list_group)
    elif choice == '4':
        return 'exit'


"""
Изначальная группа студентов убрана, если хотите создать свою пользуйтесь функционалом программы
students_list_group = [
    {'name': 'Yaroslav', 'grades': [80, 90, 100]},
    {'name': 'Alex', 'grades': [20, 30, 80]},
    {'name': 'Viktor', 'grades': [80, 85, 75]},
    {'name': 'Inna', 'grades': [10, 15, 12]},
]"""
students_list_group = []
if __name__ == '__main__':
    ext = ''
    while ext != 'exit':
        ext = group_managment()
