import pytest
import time
import pandas as pd
from pages.CreateAccountPage import CreateAccountPage
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage
from pages.ExtraoptionsPage import ExtraoptionsPage
import allure

@pytest.mark.usefixtures('setup')
class Test_CreateAccount:
    xl = pd.read_excel('FILEPATH\\Dane.xlsx', sheet_name="Arkusz1")
    baseURL = xl.at[0, 'Wartosc']
    email_1 = xl.at[1, 'Wartosc']
    email_2 = xl.at[2, 'Wartosc']
    password = xl.at[3, 'Wartosc']
    name = xl.at[5, 'Wartosc']
    lastname = xl.at[6, 'Wartosc']
    search_keyword = xl.at[10, 'Wartosc']

    @allure.title('Test rejestracji użytkownika')
    def test_create_account(self):
        # pytest.skip()
        self.driver.get(self.baseURL)
        self.cap = CreateAccountPage(self.driver)
        self.cap.clickAccountIcon()
        self.cap.clickCreateAccount()
        self.cap.setName(self.name)
        self.cap.setUserLastname(self.lastname)
        self.cap.setEmail(self.email_1)
        self.cap.setUserPassword(self.password)
        self.cap.setUserPasswordConf(self.password)
        self.cap.clickSighIn()
        time.sleep(30)
        self.cap.AssertRegistrationSuccess()

    @allure.title('Test rejestracji na checkoucie')
    def test_checkout_create_account(self):
        # pytest.skip()
        self.driver.get(self.baseURL)           # otwiera stronę, która jest wskazana w zmiennej baseURL
        self.mp = MainPage(self.driver)         # (mp - main page) wyznacze zmienną self.mp na bazie MainPage
        self.sp = SearchPage(self.driver)       # (sp - search page) wyznacze zmienną self.sp na bazie SearchPage
        self.pp  = ProductPage(self.driver)     # (pp - product page) wyznacze zmienną self.pp na bazie ProductPage
        self.scp = ShoppingCartPage(self.driver)     # (scp - shopping cart page) wyznacze zmienną self.scp na bazie ShoppingCartPage
        self.cap = CreateAccountPage(self.driver)   # (cap - create account page) wyznacze zmienną self.cap na bazie CreateAccountPage
        self.ex = ExtraoptionsPage(self.driver)       # (ex - Extraoptions) wyznacze zmienną self.ex na bazie ExtraoptionsPage
        self.mp.SearchProduct(self.search_keyword)
        self.mp.clickSearchButton()
        self.sp.selectFirstItem()
        self.pp.clickAddToCart()
        self.ex.clickGoToCart()
        self.scp.clickGoToOrderButton()
        self.cap.clickCreateAccount()
        self.cap.setName(self.name)
        self.cap.setUserLastname(self.lastname)
        self.cap.setEmail(self.email_2)
        self.cap.setUserPassword(self.password)
        self.cap.setUserPasswordConf(self.password)
        self.cap.clickSighIn()
        time.sleep(30)
        self.cap.AssertRegistrationSuccess()