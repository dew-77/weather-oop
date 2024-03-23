from pydantic_settings import BaseSettings
from typing import Dict, List


class Settings(BaseSettings):
    api_url: str
    api_key: str
    file_to_write: str
    units: Dict[str, List[str]] = {
        'Fahrenheit': ['imperial', '°F'],
        'Celsius': ['metric', '°C'],
        'Kelvin': ['standard', '°K'],
    }

    class Config:
        env_prefix = ''


settings = Settings()
