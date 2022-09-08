from Exercises.inheritance.person import Employee
from Exercises.inheritance.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'
