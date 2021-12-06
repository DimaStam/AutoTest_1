
import pytest
import time
import pandas as pd
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage
from pages.SearchPage import SearchPage
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage
from pages.ExtraoptionsPage import ExtraoptionsPage
from pages.CheckoutDeliveryPage import CheckoutDeliveryPage
import allure

@pytest.mark.usefixtures('setup')
class Test_Login:
    xl = pd.read_excel('FILEPATH\\Dane.xlsx', sheet_name="Arkusz1")
    baseURL = xl.at[0, 'Wartosc']
    username = xl.at[1, 'Wartosc']
    password = xl.at[3, 'Wartosc']
    fake_password = xl.at[11, 'Wartosc']
    search_keyword = xl.at[10, 'Wartosc']

    @allure.title('Test prawidłowego logowania')
    def test_login_passed(self):
        # pytest.skip()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickAccountIcon()
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.lp.AssertHappyPass()

    @allure.title('Test nieprawidłowego logowania')
    def test_login_failed(self):
        # pytest.skip()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickAccountIcon()
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.fake_password)
        self.lp.clickLogin()
        time.sleep(1)
        self.lp.AssertUnhappyPass()

    @allure.title('Test logowania na checkoucie')
    def test_checkout_login(self):
        # pytest.skip()
        self.driver.get(self.baseURL)           # otwiera stronę, która jest wskazana w zmiennej baseURL
        self.mp = MainPage(self.driver)         # (mp - main page) wyznacza zmienną self.mp na bazie MainPage
        self.sp = SearchPage(self.driver)       # (sp - search page) wyznacza zmienną self.sp na bazie SearchPage
        self.pp  = ProductPage(self.driver)     # (pp - product page) wyznacza zmienną self.pp na bazie ProductPage
        self.scp = ShoppingCartPage(self.driver)     # (scp - Shopping Cart page) wyznacza zmienną self.cp na bazie ShoppingCartPage
        self.lp = LoginPage(self.driver)        # (lp - login page) wyznacza zmienną self.lp na bazie LoginPage
        self.ex = ExtraoptionsPage(self.driver)       # (ex - Extraoptions) wyznacza zmienną self.ex na bazie ExtraoptionsPage
        self.cdp = CheckoutDeliveryPage(self.driver)        # (cdp - CheckoutDelivery) wyznacza zmienną self.ex na bazie CheckoutDeliveryPage
        self.mp.SearchProduct(self.search_keyword)
        self.mp.clickSearchButton()
        self.sp.selectFirstItem()
        self.pp.clickAddToCart()
        self.ex.clickGoToCart()
        self.scp.clickGoToOrderButton()
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.cdp.AssertCheckoutDeliveryTitle()