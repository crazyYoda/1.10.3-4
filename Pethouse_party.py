# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
# Решите задачу с помощью метода конструктора и примените один из принципов наследования.
# При выводе в консоль вы должны получить:  «Иван Петров, г. Москва, статус "Наставник"»

class Users:
    def __init__(self, first_name='', second_name=''):
        self.first_name = first_name
        self.second_name = second_name

    def get_data(self):
        return self.first_name

    def get_name(self):
        return self.second_name

    def get_balance(self):
        return self.balance


class Guest(Users):

    def __init__(self, first_name='', second_name='', city='', status=''):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.status = status


Ivan_Petrov = Guest(first_name='Иван', second_name='Петров', city='Москва', status='статус "Наставник"')

print(f'Клиент "{Ivan_Petrov.first_name} {Ivan_Petrov.second_name}", г. {Ivan_Petrov.city}, {Ivan_Petrov.status}')
