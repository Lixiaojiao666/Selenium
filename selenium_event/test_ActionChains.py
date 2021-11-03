from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Firefox()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    #skip跳过，无条件和原因的跳过
    @pytest.mark.skip()
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        #element_click = self.driver.find_element(By.XPATH,'/html/body/form/input[3]')
        #element_double_click = self.driver.find_element(By.XPATH,'/html/body/form/input[2]')
        #element_right_click = self.driver.find_element(By.XPATH, '/html/body/form/input[4]')

        #self.driver.find_element() 与  find_element_by_xpath()
        #xpath路径 ： /html/body/form/input[4] 与 //input[@value='click me  是一样的

        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_double_click = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_right_click = self.driver.find_element_by_xpath("//input[@value='right click me']")

        actions = ActionChains(self.driver)
        actions.click(element_click)
        actions.context_click(element_right_click)
        actions.double_click(element_double_click)
        sleep(3)
        actions.perform()
        sleep(3)

    @pytest.mark.skip()
    #将鼠标移动到百度首页右上角设置按钮
    def test_move_to_element(self):
        #打开百度网页
        self.driver.get("https://www.baidu.com")
        #定位到设置元素
        #ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        ele = self.driver.find_element_by_id('s-usersetting-top')
        #ele = self.driver.find_element_by_link_text("设置")

        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    #鼠标拖拽
    @pytest.mark.skip()
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMoolTools.htm')
        drag_ele = self.driver.find_element_by_id('dragger')
        drop_ele = self.driver.find_element_by_xpath('/html/body/div[2]')

        action = ActionChains(self.driver)

        #拖拽到一个位置，然后释放
        #action.drag_and_drop(drag_ele,drop_ele)
        #在drag_ele位置点击鼠标，并且不放开，到drop_ele位置，释放鼠标
        action.click_and_hold(drag_ele).release(drop_ele)
        #在drag_ele位置点击鼠标，并且不放开，移动到drop_ele位置，然后释放鼠标
        action.click_and_hold(drag_ele).move_to_element(drop_ele).release()

        action.perform()
        sleep(3)


    #模拟键盘操作
    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        #定位输入框
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        #点击输入框
        ele.click()


        action = ActionChains(self.driver)
        #向输入框中输入username，pause(1)暂停1S
        action.send_keys("username").pause(1)
        #向输入框中输入空格，pause(1)暂停1S
        action.send_keys(Keys.SPACE).pause(1)
        #向输入框中输入tom，pause(1)暂停1S
        action.send_keys("tom").pause(1)
        # 向输入框中输入BACKSPACE，pause(1)暂停1S
        action.send_keys(Keys.BACK_SPACE).pause(1)

        action.perform()
        sleep(3)

#if __name__ == '__main__':
#   pytest.main(['-v','-s',''])
