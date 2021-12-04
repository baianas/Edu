# psql  ->вход в БД как название компа(главный юзер)

# sudo -u postgres psql postgres ->вход в БД как postgres


"""ТИПЫ ДАННЫХ"""
# целые числа:
# SMALLINT, INT2        -32768 до 32768
# INTEGER, INT, INT4    -2147483648 до 2147483648 
# BIGINT, INT8          -9223372036854775808 до 9223372036854775808

# SMALLSERIAL   1 до 32768
# SERIAL        1 до 2147483648
# BIGSERIAL     1 до 9223372036854775808

"FLOAT"

# REAL                  точность до 6 знаков
# DOUBLE PRECISION      точность до 15 знаков

# DECIMAL(кол-во символов, после запятой)
# NUMERIC(кол-во символов, после запятой)


# MONEY   - точность 2 знака после запятой, также хранит валюту

"STRING"
# CHAR - строка с фиксированной длиной
# VARCHAR - строка с максимальной длиной
# TEXT - строка неограниченной длины

# CHAR(10)      -> hello -> 'hello     '
# VARCHAR(10)   -> hello -> 'hello'

"boolean"

# t/f -> True/False, TRUE/FALSE, 1/0, On/Off, YES/NO

"Дата и время"
# DATE (4 байта) -> '2021-09-21'
# TIME (8 байт)  -> '18:23:59'
# TIMESTAMP (8 байт) -> '2021-09-21 18:25:21'


"""ОГРАНИЧЕНИЯ (constraint)"""
# NULL/NOT NULL     ->указывает, может ли столбец быть пустым или нет
# DEFAULT           -> задаёт значение по умолчанию
# UNIQUE            -> значения в столбце должны быть уникальными
# PRIMARY KEY       -> указывает, какой столбец будет ключем(NOT NULL + UNIQUE + INDEX)
# FOREIGN KEY       -> внешний ключ, ссылка на другую таблицу
# CHECK             -> проверяет значение на определённое условие

# create database name_of_database;  ->создать базу данных с именем
# drop datebase name_of_database;  ->удалить базу данных(находясь в другой бд, + если нужно удалить бд другого юзера нужен superuser)
# drop role name_user;  ->удаляет юзера

# \l -> список бд

# \c name_of_database  -> коннект к бд с именем

# \du  -> показывает список всех юзеров и их роли

# CREATE USER test_user(имя юзера) WITH PASSWORD '(password)';  -> создаём юзера с паролем

# ALTER ROLE test_user(имя) WITH SUPERUSER;  -> даем права суперюзера(может вносить любые изменения)
# alter role name(imya) with superuser, createrole, credatedb, replication, bypassrls;   ->дали все привелегии

# exit -> выход

# CREATE DATABASE test_user(нужно создавать бд с таким же названием как юзера);

# psql -U test_user  -> войти как test_user

# grant all privileges on database test_user(название бд) to test_user;  -> дает привелегии почти как у овнера, овнера поменять нельзя

# create database my_db_test_user woth owner test_user;  -> создать бд с другого профиля в профиле тест юзер



# CREATE TABLE Person(
# test_user(# id serial primary key,
# test_user(# name varchar(50) NOT NULL,
# test_user(# last_name varchar(100),
# test_user(# age int);

# \dt  ->показыает таблицу

# \d name_of_table  ->показывает поля таблицы


"""INSERT"""
# INSERT INTO name_of_table (name, last_name, age) VALUES ('John', 'Snow', 34);  # можно прописать(id, name, last_name, age)

#  INSERT INTO name_of_table (name, last_name, age) VALUES ('Emily', 'Clark', 23), ('John', 'Snow', 34);  -> можно сразу несколько


"""SELECT"""# --> 
# select *(* = all) from name_of_table;  ->показывает таблицу
# select name, last_name from name_of_table;  ->можно выбрать что именно вытащить
# select * from name_of_table where age > 40;  -> where - условие, как if(сейчас выводит старше сорока)
# select column from table_name;
# select column1 || ' ' || column2 as column_name from table_name;  --> вытащить столбцы column1, column сконкатенировав под названием column_name из table_name

# delete from students where age < 18;  ->удаление по возрасту

# update  students set age = 32;  -> поменять возраст всех строк
# # update  students set age = 32 where id = 1  -> поменять возраст где id = 1


"""ORDER BY"""  #  -->упорядочивание
# select * from table_name order by column(asc);  --> упорядочивает элементы стобца column по возрастанию
# select * from table_name order by column1, column2(asc); --> упорядочивает элементы стобца сперва по column1, потом column2 по возрастанию
# select * from table_name order by column desc;  --> упорядочивает элементы стобца column по убыванию
# select * from table_name order by column1, column2 desc; --> упорядочивает элементы стобца сперва по column1, потом column2 по убыванию
# select * from table_name order by column nulls first;  --> пустые поля выйдут в начале
# select * from table_name order by column nulls last;  --> пустые поля выйдут в конце


"""DISTINCT"""  # -->избавляет от дубликатов
# select distinct column from table_name;  -->избавляет от дубликатов
# select distinct on(column1) column1, column2 from table_name order by column1, column2;  -->избавляет от дубликатов


"""WHERE"""  # -->условие, как if
"можно использовать операторы: and, or, not"

"""BETWEEN"""  # -->между
# select * from name_oof_table where column between condition1 and condition2;
# EXAMPLE:
# example1:
# select * from name_of_table where age between 20 and 30;  --> выведет столбец имен в промежутке от 20 до 30 лет
# example2:
# select * from name_of_table where (age between 20 and 30) and (experience between 3 and 9);  --> выведет столбец имен в промежутке от 20 до 30 лет и с опытом работы от 3 до 9 лет включительно


"""LIKE"""
# select * from table_of_name where column like '%';
# EXAMPLE:
# example1:
# select * from info where name like 'A%';  --> вытаскивает где имна начинаются на 'A' и за ним может быть любой символ, даже пустота. 
"Знак % означает любое количество символов"
"можно использовать как %symbols означает, что перед symbols может быть любое количество символов"
# example2:
# select * from info where name like 'A_';  --> вытаскивает где имна начинаются на 'A' и за ним может быть только один любой другой символ

"""ILIKE"""
"""тот же LIKE, но не чувтвителен к регистру"""


"""IS NULL"""  #ищет нулевые значения
# select * from name_of_table where column is null

"""LIMIT/OFFSET"""  # -->лимитирует/начинает с
# select * from name_of_table limit 10  --> выведет 10 элементов
# select * from name_of_table order by column limit 10 -->выведет упоряд. 10 элементов

# OFFSET  --> начать с
# select * from name_of_table order by column limit 10 offset 4; -->выведет упоряд. 10 элементов начиная с 4го(т.е. пропускает 1-ые 4 элемента и выводит с 5го 10 элементов)


"""FETCH"""  #тот же лимит, но желательнее его использовать
# select * from name_of_table order by column fetch first (num) row only;   --> выведет первые num элементов
# select * from name_of_table order by column offset (num2) fetch first (num) row only;   --> выведет первые num элементов начиная с num2(т.е. пропустит num2 элементов и насчнет с num2 +=1 и выведет num элементов)


"""GROUP BY"""
"Агрегационные функции"
# select sum(age) as age_sum from name_of_table where country = 'Country1';  --> выведет сумму возрастов из страны Country1
# select count(column) from name_of_table

# select count(id) from name_of_table where email like '%yahoo.com';  -->выводит количество, подходящих элементов
"С group by" 
#select country, count(id) from name_of_table group by country  -->выводит группируя по стране
# select country, sum(experience) from name_of_table group by country  -->выводит группируя по стране сумму опыта

# select avg(experience) from name_of_table;  -->средняя опыта всех программистов
# select country, avg(age) from name_of_table group by country  -->выводит группируя по стране средний возраст

# select max(age) from name_of_table -->количество самых старших 

"""HAVING = WHERE"""  #то же, что и where, но используется только с group by
# select programming_language, avg(experience) from name_of_table group by programming_language having avg(experience) > 2;   -->выводит язык программирования где средний опыт больше 2 группируя по языку программирования


"""UPDATE"""
"UPDATE table_name SET column1=value1, column2=value2 WHERE condition;"
# update table_name set column1='SOME1', column2='SOME2' where id=num;  -->поменяет значение в столбце column1, column2 где id = num


"""DELETE"""
"DELETE FROM table_name WHERE condition"
# delete from info where id=17;  ->удаляет где id=17
# delete from info where age is null;  -->удляет все, где возраст не указан



"""ALTER TABLE"""  #--> редактирование таблицы и её столбцов
"ALTER TABLE table_name ADD/RENAME/DROP/ALTER COLUMN ..."

"переименование таблицы"
# alter table table_name rename to new_table_name

"переименование столбца"
# alter table table_name rename column column_name to new_column_name;

"добавить новый столбец"
# alter table table_name add column column_name constraint(ограничения)

"изменения типа столбца"
# alter table table_name alter column column_name type new_type

"удаление столбца"
# alter table table_name drop column_name1, drop column2_name

"Установка/снятие ограничений"

# NULL/NOT NULL, DEFAULT
# ALTER TABLE table_name ALTER COLUMN column_name SET|DROP NOT NULL

# ALTER TABLE table_name ALTER COLUMN column_name SET|DROP DEFAULT ЗНАЧЕНИЕ


# ALTER TABLE table_name ADD CONSTRAINT constraint_name ОГРАНИЧЕНИЕ(столбец)

# ALTER TABLE products ADD CONSTRAINT price_check CHECK(price > 0)

# ALTER TABLE products DROP CONSTRAINT price_check;


# ALTER TABLE название_таблицы ADD PRIMARY KEY(id);


''' Основные команды для манипуляции с записями в таблице'''
# SELECT, INSERT, UPDATE, DELETE

# INSERT INTO название_таблицы (поля) VALUES (значения);

# SELECT * FROM название_таблицы; --> выбираемвсю таблицу (все столбцы и строки)
# SELECT name FROM название; --> выбирает конкретный столбец

#фильтрация
# SELECT * FROM название_таблицы WHERE условие;

# # UPDATE - редактировать все записи или часть записей
# update products set price = price - 10000;

# UPDATE * FROM products;
# UPDATE * FROM products WHERE id = 1;
# UPDATE * FROM products WHERE price > 50000;

#DELETE
# DELETE * FROM products;
# DELETE * FROM products WHERE id = 1;
# DELETE * FROM products WHERE price > 50000;



"""         <-------->          """
"""         <-------->          """
"""         <-------->          """
"""         <-------->          """
"""         <-------->          """
"""         <-------->          """

# alter table info alter column name(column) type varchar(80);  --> поменяли максимальную длину
# alter table info alter column last_name set not null;  -->поменяли на то, чтобы не было пустой графы
# alter table info rename column last_name to surname;  -->поменять название столбца
# alter table info add constraint name_of_constraint unique (name);  --> 
# alter table info drop age, drop email;   -->удаляем столбцы


"""Операторы сравнения"""
# <
# >
# = или <>
# !=
# <=
# >=


"""Арифметические операции"""
# +
# -
# /
# *
# %
# //


# select 2 + 3 #5 -> правильно
# 2 + 3  ->неправильно

# select * from person where name = 'John'  ->достать элементы где имя John

 
"""ЦИКЛ РАБОТЫ С БД"""
# psql  /  sudo -U postgres psql


"Вариант 1"
# create user name_of_user;
# create database name_of_db with owner name_of_user;
# alter role name_of_user with password '1';
# alter role name_of_user with superuser;


"Вариант 2"
# create user name_of_user with password '1';
# create database name_of_db;
# alter role name_of_user with superuser;



# psql -U name_of_user -d name_of_db  -> войти как юзер в бд



# constraint constraint_name unique (column)

# alter table email add constraint fk_email_users foreign key(use_id) references users(id);  ->привязка к другой таблице и ограничение

# create table name_table(
# product_id int not null,
# order_id int not null,
# CONSTRAINT fk_order_product_product FOREIGN KEY(product_id) REFERENCES product(id),
# CONSTRAINT fk_order_product_order FOREIGN KEY(order_id) REFERENCES name_table(id));



"""     <<<JOIN>>>      """

'''
3 вида связей:
1. Один к одному
2. Один к многим
3. Много к многим
'''
# select users.id, users.name, users.last_name, email.email from users inner join email on users.id=email.user_id;   -->связываем две таблицы

# ДОПУСТИМО импользовать AS чтобы укоротить название таблицы:

# SELECT u.id, u.name, u.last_name, e.email FROM users AS u INNER JOIN email AS e ON u.id=e.user_id;


# SELECT u.id, u.name, u.last_name, e.email FROM users AS u LEFT OUTER JOIN email AS e ON u.id=e.user_id;  ->сперва вытаскивает инфу с левой таблицы(т.е. раньше прописана в строчке коде выша)


# SELECT u.id, u.name, u.last_name, e.email FROM users AS u RIGHT OUTER JOIN email AS e ON u.id=e.user_id;   -->сперва вытаскивает инфу с правой таблицы


# SELECT u.id, u.name, u.last_name, e.email FROM users AS u FULL OUTER JOIN email AS e ON u.id=e.user_id;   -->вытаскивает всю инфу


# SELECT u.name, u.last_name, e.email, o.addres FROM users AS u INNER JOIN email AS e ON u.id=e.user_id INNER JOIN orders AS o ON o.user_id=u.id;       -->соединяет 3 таблицы


# SELECT u.name, u.last_name, e.email, o.addres FROM users AS u FULL OUTER JOIN email AS e ON u.id=e.user_id FULL OUTER JOIN orders AS o ON o.user_id=u.id;       -->соединяет 3 таблицы и выодит всю инфу


"""         <<<CASE>>>          """
# if else in PostgreSQL

# SELECT title, price CASE WHEN price > 40000 THEN 'too much' ELSE 'ok' END FROM product;           -->Условие если цена больше 40000 говорит "много"


# SELECT title, price, quantity, CASE WHEN quantity = 0 THEN 'out of stock' WHEN quantity BETWEEN 1 AND 10 THEN 'hurry up!!!' ELSE 'in stock' END FROM product;


