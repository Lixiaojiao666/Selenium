from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts:
    def setup(self):
        # self.driver 加了self后，就变成类的实例变量，这样就可以在其他的测试方法或者地方调用了
        self.driver = webdriver.Firefox()
        # 隐式等待:在设置的时间内动态的去查找元素，如果找到了，就不再继续等待，直接进行下一步操作
        # 隐式等待一般设置在setup()里，这样就会对所有的操作都生效，都会进行隐式等待
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.baidu.com")


    def teardown(self):
        #关闭驱动
        self.driver.quit()

    def test_baidu(self):
        #sleep(1)#强制等待
        #find_element(By.ID,"kw") 通过ID定位元素
        #send_keys 输入内容
        self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹测试学院")
        #sleep(1)
        self.driver.find_element(By.ID,"su").click()
        #sleep(1)
        self.driver.find_element(By.LINK_TEXT,"霍格沃兹测试学院 - 主页")
