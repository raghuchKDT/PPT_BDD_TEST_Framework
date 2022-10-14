from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_rolepage_xpath = "//*[@id='pills-device-tab']"
btn_newrole_xpath = "//*[@id='bntGoToCreateRole']"
btn_saverole_xpath = "//*[@id='btn-roleSave']"
btn_checkbox3_xpath = "//*[@id='tblRole']/tbody/tr[3]/td[1]/label/span"
btn_editrole_xpath = "//*[@id='btn-roleEdit']"
btn_deleterole_xpath = "//*[@id='btn-roledelete']"
btn_popupdeleterole_xpath = "//*[@id='btn-delete-role']"


@then('navigate to role Page')
def role_page(context):
    context.driver.find_element(By.XPATH, btn_rolepage_xpath).click()


@then('Role page should successfully load')
def verify_rolepage(context):
    time.sleep(1)
    assert 'Role' in context.driver.page_source


@then('click on new btn for create new role')
def btn_newrole(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newrole_xpath).click()


@then('Enter Role name')
def set_newrolename(context):
    rand_new_role = ''.join((random.choice('aeiourtnsclp') for i in range(4)))
    context.driver.find_element(By.ID, "roleName").clear()
    context.driver.find_element(By.ID, "roleName").send_keys(rand_new_role)


@then('save the role by clicking save btn')
def click_save(context):
    context.driver.find_element(By.XPATH, btn_saverole_xpath).click()


@then('New role should be created successfully')
def verify_newrole(context):
    time.sleep(2)
    assert 'Updated Successfully.' in context.driver.page_source


@then('click on checkbox to edit the role')
def checkbox_edit(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox3_xpath).click()


@then('click on edit btn to edit role')
def click_edit_btn(context):
    context.driver.find_element(By.XPATH, btn_editrole_xpath).click()


@then('Edit Role name')
def set_editrole(context):
    rand_edit_role = ''.join((random.choice('aeiourtnsclp') for i in range(4)))
    time.sleep(1)
    context.driver.find_element(By.ID, "roleName").clear()
    context.driver.find_element(By.ID, "roleName").send_keys(rand_edit_role)


@then('role should be edited successfully')
def verify_editedrole(context):
    time.sleep(2)
    assert 'Updated Successfully.' in context.driver.page_source


@then('click on checkbox to delete the role')
def checkbox_delete(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox3_xpath).click()


@then('click on delete btn to delete role')
def click_deleterole(context):
    context.driver.find_element(By.XPATH, btn_deleterole_xpath).click()


@then('role should be successfully deleted')
def verify_deletedrole(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_popupdeleterole_xpath).click()
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source



