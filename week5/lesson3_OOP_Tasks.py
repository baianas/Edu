# class Song:
#     def __init__(self, show_author, show_title, show_year):
#         self.show_title = f'Название этой песни {show_title}'
#         self.show_author = f'Автор этой песни {show_author}'
#         self.show_year = f'Эта песня вышла в {show_year} году'
        
        
# song = Song('Bob Marley', "Don't worry be happy", 1999)

# song.show_title
# song.show_author
# song.show_year

class ToDo:
    instances = dict()

    def __init__(self, task):
        self.task = task

    def give_priority(self, priority):
        self.instances[priority] = self.task

    def list_of_tasks(self):
        tasks = [(key, value) for key, value in self.instances.items()]

        def get_priority(to_do):
            return to_do[0]

        tasks.sort(key=get_priority)
        print(tasks)

to_do1 = ToDo("clean the house")
to_do1.give_priority(1)
to_do1.list_of_tasks()

to_do2 = ToDo("cook")
to_do2.give_priority(3)
to_do2.list_of_tasks()

to_do3 = ToDo('drive somewhere')
to_do3.give_priority(2)
to_do3.list_of_tasks()


