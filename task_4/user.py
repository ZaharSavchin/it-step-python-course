from datetime import date


class User:
    def __init__(self, short_name, ful_name, year_of_birth, month_of_birth, day_of_birth):
        self.short_name = short_name
        self.ful_name = ful_name
        self.birth_day = date(year_of_birth, month_of_birth, day_of_birth)

    def get_short_name(self):
        return self.short_name

    def get_ful_name(self):
        return self.ful_name

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_day.year
        if self.birth_day.month >= today.month and self.birth_day.day > today.day:
            age -= 1
        return age

    def __str__(self):
        return f"{self.ful_name} {self.birth_day}"
#
#
# Zahar = User("Савчин З.С.", "Савчин Захар Сергеевич", 1996, 2, 3)
# print(Zahar)
# print(Zahar.get_short_name(), Zahar.get_ful_name(), Zahar.get_age())


