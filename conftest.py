import pytest
import os
from dotenv import load_dotenv

@pytest.fixture
def yandex_login():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    return os.environ.get('YANDEX_LOGIN')

@pytest.fixture
def yandex_password():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    return os.environ.get('YANDEX_PASSWORD')
