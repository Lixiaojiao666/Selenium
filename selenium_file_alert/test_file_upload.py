from time import sleep

from selenium_frame_window.base import Base


class TestFileUpload(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        sleep(3)
        self.driver.find_element_by_id('stfile').send_keys("C:/Users/Administrator/Pictures/Camera Roll/123.png")
        sleep(3)
