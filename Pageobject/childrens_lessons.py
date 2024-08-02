import time
from Pageobject.base_page import BasePage
from utilities.Locators import LTA_Login_Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class LTAPlay(BasePage):
    def __init__(self, driver):
        self.locate = LTA_Login_Page     
        self.actions = ActionChains(driver)
        super().__init__(driver)
        
   
    def set_lta_username(self, lta_username):
        self.set(self.locate.Username, lta_username)
 
    def set_lta_password(self, lta_password):
        self.set(self.locate.Password, lta_password)
       
    def click_lta_login(self):
        time.sleep(2)
        self.click(self.locate.Verify_button)
        time.sleep(2)
        
    def cookies(self):
        self.wait_for_element(self.locate.cookies).click() 
     
    def hover_over_element(self, element):
        super().hover_over_element(element) 
              
    def childrens_page(self):
        self.wait_for_element(self.locate.childrens).click() 
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2) 
        self.wait_for_element(self.locate.resert_button).click()
        
    def search_loc(self,value):  
        time.sleep(2)    
        self.set(self.locate.search_location,value)
        time.sleep(3)
        self.click(self.locate.group_lesson_drops)
        time.sleep(2)
        self.wait_for_element(self.locate.age_dropdown).click()
        self.wait_for_element(self.locate.age).click()
        time.sleep(2) 
        self.wait_for_element(self.locate.find_a_class).click()
        time.sleep(5)
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(3)
        self.wait_for_element(self.locate.intro_course).click()
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        self.wait_for_element(self.locate.signin_for_booking).click()    
        time.sleep(4)
        
    def signin_username(self,value):
        time.sleep(2)
        self.set(self.locate.signin_username,value)  
    def signin_password(self,value):
        self.set(self.locate.signin_password,value)    
    def signin_button(self): 
        time.sleep(2)    
        self.wait_for_element(self.locate.signin_button).click()
        time.sleep(2)   
    
       
    def set_verify_username(self, value):
        time.sleep(5)   
        self.set(self.locate.Username, value)
 
    def set_verify_password(self, value):
        self.set(self.locate.Password,value)
       
    def click_verify_login(self):
        time.sleep(2)
        self.click(self.locate.Verify_button)
        time.sleep(2)            
    def click_book_class(self):  
        time.sleep(3) 
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        self.wait_for_element(self.locate.book_class).click()
        time.sleep(5)   