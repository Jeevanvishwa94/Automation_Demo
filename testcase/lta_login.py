from Pageobject.login_page import LTAHomePage
from testcase.base_test import BaseTest
from utilities.test_data import TestData
from selenium.webdriver.common.by import By



class TestLogin(BaseTest):
    
    def test_lta_login(self):
        
        lta_loginpage =  LTAHomePage(self.driver)     
        lta_loginpage.set_lta_username(TestData.Username)
        lta_loginpage.set_lta_password(TestData.Password)
        lta_loginpage.click_lta_login()
        lta_loginpage.cookies()
        element = lta_loginpage.find_element(*lta_loginpage.locate.roles_venues)
        lta_loginpage.hover_over_element(element)
        lta_loginpage.coach_button()
        lta_loginpage.Coach_qualification()
        # lta_loginpage.click_element_using_js()  
        # lta_loginpage.move_to_element()
        # lta_loginpage.count_booking()