from datetime import datetime as dt

import httpx

from constants import API_KEY, API_URL, FILE_TO_WRITE, UNITS


class Weather:
    """
    Класс для обращений к внешним сервисам погоды.
    Получает название города и единицу температуры при инициализации.
    """

    def __init__(self, city: str, need_unit: str):
        self.city = city
        self.need_unit = need_unit

    def __get_json(self):
        # Формирование URL на основе параметров
        unit = UNITS[self.need_unit][0]
        url = API_URL + \
            f'?q={self.city}&type=like&APPID={API_KEY}&units={unit}'

        # Запрос через httpx
        response = httpx.get(url=url)
        if response.status_code != 200:
            raise TimeoutError('Service currently unavailable.')

        return response.json()

    def get_weather_info(self) -> str:
        # Извлечение информации из json'а
        json = self.__get_json()

        try:
            temperature = str(json.get('list')[0].get('main').get('temp')) + \
                UNITS[self.need_unit][1]
            pressure = str(json.get('list')[0].get('main').get('pressure')) + \
                'hPa'
            wind = str(json.get('list')[0].get('wind').get('speed')) + \
                'м/с'
        except IndexError:
            raise IndexError('Incorrect city name.')

        # Формирование ответа
        weather_info = f'{temperature}-{pressure}-{wind}'
        return f'{self.city}_{dt.now():%d-%m-%Y %H:%M:%S}_{weather_info}'


class File:
    """
    Класс для обращений к внешним сервисам погоды.
    Получает название файла и данные для записи.
    """

    def __init__(self, name: str, data: str):
        self.name = name
        self.data = data

    def record_to_file(self) -> None:
        with open(self.name, 'a') as f:
            f.write(self.data + '\n')


class UserInterface:
    """
    Интерфейс для пользователя.
    """

    def __init__(self, unit: str = 'Celsius'):
        self.unit = unit

    def __get_city(self):
        city = input('Type city name: ')
        return city

    def get_weather(self) -> None:
        # Обращение к классам Weather и File + обработка исключений
        try:
            data = Weather(
                city=self.__get_city(), need_unit=self.unit
            ).get_weather_info()
            print(data)

        except Exception as error:
            print(error)
            data = f'[error] {dt.now():%d-%m-%Y %H:%M:%S}: {error}'

        File(name=FILE_TO_WRITE, data=data).record_to_file()


if __name__ == '__main__':
    interface = UserInterface()
    interface.get_weather()
