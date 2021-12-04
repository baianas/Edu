# sudo apt-get install git

# Регистрация в github/gitlab/bitbucket

# настройка
# git config --global user.email "shermatovbaianas@gmail.com(почта)"
# git config --global user.name "baianas(имя)"

# создание ключа
# ssh-keygen  #-t rsa -> етод шифрования

# cat ~/.ssh/id_rsa.pub  показывает публичный ключ

# полученный ключ добавляем в профиль github

# создание нового репозитория

# git init - преврашаем текущую директорию в git репозиторий

# git remote add origin(название, можно любое, но предпочтительно origin) git@github.com:baianas/test_repo.git
# 
# git remote -v -> посмотр списка удаленных репозиториев
# git remote rm <имя> -> удаление из списка


"""Работа с репозиторием"""
# git status - проверка изменений
# git diff - проверка изменений построчно

# git add <название файла> -> добавялет файл(ы) в версию(закомитить)

# git commit -m "Add file1" -> на основе добавленных файлов создаёт коммит(версию)

# git log - просмотр изменений

# git log --oneline - короткая версия просмотра истории версий

# git log -p

# git push origin master - пушить код из локального в удаленный

# git push -> отправка версии в удаленный репозиторий

# git clone <ссылка>

# git pull origin master -> получение версий из удаленного репозитория


# git checkout - переход по веткам

# git branch -D <название ветки>  -> удалить ветку

# git checkout <name> - отменяет послед действ. до комита

# git branch имя - создание ветки
# git branch - список веток
# git branch -D <название ветки>  -> удалить ветку

# git checkout -b имя - создание ветки и переход на нее
# git checkout имя_файла - удаление файлов из staging area

# git reset - удаление файлов из staging area
# git reset имя

# git reset HEAD~ - удаление коммитов

# git .gitignore -> не показывать в github