# В  проекте «Дом питомца» предполагается новая услуга: электронный кошелек.
# То есть система будет хранить данные о своих клиентах и их финансовых операциях.
# Вам нужно написать программу, обрабатывающую данные, и на выходе в консоль получить следующее:
# - Клиент «Иван Петров». Баланс: 50 руб.


class Users:
    def __init__(self, first_name='', second_name='', balance=0):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance

    def get_data(self, first_name):
        return self.first_name

    def get_name(self, second_name):
        return self.second_name

    def get_balance(self, balance):
        return self.balance


Ivan_Petrov = Users(first_name='Иван', second_name='Петров', balance=50)


print(f'Клиент "{Ivan_Petrov.first_name} {Ivan_Petrov.second_name}". Баланс: {Ivan_Petrov.balance}')
