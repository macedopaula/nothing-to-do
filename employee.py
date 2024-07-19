from person import Person    
class Employee(Person):

    def __init__(self, name: str, birth_date: tuple, local_birth: str, extra_language: str):
        super().__init__(name, birth_date, local_birth)
        self.language.append(extra_language)

    def __str__(self):
        return super().__str__() + f'{self.name} speaks {self.language}.'





other = Employee('Lukas', (1998, 2, 26), 'Germany', 'English')
print(other)






            

    
