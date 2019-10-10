import unittest

from selenium import webdriver

class ValidLogin(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/Home/Selenium/chromedriver")
        self.driver.get("https://ageoflearning.com")
        self.verificationErrors = []
        self.driver.implicitly_wait(2)
        self.accept_next_alert = True
        
    def valid_login(self):
        driver = self.driver
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("password")
        driver.find_element_by_link_text("btnLogin").click()
        
        welcome_text = driver.find_element_by_xpath("//welcome[text()='Welcome Admin']").text
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if _name_ == '_main_':
    unittest.main()
