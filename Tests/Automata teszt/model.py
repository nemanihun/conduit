import time

import configuration as config
import data as adatok
import test_conduit
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Testcase:

    def __init__(self, test_name, expected_result, actual_result):
        self.test_name = test_name
        self.expected_result = expected_result
        self.actual_result = actual_result

    def teszt_nev(self):
        test_name = self.test_name
        print(test_name)

    def teszt_start(self):
        test_name = self.test_name

        # Teszteset elindul
        print()
        print(f'{test_name} teszteset elindult')
        print()

    def expected_res(self, asserts):
        # Teszteset eredmény vizsgálata
        print()
        print('Teszt eset eredményének vizsgálata')
        print()

        print(f'Elvárt eredmény: {self.expected_result}')
        print()

        assert asserts

    def actual_res(self):
        print(f'{self.test_name} teszteset sikeres')
        print()

        print(f'Aktuális eredmény:  {self.actual_result}')
        print()

        print(f'{self.test_name} teszteset sikeresen lezárult')
        print()


class GetUsers:

    def __init__(self):
        self.user_data = []

    def userdata(self, us):

        users = ''

        if us == 'user1':
            users = adatok.Users.user_data.values()
        if us == 'user2':
            users = adatok.Users.user2_data.values()
        if us == 'bademail':
            users = adatok.Users.bad_user_email.values()
        if us == 'badpass':
            users = adatok.Users.bad_user_password.values()
        if us == 'user4':
            users = adatok.Users.user4_data.values()

        for user in users:
            self.user_data.append(user)

    # Regisztráció
    def signup(self, browser, us):

        # browser.get(adatok.Urls.home_url)
        self.userdata(us)

        signup_link = browser.find_element(By.LINK_TEXT, 'Sign up')
        signup_link.click()

        print('Regisztrációs adatok megadása')

        user_name = browser.find_elements(By.XPATH, '//input')[0]
        user_name.send_keys(self.user_data[0])

        email = browser.find_elements(By.XPATH, '//input')[1]
        email.send_keys(self.user_data[1])

        password = browser.find_elements(By.XPATH, '//input')[2]
        password.send_keys(self.user_data[2])

        print(
            f'Bejelentkezési adatok: Felhasználó név: {self.user_data[0]}, Email cím: {self.user_data[1]}, Jelszó: {self.user_data[2]}')

        submit_btn = browser.find_element(By.XPATH, '//button')
        submit_btn.click()

        # Registration Success Popup Ok button

        ok_btn = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'swal-button--confirm')))

        ok_btn.click()

    # Bejelentkezés
    def signin(self, browser, us):

        self.userdata(us)

        signin_link = browser.find_element(By.LINK_TEXT, 'Sign in')
        signin_link.click()

        print('Bejelentkezési adatok megadása')

        email = browser.find_elements(By.XPATH, '//input')[0]
        email.send_keys(self.user_data[1])

        password = browser.find_elements(By.XPATH, '//input')[1]
        password.send_keys(self.user_data[2])

        print(f'Bejelentkezési adatok: Email cím: {self.user_data[1]}, Jelszó: {self.user_data[2]}')

        submit_btn = browser.find_element(By.XPATH, '//button')
        submit_btn.click()

    # Kijelentkezés
    def logout(self, browser):

        logout_btn = browser.find_element(By.CLASS_NAME, 'ion-android-exit')
        logout_btn.click()

    # A "Sign in" gomb megtalálása
    def signin_btn(self, browser):

        return browser.find_element(By.LINK_TEXT, 'Sign in')

    # A "Log out" gomb megtalálása
    def logout_btn(self, browser):

        return WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'ion-android-exit')))

    def signup_ok_btn(self, browser):

        return WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'swal-button--confirm')))


class Cookie:
    # Adatkezelési nyilatkozat használata
    def cookie_handling(self, browser):
        print('Test step 1')
        print()
        print('Megvizsgálom, megjelenik-e a cookie használatról tájékoztató')

        cookie_content = browser.find_element(By.CLASS_NAME, 'cookie__bar__content')

        print()
        print('Elvárt eredmény: Megjelenik az oldalon cookie használatról tájékoztató.')

        assert cookie_content.is_displayed()

        print()
        print(f'Aktuális eredmény: "Cookie bar" látszik ezzel a tartalommal: \n {cookie_content.text}')

        print()
        print('Test step 2')
        print()
        print('Megvizsgálom, megjelenik-e a "cookie bar"-on a cookiek elfogadását szolgáló gomb')

        cookie_accept_btn = browser.find_element(By.CLASS_NAME, 'cookie__bar__buttons__button--accept')

        print()
        print('Elvárt eredmény: Megjelenik a "cookie bar"-on a cookiek elfogadását szolgáló gomb.')

        assert cookie_accept_btn.is_displayed()

        print()
        print(
            f'Aktuális eredmény: Megjelenik a "cookie bar"-on a cookiek elfogadását szolgáló gomb ezzel a felirattal: {cookie_accept_btn.text}')

        print()
        print('Test step 3')
        print()
        print('Megvizsgálom, megjelenik-e a "cookie bar"-on a cookiek visszautasítását szolgáló gomb')

        cookie_decline_btn = browser.find_element(By.CLASS_NAME, 'cookie__bar__buttons__button--decline')

        print()
        print('Elvárt eredmény: Megjelenik a "cookie bar"-on a cookiek visszautasítását szolgáló gomb.')

        assert cookie_decline_btn.is_displayed()

        print()
        print(
            f'Aktuális eredmény: Megjelenik a "cookie bar"-on a cookiek visszautasítását szolgáló gomb ezzel a felirattal: {cookie_decline_btn.text}')

        print()
        print('Test step 4')
        print()
        print(f'Megvizsgálom, a {cookie_accept_btn.text} feliratú gombra kattintva mi történik')

        print()
        print('Elvárt eredmény: A gombra kattintás után eltűnik a "cookie_bar".')

        print()
        print(f'Rákattintok, a {cookie_accept_btn.text} feliratú gombra')

        cookie_accept_btn.click()

        WebDriverWait(browser, 5).until_not(EC.presence_of_element_located((By.CLASS_NAME, 'cookie__bar__content')))

        cookie_content_list = browser.find_elements(By.CLASS_NAME, 'cookie__bar__content')

        cookie_bar_displayed = len(cookie_content_list)

        assert cookie_bar_displayed == 0

        print()
        print(f'Aktuális eredmény: Eltűnt a "cookie_bar".')
