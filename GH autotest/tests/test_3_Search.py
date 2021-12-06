import pytest
import pandas as pd
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
import allure

@pytest.mark.usefixtures('setup')
class Test_Search:
    xl = pd.read_excel('FILEPATH\\Dane.xlsx', sheet_name="Arkusz1")
    baseURL = xl.at[0, 'Wartosc']
    existing_fraze = xl.at[0, 'Input']
    not_existing_fraze = xl.at[1, 'Input']
    single_character_fraze = xl.at[2, 'Input']
    special_character_fraze = xl.at[3, 'Input']
    SQL_request = xl.at[4, 'Input']

    @allure.title('4.2.1 Wyszukiwarka dla fraz istniejących')
    def test_search_existing_fraze(self):
        # pytest.skip()
        self.driver.get(self.baseURL)       # otwiera stronę, która jest wskazana w zmiennej baseURL
        self.mp = MainPage(self.driver)     # (mp - main page) wyznacza zmienną self.mp na bazie MainPage
        self.sp = SearchPage(self.driver)   # (sp - search page) wyznacza zmienną self.sp na bazie MainPage
        self.mp.SearchExistingFraze(self.existing_fraze)
        self.mp.clickSearchButton()
        self.sp.AssertSearchPositive()

    @allure.title('4.2.2 Wyszukiwarka dla fraz nieistniejących')
    def test_search_not_existing_fraze(self):
        # pytest.skip()
        self.driver.get(self.baseURL)       
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)    
        self.mp.SearchNotExistingFraze(self.not_existing_fraze)
        self.mp.clickSearchButton()
        self.sp.AssertSearchNegative()

    @allure.title('4.2.3 Wyszukiwarka dla pojedynczego znaku')
    def test_search_single_character_fraze(self):
        # pytest.skip()
        self.driver.get(self.baseURL)       
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)    
        self.mp.SearchSingleCharacter(self.single_character_fraze)
        self.mp.clickSearchButton()
        self.sp.AssertSearchPositive()

    @allure.title('4.2.3 Wyszukiwarka dla znaku specjalnego')
    def test_search_special_character_fraze(self):
        # pytest.skip()
        self.driver.get(self.baseURL)       
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver)    
        self.mp.SearchSpecialCharacter(self.special_character_fraze)
        self.mp.clickSearchButton()
        self.sp.AssertSearchNegative()

    @allure.title('4.2.4 Wyszukiwarka dla zapytania SQL')
    def test_search_sql_request(self):
        # pytest.skip()
        self.driver.get(self.baseURL)       
        self.mp = MainPage(self.driver)
        self.sp = SearchPage(self.driver) 
        self.mp.SearchSQLrequest(self.SQL_request)
        self.sp.AssertSearchNegative()