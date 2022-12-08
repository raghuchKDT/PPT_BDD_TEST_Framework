from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import openpyxl
import XLUtils


UserManager_xpath = "//*[@id='four']/span"
btn_new_xpath = "//*[contains(text(),'New')]"
btn_save_xpath = "//*[contains(text(), 'Save')]"
btn_checkmark2_xpath = "//*[@id='tblUser']/tbody/tr[2]/td[1]/label/span"
btn_edit_xpath = "//*[contains(text(),'Edit')]"
btn_delete_xpath = "//*[@id='btn-userdelete']"
btn_deletepopup_xpath = "//*[@id='btn-delete-user']"
user_info_path = "features/Data Driven Reports/user_info.xlsx"


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
    context.driver.find_element(By.XPATH, btn_checkmark2_xpath).click()


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
    context.driver.find_element(By.XPATH, btn_checkmark2_xpath).click()


@then('click on delete btn in user')
def delete_btn(context):
    context.driver.find_element(By.XPATH, btn_delete_xpath).click()


@then('click on confirm delete btn in user')
def delete_btn(context):
    context.driver.find_element(By.XPATH, btn_deletepopup_xpath).click()


@then('User should be deleted successfully')
def verify_deleteduser(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletepopup_xpath).click()
    time.sleep(3)
    assert 'Deleted Successfully.' in context.driver.page_source


@then('Verify the headlines in user manager page')
def verify_levelmenus(context):
    time.sleep(2)
    assert 'User' in context.driver.page_source


@then('Verify the General Properties of user')
def verify_generalprop(context):
    context.driver.find_element(By.XPATH, btn_checkmark2_xpath).click()
    time.sleep(2)
    assert 'User Name' in context.driver.page_source

    assert 'Password' in context.driver.page_source

    assert 'Shift' in context.driver.page_source

    assert 'Access Level' in context.driver.page_source




@then('Get the data from the excel')
def get_data(context):

   path = user_info_path

   rows = XLUtils.getRowCount(path, 'Sheet1')

   for r in range(2, rows+1):
       username = XLUtils.readData(path, "Sheet1", r, 1)
       password = XLUtils.readData(path, "Sheet1", r, 2)

       context.driver.find_element(By.ID, "userName").clear()
       time.sleep(1)
       context.driver.find_element(By.ID, "userName").send_keys(username)
       time.sleep(1)
       context.driver.find_element(By.ID, "password").clear()
       time.sleep(1)
       context.driver.find_element(By.ID, "password").send_keys(password)

       context.driver.find_element(By.XPATH, btn_save_xpath).click()

       if context.driver.page_source=="Updated Successfully.":
           print("created successfully")
           time.sleep(2)
           XLUtils.writeData(path, "Sheet1", r, 3, "created successfully")
       else:
           print("test failed")
           time.sleep(2)
           XLUtils.writeData(path, "Sheet1", r, 4, "test failed")

       context.driver.find_element(By.XPATH, btn_new_xpath).click()