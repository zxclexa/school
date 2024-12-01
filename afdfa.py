from school_diary import rates

class StudentsManager:
    def add_grades(self):
        # Чтение данных об учениках из файла students.txt
        with open('math.txt', 'r', encoding='utf-8') as file:
            students = file.read().strip().split("\n")  # Считываем каждую строку как отдельного ученика

        # Получаем имена учеников
        student_names = [student.split(':')[0].strip() for student in students]

        # Запрашиваем оценки для каждого ученика
        for name in student_names:
            grades_input = input(f'Input grades for student "{name}" (space-separated): ')
            # Преобразуем ввод в список целых чисел
            grades = self.parse_grades(grades_input)
            self.save_grades(name, grades)

    def parse_grades(self, grades_input):
        """ Преобразует вводимые оценки в список целых чисел."""
        try:
            # Разбивает строку введенных оценок и преобразовывает в список целых чисел
            return list(map(int, grades_input.split()))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            return []

    def save_grades(self, name, grades):
        """
        Сохраняет оценки ученика в файл students_grades.txt.
        Оценки записываются в формате 'Имя: оценки'.
        """
        with open('math.txt', 'a', encoding='utf-8') as f:
            grades_str = " ".join(map(str, grades))
            f.write(f'{name}: {grades_str}\n')
        print(f'Grades for "{name}" saved: {grades_str}')

# Пример использования класса StudentsManager
if __name__ == "__main__":
    students_manager = StudentsManager()
    students_manager.add_grades()

#def print_rates():
#    with open('math.txt', 'r', encoding='utf-8') as f:
#        for i in f:
#            print(i, end='')
#
#
#a = input('Выберете действие: Ввод новых оценок(1);Зачисление ученика(2): ')
#if a=='1':
#    q=input('Введите имя/ID ученика: ')
#    w=input('Введите оценку: ')
#    with open('math.txt', 'r+', encoding='utf-8') as f:
#        rates = f.read().strip().split()

        #for i in enumerate(f):
        #    print(i)
        #    if q in i:
        #        print('fff')


#print_rates()

#with open(r"math.txt", 'r', encoding='utf-8') as fp:
#    # lines to read
#    line_numbers = [4, 7]
#    # To store lines
#    lines = []
#    for i, line in enumerate(fp):
#        # read line 4 and 7
#        if i in line_numbers:
#            lines.append(line.strip())
#        elif i > 7:
#            # don't read after line 7 to save time
#            break
#print(lines)