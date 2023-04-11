import data as adatok
import configuration as config
import model as model
import asserts as asserting
import time

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
        self.browser.maximize_window()
        time.sleep(10)

    def teardown_method(self):
        self.browser.quit()

    # ATC 01 - Regisztráció
    def test_signup(self):
        getusers = model.GetUsers()

        required_data = {
            'test_name': 'ATC 01 - Regisztráció',
            'expected_result': 'Sikeres regisztráció után látszik az "Ok" gomb',
            'actual_result': 'A regisztráció sikeres, látszik az "Ok" gomb',
        }

        testcase1 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],
        )

        testcase1.teszt_nev()

        getusers.signup(self.browser, 'user1')

        asserts = asserting.Asserts()

        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ion-android-exit')))

        getusers.logout_btn(self.browser).is_displayed()

        testcase1.expected_res()

        asserts.general_asserts(getusers.signup_ok_btn(self.browser).is_displayed())

        testcase1.actual_res()

    # ATC 02 - Bejelentkezés
    def test_signin(self):
        getusers = model.GetUsers()

        required_data = {
            'test_name': 'ATC 02 - Bejelentkezés',
            'expected_result': 'Sikeres bejelentkezés után látszik a "Log out" gomb',
            'actual_result': 'Sikeres bejelentkezés, látszik a "Log out" gomb',
        }

        testcase2 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],
        )

        testcase2.teszt_nev()

        getusers.signin(self.browser, 'user1')

        asserts = asserting.Asserts()

        WebDriverWait(self.browser, 5).until((EC.url_to_be(adatok.Urls.home_url)))

        testcase2.expected_res()

        asserts.general_asserts(getusers.logout_btn(self.browser).is_displayed())

        testcase2.actual_res()

    # ATC 03 - Kijelentkezés
    def test_logout(self):
        getusers = model.GetUsers()

        required_data = {
            'test_name': 'ATC 03 - Kijelentkezés',
            'expected_result': 'Sikeres kijelentkezés után látszik a "Sign in" gomb',
            'actual_result': 'Sikeres kijelentkezés, látszik a "Sign in" gomb',
        }

        testcase3 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],
        )

        testcase3.teszt_nev()

        getusers.signin(self.browser, 'user1')

        asserts = asserting.Asserts()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ion-android-exit')))

        getusers.logout(self.browser)

        time.sleep(5)

        testcase3.expected_res()

        asserts.general_asserts(getusers.signin_btn(self.browser).is_displayed())

        testcase3.actual_res()

    # ATC 04 - Adatkezelési nyilatkozat használata
    def test_cookie_handling(self):
        cookie = model.Cookie()

        required_data = {
            'test_name': 'ATC 04 - Adatkezelési nyilatkozat használata',
            'expected_result': '',
            'actual_result': '',
        }

        testcase4 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],
        )

        testcase4.teszt_nev()

        cookie.cookie_handling(self.browser)

    # ATC 05 - Adatok listázása
    def test_data_listing(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        asserts = asserting.Asserts()

        required_data = {
            'test_name': 'ATC 05 - Adatok listázása',
            'expected_result': 'Legalább egy cikk van az oldalon',
            'actual_result': 'Található cikk az oldalon',
        }

        testcase5 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],
        )

        testcase5.teszt_nev()

        getusers.signin(self.browser, 'user1')

        WebDriverWait(self.browser, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'counter')))

        testcase5.expected_res()

        asserts.article_listing_assert(self.browser)

        manipulatepages.article_listing(self.browser)

        testcase5.actual_res()

        # ATC 06 - Több oldalas lista bejárása

    def test_multi_page_listing(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        asserts = asserting.Asserts()

        required_data = {
            'test_name': 'ATC 06 - Több oldalas lista bejárása',
            'expected_result': 'Ki listázom az összes oldalon található cikk címét és elérek a lista oldalak végére, ezzel bejárva az összes lista oldalt.',
            'actual_result': 'Elérek a lista oldalak végére, bejártam a lista oldalát, ki tudtam listázni az összes cikk címét a lista oldalakról.',
        }

        testcase6 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],
        )

        testcase6.teszt_nev()

        getusers.signin(self.browser, 'user1')

        WebDriverWait(self.browser, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'counter')))

        time.sleep(5)

        manipulatepages.multi_page_list_explore(self.browser)

        testcase6.expected_res()

        asserts.multi_page_listing_assert(self.browser)

        # ATC 07 - Új adat bevitel / Új cikk feltöltése

    def test_new_data_upload(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        asserts = asserting.Asserts()

        required_data = {
            'test_name': 'ATC 07 - Új adat bevitele',
            'expected_result': 'Az új cikk feltöltése sikeres. A cikk címe megjelenik az oldalon.',
            'actual_result': 'Megjelenik a cikk címe. A cikk felvitele sikeres volt.',
            'article': 'article1_data'
        }

        article = required_data['article']

        testcase7 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],
        )

        testcase7.teszt_nev()

        getusers.signin(self.browser, 'user1')

        WebDriverWait(self.browser, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'counter')))

        manipulatepages.new_article_upload(self.browser, article)

        testcase7.expected_res()

        asserts.article_assert(self.browser, article)

        testcase7.actual_res()

        # ATC 08 - Adat módosítása / Cikk módosítása

    def test_modify_data(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        asserts = asserting.Asserts()

        required_data = {
            'test_name': 'ATC 08 - Adat módosítása/Cikk módosítása',
            'expected_result': 'A cikk módosítása sikeres. A cikk címe megjelenik az oldalon.',
            'actual_result': 'Megjelenik a módosított cikk címe. A cikk módosítása sikeres volt.',
            'article': 'article1_data'
        }

        article = required_data['article']

        testcase8 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],
        )

        testcase8.teszt_nev()

        getusers.signin(self.browser, 'user1')

        WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'counter')))

        manipulatepages.modify_article(self.browser, article)

        testcase8.expected_res()

        asserts.article_assert(self.browser, 'article2_data')

        testcase8.actual_res()

        # ATC 09 - Adat törlése / Cikk törlése

    def test_delete_data(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        asserts = asserting.Asserts()

        required_data = {
            'test_name': 'ATC 09 - Adat törlése/Cikk törlése',
            'expected_result': 'A cikk törlése sikeres. A cikk nem jelenik már meg az oldalon.',
            'actual_result': 'A cikk törlése sikeres. A cikk már nem jelenik meg az oldalon.',
            'article': 'article2_data'
        }

        article = required_data['article']

        testcase9 = model.Testcase(
            test_name=required_data['test_name'],
            expected_result=required_data['expected_result'],
            actual_result=required_data['actual_result'],
        )

        testcase9.teszt_nev()

        getusers.signin(self.browser, 'user1')

        WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'counter')))

        manipulatepages.delete_article(self.browser, article)

        testcase9.expected_res()

        asserts.delete_article_assert(self.browser, article)

        testcase9.actual_res()
