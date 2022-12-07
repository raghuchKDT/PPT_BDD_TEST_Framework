from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import XLUtils

baseurl = "http://localhost:5003/"
PPT_logo_xpath = "//*[@id='layoutAuthentication_content']/main/div/div[1]/div/div/div/img"
btn_signin_xpath = "//*[contains(text(),'Sign in')]"
Infopage_xpath = "//*[@id='one']"
Recentproject_xpath = "//*[@id='pills-home-tab']"
Versionhis_xpath = "//*[@id='pills-profile-tab']"
Optionspage_xpath = "//*[@id='pills-contact-tab']"
text_ppt_xpath = "/html/body/nav/a/span"
btn_logout_xpath = "//*[@id='userDropdown']"
btn_out_xpath = "//*[@id='adminicon']/ul/li/div/a"


@given('I launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    time.sleep(1)


@when('I open PushPullTouch homepage')
def open_homepage(context):
    time.sleep(1)
    context.driver.get(baseurl)


@then('Verify that the logo present on the page')
def verify_logo(context):
    time.sleep(1)
    status = context.driver.find_element(By.XPATH, PPT_logo_xpath).is_displayed()
    assert status is True


@when('Enter username "{username}" and password "{pwd}"')
def login_credentials(context, username, pwd):
    context.driver.find_element(By.ID, "UserName").send_keys(username)
    context.driver.find_element(By.ID, "Password").send_keys(pwd)


@when('click on Sign In button')
def sign_in(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_signin_xpath).click()


@then('User must successfully login to PPT webpage')
def login_page(context):
    time.sleep(1)
    try:
        title = context.driver.find_element(By.XPATH, text_ppt_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"

    title = context.driver.title
    if title == "komax Testing":
        assert True
    else:
        assert False


@then('Verify the Info Page in PPT')
def Info_page(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, Infopage_xpath)
    assert 'Info' in context.driver.page_source


@then('Info Page should have recent project')
def recent_projectpage(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, Recentproject_xpath).click()


@then('verify recent project page contents')
def verification_projectcontents(context):
    table = context.driver.find_element(By.ID, "tblProject")
    body = table.find_element(By.TAG_NAME, "tbody")
    cells = body.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text)


@then('Verify the version history in Info Page')
def version_history(context):
    context.driver.find_element(By.XPATH, Versionhis_xpath).click()
    time.sleep(2)
    assert 'Version History' in context.driver.page_source


@then('Verify the contents on version history webpage')
def ver_hiscontents(context):
    expected_Ver1 = ['Name', 'Version', 'Released Date', 'Licence']
    data_base_Ver1 = context.driver.find_elements(By.XPATH, "//*[@id='layoutSidenav_content']/main/div[3]/div/div")
    for idx, base_Ver1 in enumerate(data_base_Ver1):
        print(idx, base_Ver1.text)
        assert (expected_Ver1[idx] == base_Ver1.text)


@then('Verify the Options page in Info page')
def options_page(context):
    context.driver.find_element(By.XPATH, Optionspage_xpath).click()
    time.sleep(2)
    assert 'Options' in context.driver.page_source


@then('Verify the contents in options page')
def option_contents(context):
    time.sleep(1)
    assert 'Software options installed' in context.driver.page_source
    time.sleep(2)
    assert 'Graphic setup' in context.driver.page_source


@then('Read the data from the excel sheet')
def multiple_user(context):
    path = "C:\Downloads\selenium_BDD.xlsx"

    rows = XLUtils.getRowCount(path, 'Sheet1')

    for r in range(2, rows + 1):
        username = XLUtils.readData(path, "Sheet1", r, 1)
        password = XLUtils.readData(path, "Sheet1", r, 2)

        context.driver.find_element(By.ID, "UserName").clear()
        context.driver.find_element(By.ID, "UserName").send_keys(username)

        time.sleep(2)
        context.driver.find_element(By.ID, "Password").clear()
        context.driver.find_element(By.ID, "Password").send_keys(password)

        time.sleep(1)
        context.driver.find_element(By.XPATH, btn_signin_xpath).click()

        if context.driver.title=="komax Testing":
            print("login successfull")
            time.sleep(2)
            XLUtils.writeData(path, "Sheet1", r, 3, "login successfull")
        else:
            print("test failed")
            time.sleep(2)
            XLUtils.writeData(path, "Sheet1", r, 3, "test failed")

        context.driver.find_element(By.XPATH, btn_logout_xpath).click()
        time.sleep(1)
        context.driver.find_element(By.XPATH, btn_out_xpath).click()