from threading import Lock, Thread
from time import sleep


class Bank:
    # Глобальный lock, который будет использоваться для всех банков
    lock = Lock()

    def __init__(self, name, money=100):
        self.name = name
        self.money = money

    def replenish(self, s=10):
        print(self.money, 'money:', self.name)
        # Захватываем глобальный lock, чтобы несколько потоков не могли изменять значения денег одновременно
        with Bank.lock:
            self.money += s
        print('Replenish cash:', self.name)

    def withdraw(self, s=10):
        print(self.money, 'money:', self.name)
        sleep(1)
        # Захватываем глобальный lock, чтобы несколько потоков не могли изменять значения денег одновременно
        with Bank.lock:
            self.money -= s
        print('Withdraw cash:', self.name)

    def transfer(self, friend_bank, s=10):
        print('Lock myself: ', self.name)
        self.withdraw(s)
        print('Lock friend: ', friend_bank.name)
        friend_bank.replenish(s)


class User(Thread):
    def __init__(self, name, bank, friend_bank):
        super().__init__(name=name)
        self.name = name
        self.bank = bank
        self.friend_bank = friend_bank

    def run(self):
        print(f'{self.name} try to transfer to {self.friend_bank.name}')
        # Проверяем, не пытается ли пользователь перевести деньги на тот же самый банк
        if self.bank == self.friend_bank:
            print(f"{self.name} can't transfer to the same bank")
        # Устанавливаем одинаковый порядок захвата lock'ов для всех потоков
        # Теперь банки будут блокироваться в одном и том же порядке, чтобы избежать deadlock'ов
        elif self.bank.name < self.friend_bank.name:
            with self.bank.lock, self.friend_bank.lock:
                self.bank.transfer(self.friend_bank)
        else:
            with self.friend_bank.lock, self.bank.lock:
                self.bank.transfer(self.friend_bank)
        print(f'{self.name} made transfer operation to {self.friend_bank.name}')


bank1 = Bank('Bob')
bank2 = Bank('Kate')
bank3 = Bank('Ann')

user1 = User('Bob', bank1, bank2)
user2 = User('Kate', bank2, bank3)
user3 = User('Ann', bank3, bank2)

user1.start()
user2.start()
user3.start()

user1.join()
user2.join()
user3.join()

print(bank1.money)
print(bank2.money)
print(bank3.money)
