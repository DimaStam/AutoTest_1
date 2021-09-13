from tests.base_test import BaseTest
from pages.main_page import *


class TestSignInPage(BaseTest):
    #page loaded test
    def test_page_load(self):
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded)


    # #search Suunto test
    # def test_search_item(self):
    #     page = MainPage(self.driver)
    #     search_result = page.search_item('Suunto')
    #     self.assertIn('Suunto', search_result)

    # #signup button is visible
    # def test_sign_up_button(self):
    #     page = MainPage(self.driver)
    #     sign_up_page = page.click_sign_up_button()
    #     self.assertIn('Logowanie', sign_up_page.get_url())

 
# python -m unittest tests.test_sign_in_page.TestSignInPage