import data as adatok
import configuration as config
import model as model
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConduit(object):

    def setup_method(self):
        self.browser = config.get_preconfigured_chrome_driver()
        self.browser.get(adatok.Urls.home_url)
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()

    # ATC 01 - Regisztráció
    def test_signup(self):
        getusers = model.GetUsers()
        print()
        print('ATC 01 - Regisztráció')
        print()

        getusers.signup(self.browser, 'user1')
        print()
        print('Elvárt eredmény: Sikeres regisztráció után látszik a "Log out" gomb.')
        print()

        assert getusers.logout_btn(self.browser).is_displayed()
        print()
        print('Aktuális eredmény: A regisztráció sikeres, látszik a "Log out" gomb.')
        print()

    # ATC 02 - Bejelentkezés
    def test_signin(self):
        getusers = model.GetUsers()

        print()
        print('ATC 02 - Bejelentkezés')
        print()

        getusers.signin(self.browser, 'user1')

        print()
        print('Elvárt eredmény: Sikeres bejelentkezés után látszik a "Log out" gomb.')
        print()

        assert getusers.logout_btn(self.browser).is_displayed()

        print()
        print('Aktuális eredmény: Sikeres bejelentkezés, látszik a "Log out" gomb.')
        print()

    # ATC 03 - Kijelentkezés
    def test_logout(self):
        getusers = model.GetUsers()

        print()
        print('ATC 03 - Kijelentkezés')
        print()

        # Bejelentkezem az alkalmazásba
        getusers.signin(self.browser, 'user1')

        # Megvárom, amíg megjelenik a "Log out" gomb az oldalon.
        getusers.logout_btn(self.browser)

        # Kijelentkezem az alkalmazásból.
        getusers.logout(self.browser)

        print()
        print('Elvárt eredmény: Sikeres kijelentkezés után látszik a "Sign in" gomb.')
        print()

        assert getusers.signin_btn(self.browser).is_displayed()

        print()
        print('Aktuális eredmény: Sikeres kijelentkezés, látszik a "Sign in" gomb.')
        print()

    # ATC 04 - Adatkezelési nyilatkozat használata
    def test_cookie_handling(self):
        cookie = model.Cookie()

        print()
        print('ATC 04 - Adatkezelési nyilatkozat használata')
        print()

        cookie.cookie_handling(self.browser)

        # Elvárt eredményt a meghívott függvény írja ki.

        # Több assert van, ezeket a meghívott függvény vizsgálja

        # assert cookie_content.is_displayed()
        # assert cookie_accept_btn.is_displayed()
        # assert cookie_decline_btn.is_displayed()
        # assert cookie_bar_displayed == 0

        # Aktuális eredményt a meghívott függvény írja ki.

    # ATC 05 - Adatok listázása
    def test_data_listing(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        print()
        print('ATC 05 - Adatok listázása')
        print()

        getusers.signin(self.browser, 'user1')

        # Megvárom, amíg megjelenik a "Log out" gomb az oldalon.
        getusers.logout_btn(self.browser)

        print()
        print('Elvárt eredmény: Legalább egy cikk van az oldalon.')
        print()

        # Megvizsgálom, található-e legalább egy cikk az oldalon.

        # Kilistázom az oldalon található cikkek címét.
        manipulatepages.article_list_function(self.browser)
        article_amount = manipulatepages.article_amount

        assert article_amount > 0

        print()
        print('Aktuális eredmény: Található cikk az oldalon.')
        print()

        # ATC 06 - Több oldalas lista bejárása

    def test_multi_page_listing(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        print()
        print('ATC 06 - Több oldalas lista bejárása')
        print()

        # Bejelentkezem az alkalmazásba.
        getusers.signin(self.browser, 'user1')

        # Megvárom, amíg megjelenik a "Log out" gomb az oldalon.
        getusers.logout_btn(self.browser)

        # Végig lépegetek a lista oldalain és kigyűjtöm, melyik oldalon hány cikk van.
        page_numbers = manipulatepages.multi_page_list_explore(self.browser)
        total_pages = page_numbers['total']
        active_page_nr = page_numbers['active']

        print()
        print('Elvárt eredmény: Végig lépegetve az oldalakon, elérek a lista utolsó oldaláig.')
        print()

        # Megvizsgálom, hogy az utolsó oldal száma megegyezik-e a lista összes oldalának mennyiségével. Ha a két szám megegyezik, eljutottam a lista utolsó oldalára.
        assert active_page_nr == total_pages

        print(f'Összes oldal száma: {total_pages} / aktív oldal száma: {active_page_nr}')

        print()
        print('Aktuális eredmény: Végig tudtam lépegetni a lista összes oldalán és elértem az utolsó oldalig.')
        print()

        # ATC 07 - Új adat bevitel / Új cikk feltöltése

    def test_new_data_upload(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        article = 'article1_data'

        print()
        print('ATC 07 - Új adat bevitele')
        print()

        # Bejelentkezem az alkalmazásba.
        getusers.signin(self.browser, 'user1')

        # Megvárom, amíg megjelenik a "Log out" gomb az oldalon.
        getusers.logout_btn(self.browser)

        # Feltöltök egy új cikket.
        article_info = manipulatepages.new_article_upload(self.browser, article)
        title_element = article_info['title_elem']
        title = article_info['title']

        print()
        print('Elvárt eredmény: Az új cikk feltöltése sikeres. A cikk címe megjelenik az oldalon.')
        print()

        # Megvizsgálom, megjelenik-e a feltöltött cikk az oldalon.
        # asserts.article_assert(self.browser, article)
        assert title_element.text == title

        print()
        print('Aktuális eredmény: Megjelenik a cikk címe. A cikk felvitele sikeres volt.')
        print()

        # ATC 08 - Adat módosítása / Cikk módosítása

    def test_modify_data(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        article = 'article1_data'

        print()
        print('ATC 08 - Adat módosítása/Cikk módosítása')
        print()

        # Bejelentkezem az alkalmazásba.
        getusers.signin(self.browser, 'user1')

        # Megvárom, amíg megjelenik a "Log out" gomb az oldalon.
        getusers.logout_btn(self.browser)

        # Módosítok egy általam felvitt cikket.
        article_info = manipulatepages.modify_article(self.browser, article)
        title_element = article_info['title_elem']
        title = article_info['title']

        print()
        print('Elvárt eredmény: A cikk módosítása sikeres. A cikk címe megjelenik az oldalon.')
        print()

        # Megvizsgálom, megjelenik-e a módosított cikk.
        assert title_element.text == title

        print()
        print('Aktuális eredmény: Megjelenik a módosított cikk címe. A cikk módosítása sikeres volt.')
        print()

        # ATC 09 - Adat törlése / Cikk törlése

    def test_delete_data(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        article = 'article3_data'

        print()
        print('ATC 09 - Adat törlése/Cikk törlése')
        print()

        # Bejelentkezem az alkalmazásba.
        getusers.signin(self.browser, 'user1')

        # Megvárom, amíg megjelenik a "Log out" gomb az oldalon.
        getusers.logout_btn(self.browser)

        # # Feltöltök egy cikket, amit utána kitörlök.
        manipulatepages.new_article_upload(self.browser, article)

        # Törlöm a létrehozott cikket.
        article_info = manipulatepages.delete_article(self.browser, article)
        title_element = article_info['title_elem']
        title = article_info['title']

        print()
        print('Elvárt eredmény: A cikk törlése sikeres. A cikk nem jelenik már meg az oldalon.')
        print()

        # Megvizsgálom megtalálható-e a törölt cikk címe a lista oldalon.

        try:
            deleted_article = WebDriverWait(self.browser, 2).until(
                EC.presence_of_element_located((By.XPATH, f'//h1[text()="{title}"]')))
            assert False
        except Exception as e:
            assert True

        print()
        print('Aktuális eredmény: A cikk törlése sikeres. A cikk már nem jelenik meg az oldalon.')
        print()

    def test_more_articles_uploads(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        file = adatok.Articles.hirek_csv

        print()
        print('ATC 10 - Ismételt és sorozatos adatbevitel adatforrásból/Cikkek feltöltése csv-ből')
        print()

        # Bejelentkezem az alkalmazásba.
        getusers.signin(self.browser, 'user1')

        # Megvárom, amíg megjelenik a "Log out" gomb az oldalon.
        getusers.logout_btn(self.browser)

        # Feltöltöm a cikkeket.
        article = manipulatepages.more_articles_uploads_from_data_source(self.browser, file)

        print()
        print('Elvárt eredmény: Az új cikkek feltöltése sikeres. A cikkek címe megjelenik az oldalon.')
        print()

        # Megvizsgálom, megjelennek-e a feltöltött cikkek az oldalon.

        for item in article:
            assert item in manipulatepages.article_title_list

        print()
        print('Aktuális eredmény: Megjelenik a feltöltött cikkek címe. A cikkek felvitele sikeres volt.')
        print()

    def test_data_download(self):
        manipulatepages = model.ManipulatePages()

        getusers = model.GetUsers()

        file = adatok.Articles.saved_csv

        print()
        print('ATC 11 - Adatok lementése felületről/Cikkek címének lementése csv-be')
        print()

        # Bejelentkezem az alkalmazásba.
        getusers.signin(self.browser, 'user1')
        time.sleep(5)
        # Megvárom, amíg megjelenik a "Log out" gomb az oldalon.
        getusers.logout_btn(self.browser)

        # Letöltöm a testuser1 felhasználó cikkeinek címét a weboldalról.
        article = manipulatepages.article_download(self.browser, file)

        print()
        print(
            'Elvárt eredmény: A cikkek címének lementése sikeres. A cikkek címe megtalálható a csv fileban. A lementendő cikk címek száma és a csv file-ban található cikkek száma megegyezik.')
        print()

        # Megvizsgálom, a lementedő cikkek száma megegyezik-e a csv file-ban található cikkek számával.

        assert manipulatepages.article_amount == article

        print()
        print('Aktuális eredmény: A lementendő cikk címek száma és a csv file-ban található cikkek száma megegyezik.')
        print()
