from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.Locators import SearchPageLocators
import allure


class SearchPage:
    product_list_xpath = SearchPageLocators.product_list_xpath

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Sprawdzenie czy wyświetlają się produkty. Odbywa się poprzez sprawdzenie czy kontener z komunikatem jest na stronie')
    def AssertSearchPositive(self):
        assert not len(self.driver.find_elements_by_xpath('//div[@class="message notice"]'))


    @allure.step('Sprawdzenie czy na stronie wyświetla się tekst "Brak produktów"')
    def AssertSearchNegative(self):
        assert "Brak wyników wyszukiwania." in self.driver.find_element_by_xpath('//div[@class="message notice"]').text


    @allure.step('Znajdowanie pierwszego elementa z listy oraz klikanie w niego')
    def selectFirstItem(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.product_list_xpath))).click()
    