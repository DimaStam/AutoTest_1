import pytest
import time
import pandas as pd
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage
from pages.SearchPage import SearchPage
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage
from pages.LoginPage import LoginPage
from pages.ExtraoptionsPage import ExtraoptionsPage
import allure

@pytest.mark.usefixtures('setup')
class Test_add_to_cart:
    xl = pd.read_excel('FILEPATH\\Dane.xlsx', sheet_name="Arkusz1")
    baseURL = xl.at[0, 'Wartosc']
    search_keyword = xl.at[10, 'Wartosc']
    value = 1500

    @allure.title('Test dodawania do koszyka')
    def test_add_to_cart(self):
        pytest.skip()
        self.driver.get(self.baseURL)           # otwiera stronę, która jest wskazana w zmiennej baseURL
        self.mp = MainPage(self.driver)         # (mp - main page) wyznacza zmienną self.mp na bazie MainPage
        self.sp = SearchPage(self.driver)       # (sp - search page) wyznacza zmienną self.sp na bazie SearchPage
        self.pp  = ProductPage(self.driver)     # (pp - product page) wyznacza zmienną self.pp na bazie ProductPage
        self.ex = ExtraoptionsPage(self.driver)       # (ex - Extraoptions) wyznacza zmienną self.ex na bazie ExtraoptionsPage
        self.mp.SearchProduct(self.search_keyword)
        self.mp.clickSearchButton()
        self.sp.selectFirstItem()
        self.pp.clickAddToCart()
        time.sleep(2)
        self.ex.AssertExtraoptionsTitle()

    @allure.title('Test komunikatu o niedostępności produktu')
    def test_product_not_available(self):
        # pytest.skip()
        self.driver.get(self.baseURL)
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.pp  = ProductPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ex = ExtraoptionsPage(self.driver)
        self.scp = ShoppingCartPage(self.driver)
        self.mp.clickAcceptCookies()
        self.mp.SearchProduct(self.search_keyword)
        self.mp.clickSearchButton()
        self.sp.selectFirstItem()
        self.pp.clickAddToCart()
        self.ex.clickGoToCart()
        self.pp.setInputValue(self.value)
        time.sleep(5)
        self.pp.AssertProductNotAvailable()