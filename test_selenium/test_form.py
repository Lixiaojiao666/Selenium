from time import sleep

from selenium import webdriver


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_form(self):
        self.driver.get('https://testerhome.com/account/sign_in')
        ele_user = self.driver.find_element_by_id('user_login').send_keys('123')
        ele_passport = self.driver.find_element_by_id('user_password').send_keys('123')
        #ele_remember = self.driver.find_element_by_id('user_remember_me').click()
        ele_remember = self.driver.find_element_by_css_selector('#user_remember_me')
        self.driver.execute_script("arguments[0].click();", ele_remember)
        ele_login = self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        sleep(3)
