from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_xcode_xpath = "//*[@id='pills-xcode-tab']"
btn_newxcode_xpath = "//*[@id='collapseXcodeParent']/div[1]/button[1]"
btn_selectmodule_xpath = "drdXCodeModule"
click_modulepicturepng_xpath = "//*[@id='xcodepopImg']"
btn_savexcode_xpath = "//*[@id='btn-add-xcode']"
btn_clickxcode_xpath = "//*[@id='xcodd-73']"
btn_editxcode_xpath = "//*[@id='btn-XEdit']"
btn_saveedited_xpath = "//*[@id='btn-add-xcode']"
btn_xcodedelete_xpath = "//*[@id='xcodd-73']"
btn_deletexcode_xpath = "//*[@id='btn-XDelete']"
btn_deletepopupxcode_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div/div/div[2]/div/button[2]"
btn_copyxcode_xpath = "//*[@id='btn-SaveAs']"
btn_selectxcode_xpath = "//*[@id='drdCopyXCode']"
btn_savecopyxcode_xpath = "//*[@id='btn-copy-xcode']"
btn_generalpropxcode_xpath = "//*[@id='xcodd-65']"


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
    context.driver.find_element(By.ID, btn_selectmodule_xpath).click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, click_modulepicturepng_xpath).send_keys("C:\\Users\\KnoDTec\\Downloads\\Picture.png")


@then('click save for creating')
def save_xcode(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_savexcode_xpath).click()


@then('New Xcode should be successfully created')
def step_impl(context):
    time.sleep(2)
    assert 'XCode Added successfully.' in context.driver.page_source


@then('click on xcode which you want to edit')
def click_xcode(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_clickxcode_xpath).click()


@then('click on edit btn of xcode')
def edit_xcode(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editxcode_xpath).click()


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


@then('Edit module and image')
def edit_modulepng(context):
    time.sleep(1)
    element1 = context.driver.find_element(By.XPATH, "//*[@id='xcodepopImg1']")
    context.driver.execute_script("arguments[0].scrollIntoView();", element1)
    context.driver.find_element(By.XPATH, click_modulepicturepng_xpath).send_keys("C:\\Users\\KnoDTec\\Downloads\\Picture.png")


@then('click on save btn to edit')
def save_edited(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_savexcode_xpath).click()


@then('Edited xcode should load successfully')
def verify_editedxcode(context):
    time.sleep(1)
    assert 'XCode Added successfully.' in context.driver.page_source


@then('click on copy btn')
def copy_btn(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_copyxcode_xpath).click()


@then('Select the xcode you want to copy')
def copy_xcode(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_selectxcode_xpath).click()


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


@then('Click on save btn to copy the xcode')
def save_copied(context):
    context.driver.find_element(By.XPATH, btn_savecopyxcode_xpath).click()


@then('Xcode should be successfully copied')
def verify_copied(context):
    time.sleep(1)
    assert 'Added Successfully.' in context.driver.page_source


@then('click on the xcode you want to delete')
def delete_xcode(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_xcodedelete_xpath).click()


@then('click on delete btn to delete the xcode')
def delete_xcode(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletexcode_xpath).click()


@then('verify that the xcode is deleted successfully')
def verify_deleted(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_deletepopupxcode_xpath).click()
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source


@then('click on xcode to see its general properties')
def gene_properties(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_generalpropxcode_xpath).click()


@then('verify the general properties of the xcode')
def step_impl(context):
    xCodeprop = context.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[4]/div/div/div[2]/div")
    expected = ['XCode Name', 'Customer ID', 'Description']
    contents = []
    for var in xCodeprop:
        contents.append(var.text)
    for expvar in expected:
        assert (expvar in contents[0]) is True