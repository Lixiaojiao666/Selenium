from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction():
    def setup(self):

        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)

        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_touchaction_scrollbottom(self):
        '''
        打开Chrome
        打开URL: http://www.baidu.com
        向搜索框中输入‘selenium测试’
        通过TouchAction点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        :return:
        '''
        #打开百度
        self.driver.get('http://www.baidu.com')
        #找到输入框（id为kw），输入'selenium测试'
        ele1 = self.driver.find_element_by_id('kw').send_keys('selenium测试')
        #找到 百度一下 按钮（id为su）
        ele2 = self.driver.find_element_by_id('su')


        #实例化一个TouchActions对象
        actions = TouchActions(self.driver)
        #点击 百度一下按钮
        actions.tap(ele2)
        # 滑动到底端，不知道底端的具体坐标，所以给一个尽量大的值
        actions.scroll_from_element(ele2, 0, 10000)
        sleep(3)

        actions.perform()

        #找到 下一页 按钮，点击它
        #actions.tap(self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]')).perform()

        sleep(3)
        self.driver.refresh()
        actions.tap(self.driver.find_element(By.XPATH, '//*[@id="page"]/div/a[10]')).perform()


