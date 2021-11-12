import json
from selenium import webdriver

class TestLoginQiYeWeiXin():
    def setup(self):

        #使用remote复用cookie:关掉浏览器,打开命令行，输入：chrome -remote-debugging-port=9222,打开了一个调试用的口子9222
        #声明一个webdriver参数类
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        #设置参数options=chrome_arg，或者chrome_options=chrome_arg复用浏览器，参数不同与selenium版本有关系
        self.driver = webdriver.Chrome(chrome_options=chrome_arg)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    #使用remote复用手动登录的浏览器
    def test_login_fuyong(self):
        # 打开企业微信，(手动登录)点击通讯录，
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()

