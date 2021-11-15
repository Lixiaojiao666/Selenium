import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginQiYeWeiXin():
    def setup(self):

        #使用remote复用cookie:关掉浏览器,打开命令行，输入：chrome -remote-debugging-port=9222,打开了一个调试用的口子9222
        #声明一个webdriver参数类
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        #设置参数options=chrome_arg，或者chrome_options=chrome_arg复用浏览器，参数不同与selenium版本有关系
        self.driver = webdriver.Chrome(chrome_options=chrome_arg)

        #隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    #使用remote复用手动登录的浏览器
    def test_add_members(self):
        # 打开企业微信，(手动登录)点击通讯录，
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()

        #显式等待：等待10，直到 元素可被点击
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="js_contacts54"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]')))

        self.driver.find_element_by_xpath('//*[@id="js_contacts54"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('李小梨')
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys('lixiaoli')
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys('15518806666')
        self.driver.find_element_by_xpath('//*[@id="js_contacts54"]/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()


