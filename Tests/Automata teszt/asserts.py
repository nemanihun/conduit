import time
import model
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Asserts:

    # Több tesztesetnél is felhasználható assert
    def general_asserts(self, asserts):
        assert asserts

    # Cikkek listázása teszteset assertje
    def article_listing_assert(self, browser):
        manipulatpages = model.ManipulatePages()
        manipulatpages.article_number(browser)
        print()
        print('Megvizsgálom, jelennek-e meg cikkek az adott oldalon')
        article_numbers = manipulatpages.article_amount

        assert article_numbers > 0

    # Több oldalas lista bejárása teszteset assertje
    def multi_page_listing_assert(self, browser):
        page_number = 0
        active_element = browser.find_elements(By.XPATH, '//nav/ul/li[@class="page-item active"]')
        pages = browser.find_elements(By.XPATH, '//a[@class="page-link"]')
        total_pages = len(pages)

        for item in active_element:
            page_number += int(item.text)

        print('Megvizsgálom, hogy az aktív oldal-e az utolsó oldala a listának')
        print()
        print(f'Összes oldal száma: {total_pages} / aktív oldal száma: {page_number}')

        assert page_number == total_pages

        print()
        print('Az aktív oldal az utolsó oldala a listának. Bejártam a több oldalas lista minden oldalát')

    # Cikk módosítása teszteset assertje
    def article_assert(self, browser, article):
        manipulatpages = model.ManipulatePages()
        manipulatpages.articledata(article)
        title = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//h1')))

        print()
        print('Megvizsgálom, megjelenik-e a cikk')

        time.sleep(5)

        assert title.text == manipulatpages.article_data[0]

    # Cikk törlése teszteset assertje
    def delete_article_assert(self, browser, article):
        manipulatpages = model.ManipulatePages()
        manipulatpages.articledata(article)
        manipulatpages.go_to_profile(browser)

        title = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='preview-link']//h1")))

        print()
        print('Megvizsgálom, megjelenik-e a törölt cikk')

        time.sleep(5)

        assert len(title) == 0
