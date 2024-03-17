# weather-oop

Программа для получения текущей погоды, созданная с применением принципов ООП. 

- Принимает на вход название города и выводит строку вида
`{Название_Города}_{дата и время}_{погода}`, где погода - это температура, давление и скорость ветра.

- Результаты и ошибки дублируются в текстовый файл.

- Опциональный выбор единиц температуры

Пример записей в файле:

```plain
Москва_17-03-2024 23:35:57_2.38°C-1016hPa-1.98м/с
Анкара_17-03-2024 23:36:03_7.89°C-1015hPa-1.28м/с
[error] 17-03-2024 23:36:09: Incorrect city name.
```

## Технологии

- Python 3.11
- Библиотеки httpx, datetime

В качестве внешнего сервиса погоды используется API [openweathermap.org](https://openweathermap.org/current).

## Установка и запуск

1. Создать виртуальное окружение:
```bash
# Для Linux
python3 -m venv venv
# Для Windows
python -m venv venv
```
2. Активировать созданное окружение:
```bash
# Для Linux
. venv/bin/activate
# Для Windows
. venv/Scripts/activate
```
3. Установить зависимости:
```bash
pip install -r requirements.txt
```
4. Ввести свой токен OWM в поле API_KEY:
```python
API_KEY = 'key_example_123'
```
5. Запустить программу:
```bash
# Для Linux
python3 weather.py
# Для Windows
python weather.py
```