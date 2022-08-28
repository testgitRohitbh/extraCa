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
        self.driver.get("https://tide.com/en-us")                                     #launch website
        self.driver.save_screenshot("C:\Screenshot\homepage.jpg")                     #take a scrrenshot
        self.driver.find_element_by_xpath("//a[normalize-space()='Register']").click()      #Click on register
        parent = self.driver.current_window_handle
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign up now']").click()    #click on sign up
        child = self.driver.window_handles
        for childwindow in child:
            self.driver.switch_to.window(childwindow)
        self.driver.find_element_by_xpath("//button[normalize-space()='Log in']").click()   #click on log in
        self.driver.find_element_by_id("login-email").send_keys("rsamarth846@gmail.com")     #Enter the useremail
        self.driver.find_element_by_id("login-password").send_keys("Admin@123")              #Enter the Userpassword
        self.driver.find_element_by_xpath("//input[@value='LOG IN']").click()
        self.driver.save_screenshot("C:\Screenshot\loginpage.jpg")
        time.sleep(5)

    @pytest.fixture()
    def test_case2(self,setup,test_case1):
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Laundry Booster")      #Serach 1 product
        self.driver.save_screenshot("C:\Screenshot\page1.jpg")
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath("//a[@href='/en-us/shop/type/laundry-booster/tide-brights-and-whites-rescue"
                                          "']//p[contains(text(),'Tide')]") .click()                          #click on the product
        self.driver.find_element_by_css_selector("div[class='col-12 col-lg-3 right-column'] span["
                                                 "class='ps-button-label']").click()
        self.driver.find_element_by_xpath("//*[name()='path' and contains(@d,'M1230.15,1')]").click()
        self.driver.back()

    @pytest.fixture()
    def test_case3(self,setup,test_case1,test_case2):
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Powder")
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath("//button[normalize-space()='Products (6)']").click()
        self.driver.find_element_by_xpath("//a[@href='/en-us/shop/type/powder/tide-clean-breeze-powder']//p[contains("
                                          "text(),'Tide')]").click()
        self.driver.find_element_by_css_selector("div[class='col-12 col-lg-3 right-column'] div[aria-label='Tide "
                                                 "Clean Breeze Powder, shop now.']").click()
        self.driver.find_element_by_xpath("//*[name()='path' and contains(@d,'M1230.15,1')]").click()
        self.driver.back()

    @pytest.fixture()
    def test_case4(self,setup,test_case1,test_case2,test_case3):
        self.driver.find_element_by_xpath("//a[contains(text(),'What’s New')]").click()
        self.driver.find_element_by_xpath("//p[contains(text(),'Tide Hygienic Clean Heavy Duty 10X Free Power PODS')]").click()
        self.driver.back()

    @pytest.fixture()
    def test_case5(self,setup,test_case1,test_case2,test_case3,test_case4):
        wash = self.driver.find_element_by_xpath("//button[contains(@aria-label,'Open/Close submenu')][normalize-space()='How to Wash Clothes']")
        stain = self.driver.find_element_by_xpath("//a[contains(text(),'How to Remove Stains')]")
        actions = ActionChains(self.driver)
        actions.move_to_element(wash).move_to_element(stain).click().perform()
        self.driver.back()

    @pytest.fixture()
    def test_case6(self,setup,test_case1,test_case2,test_case3,test_case4,test_case5):
        our = self.driver.find_element_by_xpath("//button[contains(@aria-label,'Open/Close submenu')][normalize-space()='Our Commitment']")
        ambition = self.driver.find_element_by_xpath("//a[normalize-space()='Our Ambition']").click()
        actions = ActionChains(self.driver)
        actions.move_to_element(our).move_to_element(ambition).click().perform()
        self.driver.back()

    def test_case7(self,setup,test_case1,test_case2,test_case3,test_case4,test_case5,test_case6):
        self.driver.find_element_by_xpath("//a[contains(text(),'Contact Us')]").click()
        self.driver.find_element_by_id("j_id0:j_id1:j_id2:idForm:j_id598:j_id599:theSearchstring").send_keys(
            "Can Tide be used on baby clothes?"
        )
        self.driver.find_element_by_id("j_id0:j_id1:j_id2:idForm:j_id598:j_id599:theSearchstring").send_keys(Keys.ENTER  )







