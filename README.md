# api_final

## ===============================
### Описание.

Эта программа - **API** для сервиса *Yatube*. При помощи этого **API** можно делать запросы к *Yatube* из сторонних приложений.

### Установка.

#### Клонировать репозиторий и перейти в него в командной строке:
```
 git clone https://github.com/AlexandrSharganov/api_final_yatube.git
 ```

#### Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```

#### Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Выполнить миграции:
```
python3 manage.py migrate
```

#### Запустить проект:
```
python3 manage.py runserver
```

### Примеры. Некоторые примеры запросов к API.

#### Получить список всех публикаций.
```
GET http://127.0.0.1:8000/api/v1/posts/
```

#### Получить одну публикацию.
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

#### Создать публикацию.
```
POST http://127.0.0.1:8000/api/v1/posts/
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

### Работу выполнил
- [Александр Шарганов](https://github.com/AlexandrSharganov)
