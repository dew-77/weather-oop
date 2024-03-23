from datetime import datetime as dt

import httpx
from pydantic import ValidationError

from constants import settings
from exceptions import (
    IncorrectCityNameException, ServiceAvailabilityException,
    IncorrectJsonFormatException
)
from models import WeatherResponse


class Weather:
    """
    Класс для обращений к внешним сервисам погоды.
    Получает название города и единицу температуры при инициализации.
    """

    def __init__(self, city: str, need_unit: str) -> None:
        self.city = city
        self.need_unit = need_unit

    def __get_json(self) -> httpx._models.Response.json:
        """
        Получение и валидация данных в формате JSON
        """

        # Формирование URL на основе параметров
        unit = settings.units[self.need_unit][0]
        params = {
            'q': self.city, 'type': 'like',
            'APPID': settings.api_key, 'units': {unit}
        }

        # Запрос через httpx
        try:
            response = httpx.get(url=settings.api_url, params=params)
            response.raise_for_status()
        except httpx._exceptions.HTTPStatusError:
            raise ServiceAvailabilityException('Service currently unavailable')

        return response.json()

    def get_weather_info(self) -> str:
        json = self.__get_json()

        try:
            weather_response = WeatherResponse.parse_obj(json)
        except ValidationError:
            raise IncorrectJsonFormatException('Incorrect JSON response')

        # Извлечение информации из json
        try:
            temperature = str(weather_response.list[0].main.temp) + \
                settings.units[self.need_unit][1]
            pressure = str(weather_response.list[0].main.pressure) + \
                'hPa'
            wind = str(weather_response.list[0].wind.speed) + \
                'м/с'
        except IndexError:
            raise IncorrectCityNameException('Incorrect city name')

        # Формирование ответа
        weather_info = f'{temperature}-{pressure}-{wind}'
        return weather_info


class File:
    """
    Класс для обращений к внешним сервисам погоды.
    Получает название файла и данные для записи.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def record_to_file(self, data: str) -> None:
        with open(self.name, 'a') as f:
            f.write(f'{dt.now():%d-%m-%Y %H:%M:%S} {data} \n')


class UserInterface:
    """
    Интерфейс для пользователя.
    """

    def __init__(self, city: str, unit: str = 'Celsius') -> None:
        self.weather = Weather(city=city, need_unit=unit)
        self.file = File(name=settings.file_to_write)

    def get_weather(self) -> None:
        try:
            data = f'{self.weather.city} {self.weather.get_weather_info()}'
            print(
                f"{self.weather.city} "
                f"{dt.now():%d-%m-%Y %H:%M:%S} "
                f"{self.weather.get_weather_info()}"
            )

        except (
            IncorrectCityNameException, ServiceAvailabilityException,
            IncorrectJsonFormatException
        ) as error:
            print(error)
            data = error

        self.file.record_to_file(data=data)


if __name__ == '__main__':
    city = input('Type city name: ')
    interface = UserInterface(city)
    interface.get_weather()
