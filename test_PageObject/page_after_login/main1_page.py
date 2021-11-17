from selenium import webdriver
from selenium.webdriver.common.by import By

from test_PageObject.page_after_login.address_page import AddressPage


class MainPage1:
    def __init__(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        # 设置参数options=chrome_arg，或者chrome_options=chrome_arg复用浏览器，参数不同与selenium版本有关系
        self.driver = webdriver.Chrome(chrome_options=chrome_arg)
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.implicitly_wait(5)

    def goto_address(self):
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        self.driver.find_element(By.XPATH,'//*[@id="menu_contacts"]/span').click()
        return AddressPage(self.driver)