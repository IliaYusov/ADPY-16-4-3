from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest

class TestYandexAuth:

    def test_yandex_auth(yandex_login, yandex_password):
        """правильный логин и пароль"""
        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element_by_id('passp-field-login')
        elem.send_keys(yandex_login)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id('passp-field-passwd')
        elem.send_keys(yandex_password)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Введите пароль" not in driver.page_source

    def test_yandex_auth_wrong_pswd(yandex_login, yandex_password):
        """правильный логин и неправильный пароль"""
        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element_by_id('passp-field-login')
        elem.send_keys(yandex_login)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id('passp-field-passwd')
        elem.send_keys('!@#$%^&*()_+')
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Введите пароль" in driver.page_source

    def test_yandex_auth_empty_pswd(yandex_login, yandex_password):
        """правильный логин и пустой пароль"""
        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element_by_id('passp-field-login')
        elem.send_keys(yandex_login)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id('passp-field-passwd')
        elem.send_keys('')
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Введите пароль" in driver.page_source

    def test_yandex_auth_wrong_login(yandex_login, yandex_password):
        """неправильный логин"""
        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element_by_id('passp-field-login')
        elem.send_keys('!@#$%^&*()_+')
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Введите логин" in driver.page_source