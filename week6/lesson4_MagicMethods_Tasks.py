"""Task1"""
# class Account:
#     def __init__(self, name, balance, city):
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print('Счет создан')
    
#     def __repr__(self):
#         return f'{self.name} {self.balance}'
    
#     def __str__(self):
#         return f'Hello {self.name} {self.balance} {self.city}'
    
#     def __del__(self):
#         print('Пока')
        
# obj_account = Account("Rick", 2013, 'Bishkek')  
# print(obj_account)  
# print(repr(obj_account)) 


"""Task2"""
# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value
        
#     def __add__(self, num):
#         return f'Это сложение и результат равен: {self.value + num}'
    
#     def __sub__(self, num):
#         return f'Это вычитание и результат равен: {self.value - num}'

#     def __mul__(self, num):
#         return f'Это умножение и результат равен: {self.value * num}'
        
#     def __truediv__(self, num):
#         return f'Это деление и результат равен: {self.value / num}'

# obj_int = MyNumber(5)  
# print(obj_int + 5)  
# print(obj_int - 5)  
# print(obj_int * 5)  
# print(obj_int / 5) 


"""Task3"""
# class MyList(list):
#     def __init__(self, item):
#         self.item = item
        
#     def __getitem__(self, index):
#         return self.item[index-1]
    
# obj_list = MyList([1,2,3,4,5])  
# print(obj_list[1])


"""Task4"""
# class Student:
#     def __init__(self, name, class_name, ball):
#         self.name = name
#         self.class_name = class_name
#         self.ball = ball
#         score = {value for value in self.ball.values()}
#         self.mball = sum(list(score)) / len(list(score))   
        

#     def __gt__(self, other):
#         return f'> {self.mball > other.mball}'

#     def __lt__(self, other):
#         return f'< {self.mball < other.mball}'

#     def __ge__(self, other):
#         return f'>= {self.mball >= other.mball}'

#     def __le__(self, other):
#         return f'<= {self.mball <= other.mball}'


# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  

# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2)



"""Task5"""
class Word:
    def __init__(self, string):
        self.len_string = len(string)
        self.string = string
        
    def __new__(cls, self):
        return super(Word, cls).__new__(self.string.strip()) 

    def __gt__(self, other):
        return self.len_string > other.len_string

    def __lt__(self, other):
        return self.len_string < other.len_string

    def __ge__(self, other):
        return self.len_string >= other.len_string

    def __le__(self, other):
        return self.len_string <= other.len_string
        
    
        
word1 = Word('H  e  l  l  o')  
word2 = Word('world!')  
print(word1 > word2)  
print(word1 < word2)  
print(word1 >= word2)  
print(word1 <= word2) 