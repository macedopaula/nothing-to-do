class Person:
    
    def __init__(self, name: str, birth_date: tuple, local_birth: str ):
        self.name = name
        self.birth_date = birth_date # (year, month, date)
        self.local_birth = local_birth
        self.language = ['German']

    def calculate_age(self):
        from datetime import date

        today = date.today()
        
        try:
            from date_validator import date_validator
            date_validator(self.birth_date[0], self.birth_date[1], self.birth_date[2])
        except:
            print('Invalid birthdate')
        else:
            if(self.birth_date[1] == today.month):
                if(self.birth_date[2] > today.day):
                    return today.year - self.birth_date[0] - 1
                else:
                    return today.year - self.birth_date[0]
            elif((self.birth_date[1] > today.month)):
                return today.year - self.birth_date[0] - 1
            else:
                return today.year - self.birth_date[0]
        
        
    def __str__(self):

        age = Person.calculate_age(self)
        return f'{self.name} is {age} years old and was born in {self.local_birth}. '