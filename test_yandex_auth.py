from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest

def yandex_source_after_login(login=None, password=None):
    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth/')
    elem = driver.find_element_by_id('passp-field-login')
    elem.send_keys(login)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    if password is not None:
        elem = driver.find_element_by_id('passp-field-passwd')
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
    source = driver.page_source
    driver.close()
    return source

class TestYandexAuth:

    def test_yandex_auth(self, yandex_login, yandex_password):
        """правильный логин и пароль"""
        page_source = yandex_source_after_login(login=yandex_login, password=yandex_password)
        assert "Введите пароль" not in page_source

    def test_yandex_auth_wrong_pswd(self, yandex_login):
        """правильный логин и неправильный пароль"""
        page_source = yandex_source_after_login(login=yandex_login, password='!@#$%^&*()_+')
        assert "Введите пароль" in page_source

    def test_yandex_auth_empty_pswd(self, yandex_login):
        """правильный логин и пустой пароль"""
        page_source = yandex_source_after_login(login=yandex_login, password='')
        assert "Введите пароль" in page_source

    def test_yandex_auth_wrong_login(self):
        page_source = yandex_source_after_login(login='!@#$%^&*()_+')
        assert "Такой логин не&nbsp;подойдет" in page_source
