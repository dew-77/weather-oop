from pydantic import BaseModel
from typing import List


class MainInfo(BaseModel):
    temp: float
    pressure: int


class WindInfo(BaseModel):
    speed: float


class WeatherInfo(BaseModel):
    main: MainInfo
    wind: WindInfo


class WeatherResponse(BaseModel):
    list: List[WeatherInfo]
