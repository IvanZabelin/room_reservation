from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_descriptian: str = 'Сервис для бронирования переговорных комнат.'
    database_url: str
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    email: Optional[str] = None
    google_application_credentials: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
