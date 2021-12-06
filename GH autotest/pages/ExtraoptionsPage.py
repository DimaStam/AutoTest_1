from locators.Locators import ExtraoptionsPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure

class ExtraoptionsPage:
    go_to_cart_button_xpath = ExtraoptionsPageLocators.go_to_cart_button_xpath 

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Wyszukiwanie przyciska "Zobacz koszyk" oraz klikanie w niego')
    def clickGoToCart(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, self.go_to_cart_button_xpath))).click()

    @allure.step('Sprawdzenie title strony Extraoptions')
    def AssertExtraoptionsTitle(self):
        assert "Dodano do koszyka" in self.driver.title