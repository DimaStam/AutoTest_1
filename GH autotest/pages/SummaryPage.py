from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
import time
from locators.Locators import SummaryPageLocators
import allure

class SummaryPage:
    payU_xpath = SummaryPageLocators.payU_xpath
    blik_xpath = SummaryPageLocators.blik_xpath
    apple_pay_xpath = SummaryPageLocators.apple_pay_xpath
    raty_payU_xpath = SummaryPageLocators.raty_payU_xpath
    raty_CA_xpath = SummaryPageLocators.raty_CA_xpath
    twisto_xpath = SummaryPageLocators.twisto_xpath
    bank_transfer_xpath = SummaryPageLocators.bank_transfer_xpath
    paypal_xpath = SummaryPageLocators.paypal_xpath
    agreement_1_id = SummaryPageLocators.agreement_1_id
    agreement_2_id = SummaryPageLocators.agreement_2_id
    order_and_pay_button_xpath = SummaryPageLocators.order_and_pay_button_xpath
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Wybór opcji opłaty PayU')
    def selectPayU(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.payU_xpath))).click()

    @allure.step('Wybór opcji opłaty Blik')
    def selectBlik(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.blik_xpath))).click()

    @allure.step('Wybór opcji opłaty Apple Pay')
    def selectApplePay(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.apple_pay_xpath))).click()

    @allure.step('Wybór opcji opłaty Raty PayU')
    def selectRatyPayU(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.raty_payU_xpath))).click()

    @allure.step('Wybór opcji opłaty Raty Credit Agricole')
    def selectRatyCA(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.raty_CA_xpath))).click()

    @allure.step('Wybór opcji opłaty Twisto')
    def selectTwisto(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.twisto_xpath))).click()

    @allure.step('Wybór opcji opłaty Przelew Tradycyjny')
    def selectBankTransfer(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.bank_transfer_xpath))).click()

    @allure.step('Wybór opcji opłaty PayPal')
    def selectPayPal(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.paypal_xpath))).click()

    @allure.step('Zaznaczenie pierwszego checkboxa')
    def clickCheckbox1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, self.agreement_1_id))).click()

    @allure.step('Zaznaczenie drugiego checkboxa')
    def clickCheckbox2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, self.agreement_2_id))).click()

    @allure.step('Klikanie w przycisk "Zamawiam i płacę"')
    def clickOrderAndPayButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.order_and_pay_button_xpath))).click()

    @allure.step('Sprawdzenie title strony')
    def AssertPayUTitle(self):
        assert "PayU" in self.driver.title

    @allure.step('Sprawdzenie title strony')
    def AssertRatyCATitle(self):
        assert "Bank Credit Agricole - Crédit Agricole" in self.driver.title

    @allure.step('Sprawdzenie title strony')
    def AssertPayPalTitle(self):
        assert "Zaloguj się do swojego konta PayPal" in self.driver.title

    @allure.step('Sprawdzenie czy na stronie wyświetla się tekst "Dziękujemy za złożenie zamówienia!"')
    def AssertSuccessPage(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Dziękujemy za złożenie zamówienia!')]")))
        assert True