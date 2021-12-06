import pytest
import time
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
import pandas as pd
import allure

@pytest.mark.usefixtures('setup')
class Test_Reset_Password:
    xl = pd.read_excel('FILEPATH\\Dane.xlsx', sheet_name="Arkusz1")
    baseURL = xl.at[0, 'Wartosc']
    username = xl.at[1, 'Wartosc']
    password = xl.at[3, 'Wartosc']
    new_password = xl.at[4, 'Wartosc']

    @allure.title('Test zmiany hasła używtkownika')
    def test_reset_password(self):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.mp = MainPage(self.driver)
        self.mp.clickAcceptCookies()
        self.lp.clickAccountIcon()
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickAccountData()
        self.lp.clickResetPassword()
        self.lp.setUserActualPassword(self.password)
        self.lp.setUserNewPassword(self.new_password)
        self.lp.setConfirmUserNewPassword(self.new_password)
        time.sleep(3)
        self.lp.clickSave()
        self.lp.AssertPasswordChanged()

    @allure.title('Test prawidłowego logowania po zmianie hasła')
    def test_login_passed(self):
        # pytest.skip()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickAccountIcon()
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.new_password)
        self.lp.clickLogin()
        self.lp.AssertHappyPass()

    @allure.title('Test logowania używając stare hasło')
    def test_login_old_password(self):
        # pytest.skip()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickAccountIcon()
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        self.lp.AssertUnhappyPass()

# pytest --alluredir=FILEPATH\GH autotest\report
# allure serve FILEPATH\GH autotest\report