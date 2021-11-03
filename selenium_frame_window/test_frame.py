from selenium_frame_window.base import Base

#//*[@id="iframeResult"]   //*[@id="draggable"] //*[@id="submitBTN"]
class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

        #切换到frame下，才能定位到元素
        self.driver.switch_to.frame('iframeResult')
        #另外一种切换方式
        #self.driver.switch_to_frame('iframeResult')

        # 定位元素，获取文本，打印出来
        print(self.driver.find_element_by_id('draggable').text)

        #切换回父frame
        self.driver.switch_to.parent_frame()
        #另一种切换方式：切换回默认的frame
        #self.driver.switch_to.default_content()

        #找到 点击运行 按钮，获取文本，打印出来
        print(self.driver.find_element_by_id('submitBTN').text)

