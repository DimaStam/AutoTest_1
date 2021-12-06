import pytest
import time
from pages.MainPage import MainPage
from pages.ContactFormPage import ContactFormPage
import pandas as pd
import allure

@pytest.mark.usefixtures('setup')
class Test_ContactForm:
    xl = pd.read_excel('FILEPATH\\Dane.xlsx', sheet_name="Arkusz1")
    baseURL = xl.at[0, 'Wartosc']
    name = xl.at[5, 'Wartosc']
    email = xl.at[1, 'Wartosc']
    phone = xl.at[8, 'Wartosc']
    comment = xl.at[9, 'Wartosc']

    @allure.title('Weryfikacja działania formularzu kontaktowego')
    def test_contact_form(self):
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.mp = MainPage(self.driver)
        self.cf = ContactFormPage(self.driver)
        try:
            self.mp.clickAcceptCookies()
        except:
            print('Nie ma cookies')
        else:
            self.mp.clickContactForm()
            self.cf.SetContactFormUserName(self.name)
            self.cf.SetContactFormEmail(self.email)
            self.cf.SetContactFormPhone(self.phone)
            self.cf.SetContactFormComment(self.comment)
            self.cf.clickSendButton()
            self.cf.AssertContactFormSent()