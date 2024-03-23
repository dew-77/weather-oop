# weather-oop

Программа для получения текущей погоды, созданная с применением принципов ООП. 

- Принимает на вход название города и выводит строку вида
`{Название_Города}_{дата и время}_{погода}`, где погода - это температура, давление и скорость ветра.

- Результаты и ошибки дублируются в текстовый файл.

- Опциональный выбор единиц температуры

Пример записей в файле:

```bash
23-03-2024 14:54:33 Moscow 277.46°C-1000hPa-5.99м/с
23-03-2024 14:54:25 Incorrect city name 
23-03-2024 14:54:25 Service currently unavailable
```

## Технологии

- Python 3.11
- Библиотеки httpx, datetime
- pydantic

В качестве внешнего сервиса погоды рекомендуется использовать API [openweathermap.org](https://openweathermap.org/current).

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
4. Создать файл `.env` и заполнить его по примеру в `.env.example`:
5. Запустить программу:
```bash
# Для Linux
python3 weather.py
# Для Windows
python weather.py
```