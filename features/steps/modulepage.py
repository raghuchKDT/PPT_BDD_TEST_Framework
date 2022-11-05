from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_module_link_text = "Module"
btn_newmodule_xpath = "//*[@id='deChk2']/div[2]/div/button[1]"
click_modulepicture_xpath = "//*[@id='modImg']"
btn_save_module = "//*[@id='btn-add-module']"
txt_moduleselect_xpath = "//*[contains(text(),'itaer')]"
btn_deletemodule_xpath = "//*[@id='btn-DeleteModule']"
btn_module_xpath = "//*[contains(text(),'Xcode-20')]"
btn_deletepopup_xpath = "//*[@id='btn-delete-module']"
btn_savecopymodule_xpath = "//*[@id='btn-copy-module']"
btn_generalprop_xpath = "//*[contains(text(),'Xcode-20')]"
btn_copimodule_xpath = "//*[@id='btn-SaveAs']"
module_image_path = "C:\\Downloads\\module.png"


@then('navigate to Module page')
def module_page(context):
    context.driver.find_element(By.LINK_TEXT, btn_module_link_text).click()
    time.sleep(3)


@then('Module Page should load successfully')
def step_impl(context):
    time.sleep(2)
    assert 'Module' in context.driver.page_source


@then('click on new btn for new module')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newmodule_xpath).click()


@then('Enter Module Name and description')
def set_newmodule(context):
    rand_new_module = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewModule").clear()
    context.driver.find_element(By.ID, "txtNewModule").send_keys(rand_new_module)
    rand_new_moduledesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtModuleDescription").clear()
    context.driver.find_element(By.ID, "txtModuleDescription").send_keys(rand_new_moduledesc)


@then('Enter no of cavity and no of switch')
def set_cavity_switch(context):
    time.sleep(1)
    rand_newcavity_no = ''.join((random.choice('12345678') for i in range(1)))
    context.driver.find_element(By.ID, "txtCavity").clear()
    context.driver.find_element(By.ID, "txtCavity").send_keys(rand_newcavity_no)
    rand_newswitch_no = ''.join((random.choice('12345678') for i in range(1)))
    context.driver.find_element(By.ID, "txtSwitch").clear()
    context.driver.find_element(By.ID, "txtSwitch").send_keys(rand_newswitch_no)


@then('Enter cavity LED no and choose a png file from the folder')
def set_LED_picture(context):
    rand_newcavityled_no = ''.join((random.choice('12345678') for i in range(1)))
    context.driver.find_element(By.ID, "txtCavityLed").clear()
    context.driver.find_element(By.ID, "txtCavityLed").send_keys(rand_newcavityled_no)
    time.sleep(1)
    element = context.driver.find_element(By.XPATH, "//*[@id='modImg']")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    context.driver.find_element(By.XPATH, click_modulepicture_xpath).send_keys(module_image_path)


@then('click on save btn in module')
def save_btn(context):
    context.driver.find_element(By.XPATH, btn_save_module).click()


@then('Module should be created successfully')
def verify_module(context):
    time.sleep(1)
    assert 'Module Added successfully.' in context.driver.page_source


@then('click on the module you want to delete')
def delete_module(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, txt_moduleselect_xpath).click()


@then('click on delete btn to delete module')
def delete_btn(context):
    context.driver.find_element(By.XPATH, btn_deletemodule_xpath).click()


@then('Module should successfully be deleted')
def verify_deletedmodule(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletepopup_xpath).click()
    time.sleep(1)
    assert 'Module deleted successfully.' in context.driver.page_source


@then('click on module which you want to copy')
def copy_module(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_module_xpath).click()


@then('click on save btn to copy the module')
def save_copymodule(context):
    context.driver.find_element(By.XPATH, btn_savecopymodule_xpath).click()


@then('click on module which you want to see general properties')
def general_prop(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_generalprop_xpath).click()


@then('General properties of the module should be displayed')
def verify_generalprop(context):
    time.sleep(1)
    # expected_el1 = ['Description', 'Module Board COMM Pin', 'Number of Cavity', 'Number of Switch', 'Module Cavity LED No']
    # data_base_el1 = context.driver.find_elements(By.XPATH, "//*[@id='collapseSysDescBelow']/div/div")
    # time.sleep(1)
    # for idx, base_el1 in enumerate(data_base_el1):
    #     assert (expected_el1[idx] == base_el1.text)
    assert 'Description' in context.driver.page_source

    assert 'Module Board COMM Pin' in context.driver.page_source

    time.sleep(1)
    assert 'Number of Cavity' in context.driver.page_source

    assert 'Number of Switch' in context.driver.page_source

    time.sleep(1)
    assert 'Module Cavity LED No' in context.driver.page_source


@then('Enter Module Name and description to copy')
def set_copymodule(context):
    rand_copy_module = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    context.driver.find_element(By.ID, "txtCopyNewModule").clear()
    context.driver.find_element(By.ID, "txtCopyNewModule").send_keys(rand_copy_module)
    rand_copy_moduledesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    context.driver.find_element(By.ID, "txtCopyModuleDescription").clear()
    context.driver.find_element(By.ID, "txtCopyModuleDescription").send_keys(rand_copy_moduledesc)


@then('click on copy btn to copy module')
def copy_btn(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_copimodule_xpath).click()