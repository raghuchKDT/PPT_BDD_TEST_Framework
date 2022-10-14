from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

UserManager_xpath = "//*[@id='four']"
btn_new_xpath = "//*[contains(text(),'New')]"
btn_save_xpath = "//*[contains(text(), 'Save')]"
btn_checkmark3_xpath = "//*[@id='tblUser']/tbody/tr[3]/td[1]/label/span"
btn_edit_xpath = "//*[contains(text(),'Edit')]"
btn_delete_xpath = "//*[contains(text(),'Delete')]"
btn_deletepopup_xpath = "//*[@id='btn-delete-user']"
btn_checkmark2_xpath = "//*[@id='tblUser']/tbody/tr[2]/td[1]/label/span"


@then('navigate to User Manager Page')
def user_manager(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, UserManager_xpath).click()


@then('verify the user manager Page')
def verify_usermanager(context):
    time.sleep(2)
    assert 'User Manager' in context.driver.page_source


@then('click on new btn in user manager')
def new_btn(context):
    context.driver.find_element(By.XPATH, btn_new_xpath).click()


@then('Enter username and password')
def new_user(context):
    rand_new_user = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    context.driver.find_element(By.ID, "userName").clear()
    context.driver.find_element(By.ID, "userName").send_keys(rand_new_user)
    rand_new_desc = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    context.driver.find_element(By.ID, "password").clear()
    context.driver.find_element(By.ID, "password").send_keys(rand_new_desc)


@then('click on save btn')
def save_btn(context):
    context.driver.find_element(By.XPATH, btn_save_xpath).click()


@then('user should be successfully created')
def verify_newuser(context):
    time.sleep(2)
    assert 'Updated Successfully.' in context.driver.page_source


@then('click on checkmark to edit the user')
def click_checkmark(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_checkmark3_xpath).click()


@then('click on edit btn in user')
def edit_btn(context):
    context.driver.find_element(By.XPATH, btn_edit_xpath).click()


@then('Edit username and password')
def edit_user(context):
    time.sleep(1)
    rand_edit_user = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    context.driver.find_element(By.ID, "userName").clear()
    context.driver.find_element(By.ID, "userName").send_keys(rand_edit_user)
    rand_edit_desc = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    context.driver.find_element(By.ID, "password").clear()
    context.driver.find_element(By.ID, "password").send_keys(rand_edit_desc)


@then('User should be edited successfully')
def verify_editeduser(context):
    time.sleep(1)
    assert 'Updated Successfully.' in context.driver.page_source


@then('click on checkmark to delete the user')
def checkmark(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkmark3_xpath).click()


@then('click on delete btn in user')
def delete_btn(context):
    context.driver.find_element(By.XPATH, btn_delete_xpath).click()


@then('User should be deleted successfully')
def verify_deleteduser(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletepopup_xpath).click()
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source


@then('Verify the headlines in user manager page')
def verify_levelmenus(context):
    time.sleep(2)
    assert 'User' in context.driver.page_source

    assert 'Access Level' in context.driver.page_source

    assert 'Access Section' in context.driver.page_source


@then('Verify the General Properties of user')
def verify_generalprop(context):
    context.driver.find_element(By.XPATH, btn_checkmark2_xpath).click()
    time.sleep(2)
    assert 'User Name' in context.driver.page_source

    assert 'Password' in context.driver.page_source

    assert 'Shift' in context.driver.page_source

    assert 'Access Level' in context.driver.page_source


@then('Verify web elements in access section present')
def verify_accessection(context):

    # Validation of User Management in Access Section
    expected_el = ['User Management']
    data_base_el = context.driver.find_elements(By.XPATH, "//*[@id='3']/label")
    print(len(data_base_el))
    for idx, base_el in enumerate(data_base_el):
        print(idx, base_el.text)
        assert (expected_el[idx] == base_el.text)

    # Validation of Info in Access Section
    expected_el1 = ['Info']
    data_base_el1 = context.driver.find_elements(By.XPATH, "//*[@id='1']/label")
    for idx, base_el1 in enumerate(data_base_el1):
        print(idx, base_el1.text)
        assert (expected_el1[idx] == base_el1.text)

    # Validation of Project in Access Section

    expected_el2 = ['Project']
    data_base_el2 = context.driver.find_elements(By.XPATH, "//*[@id='2']/label")
    for idx, base_el2 in enumerate(data_base_el2):
        print(idx, base_el2.text)
        assert (expected_el2[idx] == base_el2.text)

    # Validation of System in Access Section

    expected_el3 = ['System']
    data_base_el3 = context.driver.find_elements(By.XPATH, "//*[@id='6']/label")
    for idx, base_el3 in enumerate(data_base_el3):
        print(idx, base_el3.text)
        assert (expected_el3[idx] == base_el3.text)

    # Validation of Project (Web HMI) in Access Section

    expected_el4 = ['Project']
    data_base_el4 = context.driver.find_elements(By.XPATH, "//*[@id='5']/label")
    for idx, base_el4 in enumerate(data_base_el4):
        print(idx, base_el4.text)
        assert (expected_el4[idx] == base_el4.text)

    # Validation of Run Test (Web HMI) in Access Section

    expected_el5 = ['Run test']
    data_base_el5 = context.driver.find_elements(By.XPATH, "//*[@id='4']/label")
    for idx, base_el5 in enumerate(data_base_el5):
        print(idx, base_el5.text)
        assert (expected_el5[idx] == base_el5.text)

    # Validation of Report (Web HMI) in Access Section

    expected_el6 = ['Report']
    data_base_el6 = context.driver.find_elements(By.XPATH, "//*[@id='7']/label")
    for idx, base_el6 in enumerate(data_base_el6):
        print(idx, base_el6.text)
        assert (expected_el6[idx] == base_el6.text)

