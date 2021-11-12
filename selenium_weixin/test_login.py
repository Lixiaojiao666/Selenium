from time import sleep
from selenium import webdriver


class TestLoginQiYeWeiXin():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    #未登录的状态
    def test_login(self):
        #打开企业微信，点击登录，点击注册，输入用户名
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()

        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="wework_admin.loginpage_wx2_$"]/main/div[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="corp_name"]').send_keys('123456')
        sleep(2)



