import data as adatok
import configuration as config
import model as model
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from datetime import datetime, date, time, timezone
from selenium.webdriver.support.ui import Select


class TestConduit(object):

    def setup_method(self):
        self.browser = config.get_preconfigured_chrome_driver()
        self.browser.get(adatok.Urls.home_url)
        time.sleep(5)

    def teardown_method(self):
        self.browser.quit()

    # TestCase 01 - Regisztráció
    def test_signup(self):
        getusers = model.GetUsers()

        required_data = {
            'test_name': 'TestCase 01 - Regisztráció',
            'expected_result': 'Sikeres regisztráció után látszik az "Ok" gomb',
            'actual_result': 'A regisztráció sikeres, látszik az "Ok" gomb',

        }

        testcase1 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],
        )

        testcase1.teszt_nev()
        testcase1.teszt_start()

        getusers.signup(self.browser, 'user4')
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ion-android-exit')))

        getusers.logout_btn(self.browser).is_displayed()
        testcase1.expected_res(getusers.signup_ok_btn(self.browser).is_displayed())
        testcase1.actual_res()

    # TestCase 02 - Bejelentkezés
    def test_signin(self):
        getusers = model.GetUsers()

        required_data = {
            'test_name': 'TestCase 02 - Bejelentkezés',
            'expected_result': 'Sikeres bejelentkezés után látszik a "Log out" gomb',
            'actual_result': 'Sikeres bejelentkezés, látszik a "Log out" gomb',

        }

        testcase2 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],

        )

        testcase2.teszt_nev()
        testcase2.teszt_start()

        getusers.signin(self.browser, 'user2')

        WebDriverWait(self.browser, 5).until((EC.url_to_be(adatok.Urls.home_url)))

        testcase2.expected_res(getusers.logout_btn(self.browser).is_displayed())

        testcase2.actual_res()

    # TestCase 03 - Kijelentkezés
    def test_logout(self):
        getusers = model.GetUsers()

        required_data = {
            'test_name': 'TestCase 03 - Kijelentkezés',
            'expected_result': 'Sikeres kijelentkezés után látszik a "Sign in" gomb',
            'actual_result': 'Sikeres kijelentkezés, látszik a "Sign in" gomb',

        }

        testcase3 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],

        )

        testcase3.teszt_nev()
        testcase3.teszt_start()

        getusers.signin(self.browser, 'user2')

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ion-android-exit')))

        getusers.logout(self.browser)

        time.sleep(5)

        testcase3.expected_res(getusers.signin_btn(self.browser).is_displayed())
        testcase3.actual_res()

    # TestCase 04 - Adatkezelési nyilatkozat használata
    def test_cookie_handling(self):
        cookie = model.Cookie()

        required_data = {
            'test_name': 'TestCase 04 - Adatkezelési nyilatkozat használata',
            'expected_result': '',
            'actual_result': '',

        }

        testcase4 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],

        )

        testcase4.teszt_nev()
        testcase4.teszt_start()

        cookie.cookie_handling(self.browser)
