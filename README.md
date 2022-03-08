# Rest api сервис для работы с базой данных

Это приложение может добавить запись в базу данных(mongoDB) и вывести его потом по номеру записи.
Для работы необходимо запустить docker-compose (команда для запуска: docker-compose up ), а после уже работоспособность БД добавив запись:
Добавление записи методом POST: /pdr

`curl -i -X POST -H "Content-type:application/json" -d "{ /"id/" : /"i/", /"name/" : /"x/"}" localhost/pdr`

Где: "i" - это любой выбранный номер 
     "x" - это любая запись 

Просмотр добавленной записи localhost/one/"i", где "i" номер выбранный ранее  
