from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_descriptian: str = 'Сервис для бронирования переговорных комнат.'

    class Config:
        env_file = '.env'


settings = Settings()
