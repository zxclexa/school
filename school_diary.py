
class Visiting:
    def __init__(self):
        pass

    def display_visitings(self):
        print('\nКоличество пропусков студентов: ')
        for i in visitings:
            print(i, visitings[i])

    def add_visitings(self,name):
        visitings[name]+=1

class Rates:
    def __init__(self,diary_math, diary_ru_lang, diary_en_lang):
        self.diary_math=diary_math
        self.diary_ru_lang=diary_ru_lang
        self.diary_en_lang=diary_en_lang

    def display_all_rates(self):
        print('\nОценки по математике: ')
        for i in diary_math:
            print(i, *diary_math[i])
        print('\nОценки по русскому языку: ')
        for i in diary_math:
            print(i, *diary_ru_lang[i])
        print('\nОценки по английскому языку: ')
        for i in diary_en_lang:
            print(i, *diary_ru_lang[i])

    def add_rate(self, rate,subject,name):
        if subject == '1':
            if name in self.diary_math:
                self.diary_math[name].append(rate)  # Добавляем оценку в список
            else:
                print('\nТакого ученика нет.')  # Создаем запись для нового ученика

        elif subject == '2':
            if name in self.diary_ru_lang:
                self.diary_ru_lang[name].append(rate)
            else:
                print('\nТакого ученика нет.')

        elif subject == '3':
            if name in self.diary_en_lang:
                self.diary_en_lang[name].append(rate)
            else:
                print('\nТакого ученика нет.')
        else:
            print("\nНеизвестный предмет.")


class Students:
    def __init__(self,name):
        self.name=name
    pass


diary_math = {
    'Прохор Тигранович': [5,2,3,4],
    'Эльнара Андреевна': [4,5,3,5]
}

diary_ru_lang = {
    'Прохор Тигранович': [2,2,3,4],
    'Эльнара Андреевна': [4,5,2,5]
}

diary_en_lang = {
    'Прохор Тигранович': [5,5,5,4],
    'Эльнара Андреевна': [4,5,5,5]
}

visitings = {
    'Прохор Тигранович': 1,
    'Эльнара Андреевна': 2
}



#ПОСЕЩЕНИЯ
v = Visiting()
v.display_visitings()
v.add_visitings('Прохор Тигранович')
v.display_visitings()

#ОЦЕНКИ
r = Rates(diary_math, diary_ru_lang, diary_en_lang)
r.display_all_rates()

r.add_rate(5, '1', 'Прохор Тигранович')
r.add_rate(3, '2', 'Эльнара Андреевна')
r.add_rate(4, '3', 'Новый Ученик')


r.display_all_rates()