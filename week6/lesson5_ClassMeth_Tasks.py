"""Task1"""
# class Product:
#     base_price = 20000
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
        
#     def has_garantiya(self, year):
#         if year - self.year > 2:
#             return 'Ваша гарантия истекла'
#         return 'Гарантия действительна'
        
#     @classmethod
#     def change_price(cls, rate):
#         cls.base_price *= rate 

# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price) 


"""Task2"""
# class User:
#     def __init__(self, name, lastname, email):
#         self.name = name
#         self.lastname = lastname
#         self.email = email
        
#     @staticmethod
#     def validate_email(email):
#         if '@' in email:
#             return True
#         else:
#             return False

#     def __str__(self):
#         if self.validate_email(self.email):
#             return f"{self.name}: {self.email}"
#         else:
#             return f"email в неправильном формате"
            
#     @classmethod
#     def create_user(cls,string:str):
#         name, last_name, email = string.split(', ')
#         return cls(name,last_name,email)


# user1 = User.create_user('John, Snow, john@email.com') 
# user2 = User.create_user('Mary, Antuanetter, antygmail.com')

# print(user1) 
# print(user2)


"""Task3"""
# class Makers:
#     student_count = 0
#     def __init__(self, name, language, kpi):
#         self.name = name
#         self.language = language
#         self.kpi = kpi
        
#     @classmethod
#     def new_student(cls, name, language, kpi):
#         cls.student_count += 1
#         return cls(name, language, kpi)
        
#     def get_info(self):
#         return f'Student name: {self.name}, Language: {self.language}'
        
#     def set_kpi(self, kpi):
#         self.kpi = kpi
#         return self.kpi
        
# student1 = Makers.new_student(name = 'Vlad', language = 'Python', kpi = 0)
# student2 = Makers.new_student(name = 'Malik', language = 'JavaScript', kpi = 0)

# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.student_count) 


"""Task4"""
# class Bike:
#     def __init__(self,cost,make,model,year, min_profit):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self._sale_price = None
#         self.sold = False
#         self.min_profit = min_profit
      
#     def set_cost(self, sale_price):
#         if sale_price < self.cost:
#             self._sale_price = sale_price + self.min_profit
#             return self._sale_price
#         else:
#             self._sale_price = sale_price
#             return sale_price
    
#     def service(self, service_cost):
#         self._sale_price += service_cost
#         return self.cost
    
#     def sell(self):
#         self.sold = not self.sold
#         profit = self.cost - self._sale_price
#         return profit

#     @classmethod
#     def get_default_bike(cls):
#         return cls(cost = 10000, make = "Author", model ="Basic ASL",year = 2020, min_profit = 2000)

# bike = Bike.get_default_bike() 
# bike.set_cost(6000) 
# bike.service(300) 
# print(bike.sell()) 
# print(bike.cost) 
# print(bike.make) 
# print(bike.year) 
# print(bike._sale_price) 
# print(bike.sold) 
# print(bike.min_profit) 

        
"""Task5"""
# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount= amount
    
#     def update(self, new_amount):
#         self.amount = new_amount

#     def __repr__(self):
#         return f'{self.amount}'
        
#     @staticmethod
#     def dollarize(float_num):
#         if float_num < 0:
#             float_num = abs(float_num)
#             amount = "-${:,.2f}".format(float_num)
#             return amount        
#         else:
#             amount = "${:,.2f}".format(float_num)
#             return amount
    
#     def __str__(self):
#         return self.dollarize(self.amount)
        
    
# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash)) 