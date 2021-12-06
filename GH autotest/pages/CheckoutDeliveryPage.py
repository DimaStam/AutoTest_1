from locators.Locators import CheckoutDeliveryLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure

class CheckoutDeliveryPage:
    proceed_to_summary_button_id = CheckoutDeliveryLocators.proceed_to_summary_button_id
    email_input_id = CheckoutDeliveryLocators.email_input_id
    phone_input_xpath = CheckoutDeliveryLocators.phone_input_xpath
    firstname_input_xpath = CheckoutDeliveryLocators.firstname_input_xpath
    lastname_input_xpath = CheckoutDeliveryLocators.lastname_input_xpath
    street_input_xpath = CheckoutDeliveryLocators.street_input_xpath
    postcode_input_xpath = CheckoutDeliveryLocators.postcode_input_xpath
    city_input_xpath = CheckoutDeliveryLocators.city_input_xpath

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Wpisywanie danych w polu "E-mail"')
    def setEmail(self, email):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.email_input_id))).clear()
        self.driver.find_element_by_id(self.email_input_id).send_keys(email)

    @allure.step('Wpisywanie danych w polu "Telefon"')
    def setPhoneNumber(self, phone):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.phone_input_xpath))).clear()
        self.driver.find_element_by_xpath(self.phone_input_xpath).send_keys(phone)

    @allure.step('Wpisywanie danych w polu "Imie"')
    def setFirstName(self, name):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.firstname_input_xpath))).clear()
        self.driver.find_element_by_xpath(self.firstname_input_xpath).send_keys(name)

    @allure.step('Wpisywanie danych w polu "Nazwisko"')
    def setLastName(self, lastname):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.lastname_input_xpath))).clear()
        self.driver.find_element_by_xpath(self.lastname_input_xpath).send_keys(lastname)

    @allure.step('Wpisywanie danych w polu "Ulica"')
    def setStreet(self, street):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.street_input_xpath))).clear()
        self.driver.find_element_by_xpath(self.street_input_xpath).send_keys(street)

    @allure.step('Wpisywanie danych w polu "Kod pocztowy"')
    def setPostcode(self, postcode):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.postcode_input_xpath))).clear()
        self.driver.find_element_by_xpath(self.postcode_input_xpath).send_keys(postcode)

    @allure.step('Wpisywanie danych w polu "Miasto"')
    def setCity(self, city):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.city_input_xpath))).clear()
        self.driver.find_element_by_xpath(self.city_input_xpath).send_keys(city)

    @allure.step('Wyszukiwanie przyciska "Zobacz podsumowanie" oraz klikanie w niego')
    def clickProceedToSummaryButton(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.ID, self.proceed_to_summary_button_id))).click()

    @allure.step('Sprawdzenie title strony Dostawa')
    def AssertCheckoutDeliveryTitle(self):
        assert "Zamówienie" in self.driver.title