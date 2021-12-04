# Task1
# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass

# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass

# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()


# Task2
# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()


#Task3
# class MyString(str):
#     def __init__(self, string):
#         self.string = string
#     def append(self, string):
#         self.string = self + string

#     def pop(self):
#         poped = self.string[-1]
#         self.string = self.string[:-1]
#         return poped

#     def __str__(self):
#         return self.string


# example = MyString('String')
# example.append('hello')
# example.pop()
# print(example)


#Task4
# class MyDict(dict):
#     def get(self, key, default = 'Are you kidding?'):
#         return dict.get(self, key, default)
        
# obj_dict = MyDict({0: 'table'})
# print(obj_dict.get(0))

#Task5
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # print(str(self))
        
#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')
        
# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
        
#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')
        

# obj_student = Student('Rick', 21, 'science')
# obj_student.display()
# obj_student.display_student()


#Task6
class ContactList(list):
    def __init__(self, names):
        self.names = names
        
    
    def search_by_name(self, names):
        super().__init__(names)
        for i in self.names:
            if names in i:
                print(i)
    
all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya'))