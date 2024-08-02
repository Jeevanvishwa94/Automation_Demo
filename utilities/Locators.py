from selenium.webdriver.common.by import By


class LTA_Login_Page:
    Username = (By.ID, "u")
    Password = (By.ID, "p")
    Verify_button = (By.XPATH, "//input[@type='submit']")
    cookies = (By.XPATH,'//button[@id="lta-cookies-button"]')
    roles_venues =(By.XPATH,'//*[@id="lta-mega-nav-navigation"]/div/ul/li[4]/button')
    coach = (By.XPATH, "//*[@id='lta-mega-nav-navigation']/div/ul/li[4]/div/div[2]/div/ul[1]/li[2]/a")
    calenter_month = (By.XPATH,'(//button[@id="eventmonth-id"])[2]')
    joinus =(By.XPATH,'//a[text()="Join Us"]')
    play=(By.XPATH, "//*[@id='lta-mega-nav-navigation']/div/ul/li[1]/button")
    childrens = (By.XPATH, '//*[@id="lta-mega-nav-navigation"]/div/ul/li[1]/div/div[2]/div/ul[3]/li[4]/a')
    resert_button= (By.XPATH,'//button[@aria-label="reset search"]')
    search_location = (By.XPATH,'//*[@id="lta-simple-panel-1"]/form/div[1]/div/div/div/div/input[3]')
    group_lesson_drops=(By.XPATH,"(//div[@class='pac-item'])[1]")
    age_dropdown = (By.XPATH,'//div[@class="lta-select__caret-down"]')
    age = (By.XPATH,"//div[@id='lta-select__selected-age-group--option-2']")
    find_a_class = (By.XPATH,"//*[@id='lta-simple-panel-1']/form/div[4]/button")
    intro_course = (By.XPATH,"//*[@id='ResultForm']/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/h2/a")
    signin_for_booking = (By.XPATH,"//*[@id='main-content']/div/section[1]/div/div/div[3]/div/div[3]/div/div[2]/a")
    signin_username=(By.XPATH,'//*[@id="56:2;a"]')
    signin_password =(By.XPATH,'//*[@id="input-2"]')
    signin_button = (By.XPATH,'/html/body/div[3]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div[4]/button')
    book_class = (By.XPATH,'//a[text()="Book class"]')
    # court_book =(By.XPATH,"//a[@href='/play/book-a-tennis-court/']")
    search_button = (By.XPATH,"(//button[@type='button'])[13]")
    search_text = (By.CLASS_NAME,"q")
    search_icon = (By.XPATH,"//button[text()='Search']")
    CPD_learning = (By.XPATH,'//*[@id="main-content"]/div/div/div[2]/div/div[3]/a/div[1]/p[1]')

  
  