class GenderTransformer:

    def __init__(self, gender: str) -> None:
        self.gender = gender

    def std_gender(self) -> str:

        if self.gender.lower() == 'male':
            return 'm'
        elif self.gender.lower() == 'female':
            return 'f'
        else:
            return 'o'


class AgeTransformer:

    def __init__(self, age: str) -> None:
        self.age = age

    def std_age(self) -> str:
        if self.age < '18':
            return 'young'
        elif self.age < '35':
            return 'adult'
        elif self.age < '55':
            return 'golden'
        else:
            return 'others'
