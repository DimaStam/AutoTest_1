from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from locators.Locators import ShoppingCartPageLocators
import allure

class ShoppingCartPage:
    go_to_order_xpath = ShoppingCartPageLocators.go_to_order_xpath
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Kliknięcie przyciska "Dalej"')
    def clickGoToOrderButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.go_to_order_xpath))).click()

    @allure.step('Sprawdzenie title strony Koszyk')
    def AssertShoppingCartTitle(self):
        assert "Koszyk" in self.driver.title
    