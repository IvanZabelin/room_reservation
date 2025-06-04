import json
import os
from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import ServiceAccountCreds



SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]


credentials_path = "D:\\Dev\\room_reservation\\privat-key.json"
if not credentials_path or not os.path.exists(credentials_path):
    raise ValueError("Google application credentials path is not set or does not exist.")

# Загружаем учетные данные из JSON-файла
with open(credentials_path, 'r') as f:
    credentials_data = json.load(f)

# Получаем объект учетных данных
cred = ServiceAccountCreds(scopes=SCOPES, **credentials_data)

# Создаем экземпляр класса Aiogoogle
async def get_service():
    async with Aiogoogle(service_account_creds=cred) as aiogoogle:
        yield aiogoogle
