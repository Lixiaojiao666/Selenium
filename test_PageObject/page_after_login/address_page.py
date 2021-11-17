from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:

    def __init__(self,driver):
        self.driver = driver

    def add_members(self):

        #显式等待：等待10，直到 元素可被点击
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="js_contacts58"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]')))

        self.driver.find_element(By.XPATH,'//*[@id="js_contacts58"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('李小梨1')
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys('lixiaoli1')
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys('15518806667')
        self.driver.find_element_by_xpath('//*[@id="js_contacts58"]/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
