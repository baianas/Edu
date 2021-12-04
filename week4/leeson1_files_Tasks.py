#Task1
# with open('task1.txt', 'r') as file:
#     for line in file.readlines(8):
#         print(line)

# file  = open("task1.txt", "r")
# numbers = file.readlines()
# number = [int(i.replace('\n', '')) for i in numbers[:5]]

# for i in numbers:
#     print(i)

# file.close()


#Task2
# with open('task2.txt', 'r') as file:
#     for line in file:
#         print(line)


# #Task3
# from os import write


# with open('task3.txt', 'w+') as file:
#     file.write('0*1*2*3*4*5*6*7*8*9*')
#     file.seek(0)
#     print(file.read())

# with open('task3.txt', 'w+') as file:
#     a = ''.join([str(i) + '*' for i in range(10)])
#     file.write(a)
#     file.seek(0)
#     print(file.read())


#Task4
# with open('task4.txt', 'r') as file:
#     text = file.readlines()
#     size = len(text)
#     print(size)


#Task5
