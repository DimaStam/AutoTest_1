### Ogarnąć test nieprawidłowego logowania się

from locators.Locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class LoginPage:
    # Zwraca się do pliku locators.py i wczytuje dane zmiennej
    customer_account_icon_xpath = LoginPageLocators.customer_account_icon_xpath
    email_input_id = LoginPageLocators.email_input_id
    password_input_id = LoginPageLocators.password_input_id
    login_button_xpath = LoginPageLocators.login_button_xpath
    logout_button_xpath = LoginPageLocators.logout_button_xpath
    account_data_button_xpath = LoginPageLocators.account_data_button_xpath
    reset_password_checkbox_xpath = LoginPageLocators.reset_password_checkbox_xpath
    current_password_id = LoginPageLocators.current_password_id
    new_password_id = LoginPageLocators.new_password_id
    confirm_new_password_id = LoginPageLocators.confirm_new_password_id
    save_button_xpath = LoginPageLocators.save_button_xpath
    notification_xpath = LoginPageLocators.notification_xpath

    def __init__(self, driver):
        self.driver = driver

    # znajduje przycisk "Zaloguj się"
    @allure.step('Klikanie w ikonkę logowania')
    def clickAccountIcon(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.customer_account_icon_xpath))).click()

    # znajduje pole do wprowadzenia emaila oraz wpisuje dane, które znajdują się pod zmienną 'username'
    @allure.step('Wpisywanie danych username')
    def setUserName(self, username):
        self.driver.find_element_by_id(self.email_input_id).clear()
        self.driver.find_element_by_id(self.email_input_id).send_keys(username)

    # znajduje pole do wprowadzenia hasła oraz wpisuje dane, które znajdują się pod zmienną 'password'
    @allure.step('Wpisywanie danych password')
    def setUserPassword(self, password):
        self.driver.find_element_by_id(self.password_input_id).clear()
        self.driver.find_element_by_id(self.password_input_id).send_keys(password)

    # znajduje button "Zaloguj się" oraz klika w niego
    @allure.step('Klikanie w przycisk "Zaloguj się"')
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    # znajduje button "Wyloguj się" oraz klika w niego
    @allure.step('Klikanie w przycisk "Wyloguj się"')
    def clickLogout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.logout_button_xpath))).click()

    # znajduje button "Zmień hasło" oraz klika w niego
    @allure.step('Klikanie w przycisk "Zmień hasło" w panelu klienta')
    def clickAccountData(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.account_data_button_xpath))).click()

    # znajduje button "Zmień hasło" oraz klika w niego
    @allure.step('Klikanie w checkbox "Zmień hasło" w panelu klienta')
    def clickResetPassword(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.reset_password_checkbox_xpath))).click()

    # znajduje pole do wprowadzenia aktualnego hasła oraz wpisuje dane, które znajdują się pod zmienną 'password'
    @allure.step('Wpisywanie aktualnego hasła')
    def setUserActualPassword(self, password):
        self.driver.find_element_by_id(self.current_password_id).clear()
        self.driver.find_element_by_id(self.current_password_id).send_keys(password)

    # znajduje pole do wprowadzenia nowego hasła oraz wpisuje dane, które znajdują się pod zmienną 'new_password'
    @allure.step('Wpisywanie nowego hasła')
    def setUserNewPassword(self, new_password):
        self.driver.find_element_by_id(self.new_password_id).clear()
        self.driver.find_element_by_id(self.new_password_id).send_keys(new_password)

    # znajduje pole do wprowadzenia potwierdzenia nowego hasła oraz wpisuje dane, które znajdują się pod zmienną 'new_password'
    @allure.step('Potwierdzenie nowego hasła')
    def setConfirmUserNewPassword(self, new_password):
        self.driver.find_element_by_id(self.confirm_new_password_id).clear()
        self.driver.find_element_by_id(self.confirm_new_password_id).send_keys(new_password)

    # znajduje button "ZZapisz" oraz klika w niego
    @allure.step('Klikanie w przycisk "Zapisz" w formularzu zmiany hasła')
    def clickSave(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button_xpath))).click()

    @allure.step('Sprawdzenie czy na stronie wyświetla się tekst "Moje zamówienia"')
    def AssertHappyPass(self):
        assert "Moje konto" in self.driver.title
        # assert "Moje konto" in self.driver.find_element_by_xpath('//h1[@class="page-title"]').text

    @allure.step('Sprawdzenie czy na stronie wyświetla się komunikat o wpisaniu nieprawidowych danych')
    def AssertUnhappyPass(self):
        assert "Logowanie się nie udało :( Sprawdź poprawność danych i spróbuj ponownie" in self.driver.find_element_by_xpath('//div[@class="message-error error message"]').text

    @allure.step('Sprawdzenie czy na stronie wyświetla się komunikat o pomyślnej zmianie hasła')
    def AssertPasswordChanged(self):
        assert "Dane konta zostały zapisane." in self.driver.find_element_by_xpath('//div[@class="message-success success message"]').text
    