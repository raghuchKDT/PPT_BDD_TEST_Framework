from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_switch_xpath = "//*[@id='pills-switch-tab']"
btn_newswitch_xpath = "//*[@id='bntGoToCreateSwicth']"
btn_saveswitch_xpath = "//*[@id='btn-switchSave']"
btn_checkbox02_xpath = "//*[@id='tblswitch']/tbody/tr/td[1]/label/span"
btn_deleteswitch_xpath = "//*[@id='btn-switchdelete']"
btn_deletepopupswitch_xpath = "//*[@id='btn-delete-switch']"
btn_editbtn_xpath = "//*[@id='btn-switchEdit']"


@then('navigate to switch page')
def switch_page(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_switch_xpath).click()


@then('Switch Page should load successfully')
def Verify_switchscreen(context):
    time.sleep(1)
    assert 'Switch' in context.driver.page_source


@then('click on new btn for new switch')
def new_switch(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newswitch_xpath).click()


@then('Enter switch name')
def set_newswitch(context):
    rand_new_switch = ''.join((random.choice('aeiourtnsclp') for i in range(6)))
    context.driver.find_element(By.ID, "switchGroup").clear()
    context.driver.find_element(By.ID, "switchGroup").send_keys(rand_new_switch)


@then('click on save')
def save_switch(context):
    context.driver.find_element(By.XPATH, btn_saveswitch_xpath).click()


@then('New switch should be created successfully')
def verify_newswitch(context):
    time.sleep(1)
    assert 'Updated Successfully.' in context.driver.page_source


@then('click on checkbox of switch')
def checkbox02(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox02_xpath).click()


@then('Edit switch name')
def step_impl(context):
    rand_edit_switch = ''.join((random.choice('aeiourtnsclp') for i in range(6)))
    context.driver.find_element(By.ID, "switchGroup").clear()
    context.driver.find_element(By.ID, "switchGroup").send_keys(rand_edit_switch)


@then('switch should be edited successfully')
def verify_editedswitch(context):
    time.sleep(1)
    assert 'Updated Successfully.' in context.driver.page_source


@then('click on delete btn for deleting the switch')
def delete_switch(context):
    context.driver.find_element(By.XPATH, btn_deleteswitch_xpath).click()


@then('switch should be deleted successfully')
def verify_deletedswitch(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletepopupswitch_xpath).click()


@then('click on Edit btn for editing switch')
def editbtn_switch(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editbtn_xpath).click()