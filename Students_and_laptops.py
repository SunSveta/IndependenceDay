
class Student:

    def __init__(self, name, stud_id):
        self.name = name
        self.stud_id = stud_id
        self.lap = self.Laptop()

    def show(self):
        print(f'{self.name} {self.stud_id}\n{self.lap.brand} {self.lap.cpu} {self.lap.ram}')

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8


s1 = Student('Ivan', 2)
s2 = Student('Mary', 3)
s1.show()
s1.lap.ram = 16
s1.show()
lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))