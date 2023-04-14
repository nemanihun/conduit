import time
import csv

import data as adatok
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GetUsers:
    # Funkciók, amelyek regisztrációval, belépéssel kapcsolatosak.
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
        if us == 'user5':
            users = adatok.Users.user5_data.values()

        for user in users:
            self.user_data.append(user)

    # Regisztráció
    def signup(self, browser, user):

        self.userdata(user)

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

        logout_button = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ion-android-exit')))

        if logout_button.is_displayed():

            # Registration Success Popup Ok button

            ok_btn = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'swal-button--confirm')))

            ok_btn.click()
        else:
            print('A regisztráció sikerült, de nem jelentkezett be az alkalmazás a folyamat végén.')

    # Bejelentkezés
    def signin(self, browser, user):

        self.userdata(user)

        signin_link = browser.find_element(By.LINK_TEXT, 'Sign in')
        signin_link.click()

        email = browser.find_elements(By.XPATH, '//input')[0]
        email.send_keys(self.user_data[1])

        password = browser.find_elements(By.XPATH, '//input')[1]
        password.send_keys(self.user_data[2])

        print()
        print('Bejelentkezem az alkalmazásba')
        print()
        print(f'Megadom a bejelentkezési adatokat: Email cím: {self.user_data[1]}, Jelszó: {self.user_data[2]}')

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


class ManipulatePages:
    # Funkciók, amelyek az oldalak tartalmát dolgozzák fel, módosítják vagy ezekhez szükségesek.
    def __init__(self):
        self.article_amount = 0
        self.article_list = []
        self.article_data = []
        self.article_title_list = []

    # Általános funkciók

    # Cikk adatok elérése a data.py-ból
    def articledata(self, adata):

        articles = ''

        if adata == 'article1_data':
            articles = adatok.Articles.article1_data.values()
        if adata == 'article2_data':
            articles = adatok.Articles.article2_data.values()
        if adata == 'article3_data':
            articles = adatok.Articles.article3_data.values()
        if adata == 'hirek_csv':
            articles = self.article_data
        for article in articles:
            self.article_data.append(article)
        return articles

    # Cikk adatok megadása
    def article_input(self, browser):
        print('Cikk adatok megadása')

        input_fields = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//input')))

        article_title = input_fields[0]
        article_title.clear()
        article_title.send_keys(self.article_data[0])

        article_about = input_fields[1]
        article_about.clear()
        article_about.send_keys(self.article_data[1])

        article_content = browser.find_element(By.XPATH, '//textarea')
        article_content.clear()
        article_content.send_keys(self.article_data[2])

        article_tag = input_fields[2]
        article_tag.clear()
        article_tag.send_keys(self.article_data[3])

        print(
            f'Cikk adatai: Cikk címe: {self.article_data[0]}, Cikk témája: {self.article_data[1]}, Cikk szövege: {self.article_data[2]}, Cikk címkéi {self.article_data[2]}')

        publish_btn = browser.find_element(By.XPATH, '//button')
        publish_btn.click()

    # Cikk feltöltés/módosítás/törlés asserthez szükséges cikk adatok
    def article_assert(self, browser):
        title = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//h1')))
        title_data = self.article_data[0]
        article_data = {'title_elem': title, 'title': title_data}
        return article_data

    # Cikk adat beolvasása CSV fáljból
    def article_table_reading(self):
        article_list = []

        with open('Tests/hirek.csv', 'r', encoding='UTF-8') as file:
            article_table = csv.reader(file, delimiter=';')

            for row in article_table:
                article_list.append(row)

        self.article_list = article_list
        return article_list


    # Profil oldalra navigálás
    def go_to_profile(self, browser):
        time.sleep(2)
        nav_links = browser.find_elements(By.XPATH, '//nav/div/ul/li[@class="nav-item"]')
        nav_links[3].click()
        time.sleep(60)


    # Cikkek száma a lista oldalon
    def article_number(self, browser):
        article_list = browser.find_elements(By.CLASS_NAME, 'article-preview')
        self.article_list = article_list
        article_number = len(article_list)
        self.article_amount = article_number

        return article_number


    # Egy konkrét cikk megtalálása és megnyitása
    def find_article(self, browser, article):
        self.articledata(article)
        article_data = self.article_data
        titles = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="preview-link"]//h1')))

        for title in titles:

            if title.text == article_data[0]:
                title.click()


    # Tesztesetek funkciói

    # Cikkek listázása
    def article_listing(self, browser):
        time.sleep(5)
        self.article_number(browser)
        amount = self.article_amount
        counter = 0
        article_title = []
        title_list = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//h1')))
        print()
        print('Kilistázom a cikkek címét')
        print()
        print('Az oldalon megjelenő cikkek címei:')
        print()

        for elem in title_list[1:]:
            counter += 1
            print(f'{counter}. Cikk címe: {elem.text}')
            article_title.append(elem.text)

        self.article_title_list = article_title
        print()
        page_url = browser.current_url
        print(f'Cikkek száma a {page_url} URL című oldalon: {amount}')
        print()

        return article_title


    # Több oldalas lista bejárása
    def multi_page_list_explore(self, browser):
        pages = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="page-link"]')))
        total_pages = len(pages)
        page_number = 0
        print()
        print(f'Lista oldalak száma {total_pages}')
        for article in range(total_pages):
            page_number += 1
            self.article_number(browser)
            amount = self.article_amount
            print(f'{amount} cikk található a {page_number}. oldalon.')
            print()
            time.sleep(5)

            if page_number < total_pages:
                print()
                print('Tovább lépek a lista következő oldalára.')
                next_link = pages[article]
                next_link.click()
                print()
            else:
                print()
                print('Elértem az utolsó lista oldal végére.')
                print()

        # Asserthez szükséges
        numbers_of_pages = {'total': total_pages, 'active': page_number}
        return numbers_of_pages


    # Új cikk feltöltése
    def new_article_upload(self, browser, article):
        self.articledata(article)
        new_article_btn = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ion-compose')))
        new_article_btn.click()
        self.article_input(browser)
        article_info = self.article_assert(browser)
        return article_info


    # Cikk módosítása
    def modify_article(self, browser, article):
        self.articledata(article)

        self.go_to_profile(browser)

        print()
        print('Megkeresem a módosítandó cikket.')
        print()

        self.find_article(browser, article)

        print('Rákattintok az "Edit article" szerkesztés gombra')
        print()

        edit_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ion-edit')))
        edit_btn.click()

        self.article_input(browser)
        article_info = self.article_assert(browser)
        return article_info


    # Cikk törlése
    def delete_article(self, browser, article):
        self.articledata(article)

        self.go_to_profile(browser)

        print()
        print('Megkeresem a törlendő cikket.')
        print()

        self.find_article(browser, article)

        print('Rákattintok az "Delete article" törlés gombra')
        print()

        delete_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ion-trash-a')))
        delete_btn.click()

        self.go_to_profile(browser)
        article_info = self.article_assert(browser)
        return article_info

    # Ismételt és sorozatos adatbevitel adatforrásból/Több cikk feltöltése adatforrásból
    def more_articles_uploads_from_data_source(self, browser):
        self.article_table_reading()
        article_title = []

        for item in self.article_list[1:]:
            article = item
            self.article_data = item
            article_title.append(self.article_data[0])
            self.new_article_upload(browser, article)

        self.go_to_profile(browser)
        self.article_listing(browser)

        return article_title


