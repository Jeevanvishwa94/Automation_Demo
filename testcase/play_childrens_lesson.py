from Pageobject.childrens_lessons import LTAPlay
from Pageobject.login_page import LTAHomePage
from testcase.base_test import BaseTest
from utilities.test_data import TestData
from selenium.webdriver.common.by import By




class TestPlay(BaseTest):
    
    def test_lta_play(self):
        
        lta_loginpage = LTAPlay(self.driver)    
        lta_loginpage.set_lta_username(TestData.Username)
        lta_loginpage.set_lta_password(TestData.Password)
        lta_loginpage.click_lta_login()
        lta_loginpage.cookies()
        element = lta_loginpage.find_element(*lta_loginpage.locate.play)
        lta_loginpage.hover_over_element(element)
        lta_loginpage.childrens_page()
        lta_loginpage.search_loc("Wim")
        lta_loginpage.signin_username("ppeusergp50")
        lta_loginpage.signin_password("Admin@123")
        lta_loginpage.signin_button()
        lta_loginpage.set_verify_username("jeevan.v@verolt.com")
        lta_loginpage.set_verify_password("15July@2024")
        lta_loginpage.click_verify_login()
        lta_loginpage.click_book_class()
        