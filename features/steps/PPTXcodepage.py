from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_xcode_xpath = "//*[@id='pills-xcode-tab']"
btn_newxcode_xpath = "//*[@id='collapseXcodeParent']/div[1]/button[1]"
btn_selectmodule_xpath = "//*[@id='drdXCodeModule']/option"
btn_clickchoosefile_xpath = "//*[@id='xcodepopImg1']"
click_xcodepicturepng_xpath = "//*[@id='xcodepopImg']"
btn_savexcode_xpath = "//*[@id='btn-add-xcode']"
btn_editxcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[7]/div[2]/div[1]/div/div[1]/div[1]/button[2]"
btn_saveedited_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[7]/div[3]/div/div/div[2]/div/button[2]"
btn_xcodedelete_xpath = "//*[@id='xcodd-73']"
btn_deletexcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[7]/div[2]/div[1]/div/div[1]/div[1]/button[4]"
btn_deletepopupxcode_xpath = "//*[@id='btn-delete-xcode']"
selectXcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[7]/div[2]/div[3]/div/div/div[2]/select/option[2]"
btn_copyxcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[7]/div[2]/div[1]/div/div[1]/div[1]/button[3]"
btn_savecopyxcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[7]/div[2]/div[3]/div/div/div[2]/div/button[1]"
btn_generalpropxcode_xpath = "//*[@id='spanxcodeProp']"


@then('navigate to Xcode Page')
def Xcode_path(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_xcode_xpath).click()


@then('Xcode Page should load successfully')
def verify_xcode(context):
    time.sleep(1)
    assert 'Xcode' in context.driver.page_source


@then('create new btn for xcode')
def new_xcode(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newxcode_xpath).click()


@then('Enter xcode name , customer code and description')
def set_xcode(context):
    rand_new_xcode = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewXcodeName").clear()
    context.driver.find_element(By.ID, "txtNewXcodeName").send_keys(rand_new_xcode)
    rand_new_xcodecustomerno = ''.join((random.choice('123456789') for i in range(2)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtXcodeCustomerId").clear()
    context.driver.find_element(By.ID, "txtXcodeCustomerId").send_keys(rand_new_xcodecustomerno)
    rand_new_xcodedesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtXcodeDescription").clear()
    context.driver.find_element(By.ID, "txtXcodeDescription").send_keys(rand_new_xcodedesc)


@then('select module which you want')
def set_module(context):
    time.sleep(1)
    element1 = context.driver.find_element(By.XPATH, "//*[@id='drdXCodeModule']")
    context.driver.execute_script("arguments[0].scrollIntoView();", element1)
    context.driver.find_element(By.XPATH, btn_selectmodule_xpath).click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, click_xcodepicturepng_xpath).send_keys("C:\\Users\\KnoDTec - Dheeraj\\Downloads\\Xcode_Module_img.png")


@then('click save for saving XCode')
def save_xcode(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_savexcode_xpath).click()


@then('New Xcode should be successfully created')
def step_impl(context):
    time.sleep(2)
    assert 'XCode Added successfully.' in context.driver.page_source


@then('verify the general properties of the xcode')
def step_impl(context):
    xCodeprop = context.driver.find_elements(By.XPATH, "//*[@id='spanxcodeProp']")
    expected = ['XCode Name', 'Customer ID', 'Description']
    contents = []
    for var in xCodeprop:
        contents.append(var.text)
    for expvar in expected:
        assert (expvar in contents[0]) is True


@then('click on edit btn of xcode')
def edit_xcode(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH,   btn_editxcode_xpath).click()


@then('Edit xcode name, customer no and description')
def set_editxcode(context):
    rand_edit_xcode = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewXcodeName1").clear()
    context.driver.find_element(By.ID, "txtNewXcodeName1").send_keys(rand_edit_xcode)

    rand_edit_xcodecustomerno = ''.join((random.choice('123456789') for i in range(2)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtXcodeCustomerId1").clear()
    context.driver.find_element(By.ID, "txtXcodeCustomerId1").send_keys(rand_edit_xcodecustomerno)

    rand_edit_xcodedesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtXcodeDescription1").clear()
    context.driver.find_element(By.ID, "txtXcodeDescription1").send_keys(rand_edit_xcodedesc)


@then('click on choose file')
def set_xcode(context):
    # time.sleep(2)
    # element2 = context.driver.find_element(By.XPATH, "//*[@id='xcodepopImg1']")
    # context.driver.execute_script("arguments[0].scrollIntoView();", element2)
    # context.driver.find_element(By.XPATH, btn_clickchoosefile_xpath).click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, click_xcodepicturepng_xpath).send_keys("C:\\Users\\KnoDTec - Dheeraj\\Downloads\\Xcode_Module_img.png")


@then('click save for saving Edited XCode')
def save_Editedxcode(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, btn_saveedited_xpath).click()


@then('Edited xcode should load successfully')
def verify_editedxcode(context):
    time.sleep(1)
    assert 'XCode Updated successfully.' in context.driver.page_source


@then('click on copy btn')
def copy_btn(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_copyxcode_xpath).click()


@then('select xcode from the list')
def select_xcode(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, selectXcode_xpath).click()


@then('Enter xcode and customer no and description')
def copy_xcodename(context):
    rand_edit_xcode = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtCopyXcodeName").clear()
    context.driver.find_element(By.ID, "txtCopyXcodeName").send_keys(rand_edit_xcode)
    rand_edit_xcodecustomerno = ''.join((random.choice('123456789') for i in range(2)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtCopyXcodeCustomerId").clear()
    context.driver.find_element(By.ID, "txtCopyXcodeCustomerId").send_keys(rand_edit_xcodecustomerno)
    rand_edit_xcodedesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtCopyXcodeDescription").clear()
    context.driver.find_element(By.ID, "txtCopyXcodeDescription").send_keys(rand_edit_xcodedesc)


@then('click save for saving Copied XCode')
def save_Copiedxcode(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_savecopyxcode_xpath).click()


@then('Xcode should be successfully copied')
def verify_copied(context):
    time.sleep(2)
    assert 'Added Successfully.' in context.driver.page_source


@then('click on delete btn to delete the xcode')
def delete_xcode(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletexcode_xpath).click()


@then('click on confirm delete btn to delete the xcode')
def confirm_delete(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_deletepopupxcode_xpath).click()


@then('verify that the xcode is deleted successfully')
def verify_deleted(context):
    time.sleep(2)
    assert 'Deleted Successfully.' in context.driver.page_source
