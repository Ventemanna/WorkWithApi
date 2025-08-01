# Работа с Django Rest Framework

Проект представялет из себя backend версию магазина бытовой техники, работающего с API. 

Проект будет доступен по адресу: http://localhost:8000

Swagger-документация (если есть): http://localhost:8000/swagger/

## Функциональность

- Регистрация и аутентификация пользователей
- CRUD для моделей
- Пагинация
- Документация через Swagger

## Доступные запросы

Реализованы базовые HTTP-запросов (GET, POST, PUT, DELETE, PATCH).

Для клиентов:

- Добавление клиента (на вход подается json, соответствующей структуре, описанной сверху)
- Удаление клиента (по его идентификатору)
- Получение клиентов по имени и фамилии (параметры — имя и фамилия)
- Получение всех клиентов 
- Изменение адреса клиента

Для товаров:

- Добавление товара (на вход подается json, соответствующей структуре, описанной сверху).
- Уменьшение количества товара (на вход запросу подается id товара и на сколько уменьшить).
- Получение товара по id.
- Получение всех доступных товаров.
- Удаление товара по id.

Для поставщиков:

- Добавление поставщика.
- Изменение адреса поставщика.
- Удаление поставщика по id
- Получение всех поставщиков
- Получение поставщика по id

Для изображений:

- Добавление изображения (на вход подается byte array изображения и id товара).
- Изменение изображения (на вход подается id изображения и новая строка для замены).
- Удаление изображения по id изображения.
- Получение изображения конкретного товара (по id товара).
- Получение изображения по id изображения.

## Стек технологий

- Python 3.12
- Django 5.2
- Django REST Framework
- PostgreSQL
- drf-yasg

## Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone git@github.com:Ventemanna/WorkWithApi.git
cd WorkWithApi
```

### 2. Запуск контейнера

```bash
docker compose build
docker compose up
```
