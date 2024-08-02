import time
from Pageobject.base_page import BasePage
from utilities.Locators import LTA_Login_Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class LTAHomePage(BasePage):
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
        time.sleep(3)
        
    def cookies(self):
        self.wait_for_element(self.locate.cookies).click()
     
    def hover_over_element(self, element):
        super().hover_over_element(element)
        
    def coach_button(self):
        self.wait_for_element(self.locate.coach).click()
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)     
    def Coach_qualification(self):      
        self.wait_for_element(self.locate.CPD_learning).click()
        time.sleep(3)
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(3)
        
                  
        
    # def click_element_using_js(self):
    #     script = "arguments[0].click();"
    #     element = self.locate.coach  # Assuming this returns the web element
    #     self.execute_script(script, element)
             
    # def hover_over_element(self, element):
    #     super().hover_over_element(element)   
              
    # self.wait_for_element(self.locate.calenter_month).click()
        
    # def search_box(self):
            
    # def count_booking(self):
    #     self.wait_for_element(self.locate.cookies).click()
    #     time.sleep(5)
    #     # self.click(self.locate.joinus)
    #     self.wait_for_element(self.locate.play).click()
    #     self.wait_for_element(self.locate.court_book).click()
    #     time.sleep(5)
  