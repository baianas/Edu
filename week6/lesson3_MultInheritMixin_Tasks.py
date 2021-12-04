"""Task1"""
# class Auto:
#     def ride(self):
#         print('Riding on a ground')


# class Boat:
#     def swim(self):
#         print('Floating on water')


# class Amphibian(Auto, Boat):
#     pass


# obj = Amphibian()
# obj.ride()
# obj.swim()


"""Task2"""
# class RadioMixin:
#     def play_music(self, title):
#         print(f'Песня называется {title}')
        

# class Auto(RadioMixin):
#     pass


# class Boat(RadioMixin):
#     pass


# class Amphibian(Auto, Boat, RadioMixin):
#     pass


# auto = Auto()
# boat = Boat()
# obj = Amphibian()

# auto.play_music('Ayigyr')
# boat.play_music('Shrek')
# obj.play_music('OSel')

"""Task3"""
# class Clock:
#     def current_time(self):
#         from datetime import datetime
#         print(datetime.now().time().strftime('%H:%M:%S'))
        
    
# class Alarm:
#     def on(self):
#         print('Будильник включен')
        
#     def off(self):
#         print('Будильник выключен')
        
        
# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         super().on()
        
        
# clock = AlarmClock()
# clock.current_time() 
# clock.alarm_on() 


"""Task4"""
# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0
#     @abstractmethod
#     def get_info(self):
#         pass

#     @abstractmethod
#     def coding(self):
#         pass


# class Backend(Coder):
#     def __init__(self, languages_backend, experience) -> None:
#         self.experience = experience
#         self.languages_backend = languages_backend

#     def get_info(self):
#             return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

#     def coding(self, time):
#             self.count_code_time += time

# class Frontend(Coder):
#     def __init__(self, languages_frontend, experience) -> None:
#         self.experience = experience
#         self.languages_frontend = languages_frontend

#     def get_info(self):
#             return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

#     def coding(self, time):
#             self.count_code_time += time


# class Fullstack(Backend, Frontend):
#     pass

# a = Backend('Python', 'Junior')
# b = Frontend('JavaScript', 'Middle')
# c = Fullstack('Python and JS', 'Senior')
# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 


"""Task5"""
# class Square:
#     def __init__(self, side):
#         self.side = side

#     def get_area(self):
#         return int(self.side ** 2)

# class Triangle:
#     def __init__(self, height, base) -> None:
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return int(0.5 * self.height * self.base)

# class Pyramid(Triangle, Square):
    
#     def get_volume(self):
#         return int((1/3) * (self.base ** 2) * self.height)
        