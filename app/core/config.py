import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('ENV', 'development'))

class Settings(BaseSettings):
    ENV: str = os.getenv('ENV', 'development')
    DATABASE_URL: str = os.getenv('DATABASE_URL')

settings = Settings()
