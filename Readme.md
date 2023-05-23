## Проект включает в себя разработку REST API, которое будет обслуживать мобильное приложение.

---
### В проекте используются <font color="MediumPurple">модели:</font>
#### <font color="DarkTurquoise">Users</font> — Модель пользователей, содержит информацию о пользователе: email, пароль, имя, фамилию, отчество.
#### <font color="DarkTurquoise">PerevalAdded</font> — Модель перевалов, содержит информацию о перевалах: название, красивое название, координаты, уровень сложности в каждый сезон, изображения, статус, дата добавления, идентификатор пользователя, который добавил перевал.
#### <font color="DarkTurquoise">Coords</font> — Модель координат, содержит информацию о координатах перевалов: широту, долготу и высоту.
#### <font color="DarkTurquoise">PerevalImages</font> — Модель изображений перевалов, содержит информацию об изображении и его названии.
#### <font color="DarkTurquoise">PerevalAreas</font> — Модель областей перевалов, содержит информацию об идентификаторе родительской области и её названии.

---
## В процессе разработки проекта были реализованы методы REST API:
#### <font color="DarkTurquoise">POST /submitData/</font> — Запрос на создание записи (перевала).
#### <font color="DarkTurquoise">GET /submitData/<id></font> — Запрос на получение информации запись (перевал) по её ID. Выводит всю информацию об объекте.
#### <font color="DarkTurquoise">PATCH /submitData/<id></font> — Отредактировать существующую запись (замена), если она в статусе "new".
#### <font color="DarkTurquoise">GET /submitData/?user__email=<email></font> — список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.
## В качестве базы данных используется PostgreSQL.

---
### <font color="MediumPurple">Установка:</font>
    * Клонируйте репозиторий.
    * Создайте виртуальное окружение и активируйте его.
    * Установите зависимости из файла requirements.txt: pip install -r requirements.txt.
    * Создайте базу данных: python manage.py migrate.
    * Запустите сервер: python manage.py runserver.
### <font color="MediumPurple">Использование:</font>
    * SubmitData/list/ - список всех перевалов.
    * SubmitData/create/ - создание нового перевала.
    * SubmitData/<int:pk>/ - информация о перевале по идентификатору.
    * SubmitData/<int:pk>/update/ - обновление информации о перевале.
