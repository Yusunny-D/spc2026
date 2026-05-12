from employee import Employee
from person import Person
from driver import Driver

employee1 = Employee('James', 25, 'Samsung')
employee2 = Employee('Sunny', 25, 'LG')
employee3 = Person('John', 25)
employee4 = Driver('Sam', 25, 'BMW')


employee1.greet()
employee2.greet()
employee3.greet()
employee4.greet()


employee3.set_age(40)
employee3.greet()
print(employee3.get_name())


employee4.drive()
employee4.drive_fast()