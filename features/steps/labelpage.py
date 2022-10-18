from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_project_xpath = "//*[@id='three']"
btn_label_xpath = "//*[@id='pills-label-tab']"
btn_newlabel_xpath = "//*[@id='bntGoToCreateLabel']"
btn_savelabel_xpath = "//*[@id='btn-labelSave']"
btn_checkbox2_xpath = "//*[@id='tblLabel']/tbody/tr[2]/td[1]/label/span"
btn_editlabel_xpath = "//*[@id='btn-LabelEdit']"
btn_deletelabel_xpath = "//*[@id='btn-labeldelete']"
btn_deletepopuplabel_xpath = "//*[@id='btn-delete-label']"


@then('navigate to Project Page')
def Project_xpath(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_project_xpath).click()


@then('navigate to Label Page')
def Label_xpath(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_label_xpath).click()


@then('Label page should successfully load')
def verify_labelpage(context):
    time.sleep(1)
    assert 'Label' in context.driver.page_source


@then('click on new btn for creating new label')
def new_label(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newlabel_xpath).click()


@then('Enter Label and description')
def set_newlabel(context):
    rand_new_label = ''.join((random.choice('aeiourtnsclp')for i in range(5)))
    context.driver.find_element(By.ID, "labelName").clear()
    context.driver.find_element(By.ID, "labelName").send_keys(rand_new_label)
    rand_new_labeldesc = ''.join((random.choice('testingthelabel') for i in range(5)))
    context.driver.find_element(By.ID, "reportDescription").clear()
    context.driver.find_element(By.ID, "reportDescription").send_keys(rand_new_labeldesc)


@then('click on save btn to save the label')
def save_label(context):
    context.driver.find_element(By.XPATH, btn_savelabel_xpath).click()


@then('Label should be created successfully')
def verify_newlabel(context):
    time.sleep(1)
    assert 'Updated Successfully.' in context.driver.page_source


@then('click on checkbox to edit label')
def checkbox_02_edit(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox2_xpath).click()


@then('click on edit btn to edit the label')
def edit_label(context):
    context.driver.find_element(By.XPATH, btn_editlabel_xpath).click()


@then('Edit Label and description')
def set_editlabel(context):
    rand_edit_label = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "labelName").clear()
    context.driver.find_element(By.ID, "labelName").send_keys(rand_edit_label)
    rand_edit_labeldesc = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    context.driver.find_element(By.ID, "reportDescription").clear()
    context.driver.find_element(By.ID, "reportDescription").send_keys(rand_edit_labeldesc)


@then('Label should be edited successfully')
def verify_editedlabel(context):
    time.sleep(1)
    assert 'Updated Successfully.' in context.driver.page_source


@then('click on checkbox to delete label')
def checkbox_delete(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox2_xpath).click()


@then('click on delete btn to delete the label')
def delete_label(context):
    context.driver.find_element(By.XPATH, btn_deletelabel_xpath).click()


@then('Label should be deleted successfully')
def verify_deletedlabel(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletepopuplabel_xpath).click()
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source


@then('verify the global variables in label page')
def global_variables(context):
    table = context.driver.find_element(By.ID, "tblLabelglobal")
    body = table.find_element(By.TAG_NAME, "tbody")
    cells = body.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text)

