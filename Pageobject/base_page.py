from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
 
class BasePage:
    """
    The Purpose Of A Basepage Is To Contain Methods Common To All Page Objects
    """
   
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
 
    def find(self,*locator):
        return self.driver.find_element(*locator)
 
    def click(self, locator):  
        self.find(*locator).click()
        # self.driver.find_element(*locator).click()
 
    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)
    
    def get_text(self, locator):
        return self.find(*locator).text
 
    def get_title(self):
        return self.driver.title
   
    def wait_for_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def execute_script(self, script: str, *args):
        return self.driver.execute_script(script, *args)
    
    def find_element(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def hover_over_element(self, element):
        from selenium.webdriver.common.action_chains import ActionChains
        action = ActionChains(self.driver)
        action.move_to_element(element).perform() 