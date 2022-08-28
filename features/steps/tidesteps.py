from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("C:\driver\chromedriver.exe")


@when('I open Tide Homepage')
def openHomePage(context):
    context.driver.get("https://tide.com/en-us/sign-in")


@when('Click On Register')
def clickOnRegister(context):
    context.driver.find_element_by_xpath("//a[normalize-space()='Register']").click()


@when('Click On Sign Up Now')
def clickOnSignUp(context):
    context.driver.find_element_by_xpath("//a[normalize-space()='Sign up now']").click()


@when('Enter firstname "{name}" and email "{mail} and password"{pwd}')
def step_impl(context, name, mail, pwd):
    context.driver.find_element_by_id("name").send_keys("Rohit")
    context.driver.find_element_by_id("email").send_keys("rohitbhagat7865@gmail.com")
    context.driver.find_element_by_id("password").send_keys("admin@123")


@when('Click on create account')
def createAccount(context):
    context.driver.find_element_by_xpath("//input[@value='CREATE ACCOUNT']").click()


@when('User must Thanks for signing up!')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//p[normalize-space()='Thanks for signing up!']").text()
    context.driver.close()


@when('click on Log in')
def step_impl(context):
    context.driver.find_element_by_xpath("//button[normalize-space()='Log in']").click()


@when('Enter "Username and Password')
def step_impl(context):
    context.driver.find_element_by_id("login-email").send_keys("rsamarth846@gmail.com")
    context.driver.find_element_by_id("login-password").send_keys("Admin@123")


@when('Click on Log in')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@value='LOG IN']").click()


@given('Click on search box')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@placeholder='Search']").click()


@when('Enter Product Name')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Laundry Booster")


@when('Click on search Box')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.ENTER)


@when('Click on the Product')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@href='/en-us/shop/type/laundry-booster/tide-brights-and-whites-rescue"
                                         "']//p[contains(text(),'Tide')]").click()


@when('click on the retailers')
def step_impl(context):
    context.driver.find_element_by_css_selector("div[class='col-12 col-lg-3 right-column'] span["
                                                "class='ps-button-label']").click()


@when('Click on search box')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Powder")
    context.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.ENTER)


@when('Click on Product')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@href='/en-us/shop/type/powder/tide-clean-breeze-powder']//p[contains("
                                         "text(),'Tide')]").click()


@when('Click on retailers')
def step_impl(context):
    context.driver.find_element_by_css_selector("div[class='col-12 col-lg-3 right-column'] div[aria-label='Tide "
                                                 "Clean Breeze Powder, shop now.']").click()


@given('Click on Whats new')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'What’s New')]").click()


@when('Click on product')
def step_impl(context):
    context.driver.find_element_by_xpath("//p[contains(text(),'Tide Hygienic Clean Heavy Duty 10X Free Power PODS')]").click()


@when('Back to home page')
def step_impl(context):
    context.driver.back()


@given('Click on how to wash cloth')
def step_impl(context):
    wash = context.driver.find_element_by_xpath(
        "//button[contains(@aria-label,'Open/Close submenu')][normalize-space()='How to Wash Clothes']")
    actions = ActionChains(context.driver)
    actions.move_to_element(wash).click().perform()


@when('Click on how to remove stains')
def step_impl(context):
    stain = context.driver.find_element_by_xpath("//a[contains(text(),'How to Remove Stains')]")
    actions = ActionChains(context.driver)
    actions.move_to_element(stain).click().perform()
    context.driver.back()


@given('Click on Our Commitment')
def step_impl(context):
    our = context.driver.find_element_by_xpath(
        "//button[contains(@aria-label,'Open/Close submenu')][normalize-space()='Our Commitment']")

    actions = ActionChains(context.driver)
    actions.move_to_element(our).click().perform()


@when('Click on Our ambition')
def step_impl(context):
    ambition = context.driver.find_element_by_xpath("//a[normalize-space()='Our Ambition']").click()
    actions = ActionChains(context.driver)
    actions.move_to_element(ambition).click().perform()

@when('Go to home page')
def step_impl(context):
    context.driver.back()


@given(u'Click on Contact Us')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Contact Us')]").click()


@when('Click on Type here for answer ask your question')
def step_impl(context):
   context.driver.find_element_by_id("j_id0:j_id1:j_id2:idForm:j_id598:j_id599:theSearchstring").send_keys(
            "Can Tide be used on baby clothes?"
        )
@when('Click on search box')
def step_impl(context):
    context.driver.find_element_by_id("j_id0:j_id1:j_id2:idForm:j_id598:j_id599:theSearchstring").send_keys(Keys.ENTER)