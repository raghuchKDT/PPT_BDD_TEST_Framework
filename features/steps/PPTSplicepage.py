from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_Splice_xpath = "//*[@id='pills-splice-tab']"
btn_newsplice_xpath = "//*[@id='bntGoToCreateSplice']"
btn_savesplice_xpath = "//*[@id='btn-spliceSave']"
btn_checkbox01splice_xpath = "//*[@id='tblSplice']/tbody/tr[1]/td[1]/label/span"
btn_editsplice_xpath = "//*[@id='btn-spliceEdit']"
btn_Savespliceedited_xpath = "//*[@id='btn-spliceSave']"
btn_copysplice_xpath = "//*[@id='btn-SpliceSaveAs']"
btn_savecopysplice_xpath = "//*[@id='btn-saveas-splice']"
btn_deletedplice_xpath = "//*[@id='btn-splicedelete']"
btn_popupdeletesplice_xpath = "//*[@id='btn-delete-splice']"


@then('navigate to Splice Page')
def splice_screen(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_Splice_xpath).click()


@then('Splice Page should load successfully')
def verify_Splicescreen(context):
    time.sleep(1)
    assert 'Splice' in context.driver.page_source


@then('click on new btn for creating splice')
def New_Splice(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newsplice_xpath).click()


@then('Enter the splice name')
def set_newsplice(context):
    rand_new_splice = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "spliceName").clear()
    context.driver.find_element(By.ID, "spliceName").send_keys(rand_new_splice)


@then('click on save for saving splice name')
def save_newsplice(context):
    context.driver.find_element(By.XPATH, btn_savesplice_xpath).click()


@then('New Splice should be created successfully')
def verify_newsplice(context):
    time.sleep(1)
    assert 'Data Added Successfully.' in context.driver.page_source


@then('click on checkbox which you want to edit')
def splice_checkbox1(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox01splice_xpath).click()


@then('click on edit btn of splice')
def edit_Splice(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editsplice_xpath).click()


@then('Edit the splice name')
def edit_splicename(context):
    rand_edit_splice = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "spliceName").clear()
    context.driver.find_element(By.ID, "spliceName").send_keys(rand_edit_splice)


@then('click on save of splice')
def save_editedsplice(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_Savespliceedited_xpath).click()


@then('Edited splice should load successfully')
def verify_editedsplice(context):
    time.sleep(1)
    assert 'Data Added Successfully.' in context.driver.page_source


@then('click on checkbox which you want to copy')
def checkbox_01(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox01splice_xpath).click()


@then('click on copy btn of splice')
def copy_splice(context):
    context.driver.find_element(By.XPATH, btn_copysplice_xpath).click()


@then('enter the name of splice')
def set_copysplicename(context):
    rand_copy_splice = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewSpliceName").clear()
    context.driver.find_element(By.ID, "txtNewSpliceName").send_keys(rand_copy_splice)


@then('click on save btn splice')
def save_Copiedsplice(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_savecopysplice_xpath).click()


@then('copied splice should load successfully')
def verify_copiedsplice(context):
    time.sleep(1)
    assert 'Data Added Successfully.' in context.driver.page_source


@then('click on checkbox which you want to delete')
def checkbox_deletesplice(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox01splice_xpath).click()


@then('click on delete btn of splice')
def delete_splice(context):
    context.driver.find_element(By.XPATH, btn_deletedplice_xpath).click()


@then('Verify that the splice is deleted successfully')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_popupdeletesplice_xpath).click()
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source