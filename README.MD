REST API для управления коллекцией книг.

## Стек
- Python 3.10+
- FastAPI
- Uvicorn

## Установка
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск
```bash
uvicorn main:app --reload
```

## Документация

После запуска: http://127.0.0.1:8000/docs

## Эндпоинты

| Метод | Адрес | Описание |
|-------|-------|----------|
| GET | /books | Все книги |
| GET | /books/{id} | Книга по ID |
| POST | /books | Добавить книгу |