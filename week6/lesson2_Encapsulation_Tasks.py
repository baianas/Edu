#Task1
#  class A:
#     def public(self):
#         return 'Public method'
        
#     def _protected(self):
#         return 'Protected method'
        
#     def __private(self):
#         return 'Private method'
        
# obj1= A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())

# Task2
# class A:
#     def method1(self):
#         print('Hello World')
        
# class B(A):
#     pass

# b1 = B()
# b1.method1()

#Task3






"""
2. Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня
заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 %
заряда при каждом обращении.
Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
разряжен).
Также предусмотрите возможность заряжания батареи.
"""


class Phone:

    def __init__(self, imei, os_description, batery = 100):
        self._imei = imei
        self._batery = batery
        self._os_description = os_description

    # if self._batery <= 10:
    #         raise ValueError('Зарядите телефон!')
    # else:

    #     def method_info(self):
    #         self._batery -= 0.5
    #         print(self._batery)
            
    #     def music(self):
    #         self._batery -= 5
    #         print('Проигрывается музыка')

    #     def video(self):
    #         self._batery -= 7
    #         print('Проигрывается видео')


# a = Phone('23', 'Android', 15)
# a.music()
# a.music()
# a.method_info()