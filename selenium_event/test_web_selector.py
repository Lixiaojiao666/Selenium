from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWebSelector:
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com/")
        pass
    def teardown(self):
        pass

    def test_web_selector(self):
        #self.driver.find_element：查找元素
        #By.XPATH：用xpath定位
        #'//*[@id="kw"]'：选取所有元素下的id="kw"的元素
        #send_keys("霍格沃兹测试学院")：输入内容
        #self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")

        #By.CSS_SELECTOR : 用CSS_SELECTOR定位
        #'#kw' :选取所有元素下的id="kw"的元素
        #self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃兹测试学院")

        # By.CSS_SELECTOR : 用CSS_SELECTOR定位
        # '[id=kw]' :选取所有元素下的id="kw"的元素
        #self.driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("霍格沃兹测试学院")

        # By.ID : 用ID定位
        # 'kw' : 选取所有元素下的id="kw"的元素
        self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹测试学院")

        self.driver.find_element(By.ID,'su').click()
