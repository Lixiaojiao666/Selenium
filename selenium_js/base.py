import os

from selenium import webdriver


class Base():
    def setup(self):
        #创建一个浏览器变量，接住os传过来的浏览器参数，对参数做判断，
        # 看是哪个浏览器，然后就启动对应的浏览器driver
        browser = os.getenv('browser')
        if browser == 'firefox':
            print('使用浏览器:firefox')
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            print(f'使用浏览器:headless')
            self.driver = webdriver.PhantomJS
        else:
            print(f'使用浏览器:Chrome')
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()
