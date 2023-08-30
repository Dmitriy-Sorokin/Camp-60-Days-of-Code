class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        print(self.name.upper())

    def age(self, current_years):
        print(current_years - self.birthyear)


jon = User(name="Jon", birthyear=1999)

jon.get_name()
jon.age(current_years=2023)

