from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import self
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys


class Test_Tata:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        yield
        self.driver.close()

    @pytest.fixture()
    def test_case1(self,setup):
        self.driver.get("https://tide.com/en-us")
        self.driver.save_screenshot("C:\Screenshot\page1.jpg")
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Powder")
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.ENTER)
        self.driver.save_screenshot("C:\Screenshot\page2.jpg")
        self.driver.back()
        time.sleep(5)

    @pytest.fixture()
    def test_case2(self,setup,test_case1):
        self.driver.find_element_by_xpath("//a[contains(text(),'What’s New')]").click()
        self.driver.find_element_by_xpath(
            "//p[contains(text(),'Tide Hygienic Clean Heavy Duty 10X Free Power PODS')]").click()
        self.driver.save_screenshot("C:\Screenshot\page3.jpg")
        self.driver.back()
        time.sleep(5)

    @pytest.fixture()
    def test_case3(self,setup,test_case1,test_case2):
        self.driver.find_element_by_xpath("//a[contains(text(),'Contact Us')]").click()
        print(self.driver.title)
        self.driver.save_screenshot("C:\Screenshot\page4.jpg")
        self.driver.back()

    @pytest.fixture()
    def test_case4(self,setup,test_case1,test_case2,test_case3):
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(
            "Laundry Booster")

        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.ENTER)
        self.driver.save_screenshot("C:\Screenshot\page5.jpg")

    def test_case5(self,setup,test_case1,test_case2,test_case3,test_case4):
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Detergent")

        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.ENTER)
        self.driver.save_screenshot("C:\Screenshot\page6.jpg")






