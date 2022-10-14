from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_pick2light_xpath = "//*[@id='pills-tab']/li[3]/a"
btn_newp2l_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/div[2]/div/button[1]"
btn_save_picktolight = "/html/body/div[1]/div[2]/main/div[4]/div/div/div[2]/div/button[2]"
btn_picktolight_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/span[1]/div/ul/li[5]/a/h6"
btn_editpicktolight_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/div[2]/div/button[2]"
btn_editsave_xpath = "/html/body/div[1]/div[2]/main/div[6]/div/div/div[2]/div/button[2]"
btn_copyptl_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/span[1]/div/ul/li[5]/a/h6"
btn_copy_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/div[2]/div/button[3]"
btn_savecopy_xpath = "/html/body/div[1]/div[2]/main/div[5]/div/div/div[2]/div/button[2]"
btn_deleteptl_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/span[1]/div/ul/li[2]/a/h6"
btn_deleteclick_xpath = "/html/body/div[1]/div[2]/main/div[3]/div/div[4]/div/div/div[1]/div[2]/div/button[4]"
btn_clickptl_xpath = "//*[@id='modd-35']/a/h6"


@then('navigate to Pick to Light page')
def pick2light(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_pick2light_xpath).click()


@then('Pick to Light Page should load successfully')
def verify_screen(context):
    time.sleep(1)
    assert 'Pick To Light' in context.driver.page_source


@then('click on new btn for p2l')
def new_picktolight(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_newp2l_xpath).click()


@then('Enter picktolight name and description')
def set_picktolight(context):
    rand_new_picktolight = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewPickToLight").clear()
    context.driver.find_element(By.ID, "txtNewPickToLight").send_keys(rand_new_picktolight)
    rand_new_picktolightdesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtPickToLightDescription").clear()
    context.driver.find_element(By.ID, "txtPickToLightDescription").send_keys(rand_new_picktolightdesc)


@then('Enter number of LED')
def new_LEDno(context):
    time.sleep(1)
    rand_newLED_no = ''.join((random.choice('12345678') for i in range(1)))
    context.driver.find_element(By.ID, "txtLightLed").clear()
    context.driver.find_element(By.ID, "txtLightLed").send_keys(rand_newLED_no)


@then('click on save btn p2l')
def save_picktolight(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_save_picktolight).click()


@then('pick to light should be created successfully')
def verify_pick2light(context):
    time.sleep(1)
    assert 'Pick To Light Added successfully.' in context.driver.page_source


@then('click on pick to light you want to edit')
def pick_tolight(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_picktolight_xpath).click()


@then('click on edit btn of pick to light')
def edit_p2l(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editpicktolight_xpath).click()


@then('edit the p2l and description')
def set_editp2l(context):
    rand_edit_picktolight = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtPickName").clear()
    context.driver.find_element(By.ID, "txtPickName").send_keys(rand_edit_picktolight)
    rand_edit_picktolightdesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtPickDesc").clear()
    context.driver.find_element(By.ID, "txtPickDesc").send_keys(rand_edit_picktolightdesc)


@then('Edit no of led')
def edit_LED(context):
    time.sleep(1)
    rand_editLED_no = ''.join((random.choice('12345678') for i in range(1)))
    context.driver.find_element(By.ID, "txtPickNum").clear()
    context.driver.find_element(By.ID, "txtPickNum").send_keys(rand_editLED_no)


@then('Pick to Light should be edited successfully')
def verify_edited(context):
    time.sleep(1)
    assert 'Pick To Light Updated successfully.' in context.driver.page_source


@then('click on save btn to save edited p2l')
def save_Edited(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editsave_xpath).click()


@then('click on pick to light you want to copy')
def copy_ptl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_copyptl_xpath).click()


@then('click on copy btn to copy')
def btn_copy(context):
    context.driver.find_element(By.XPATH, btn_copy_xpath).click()


@then('enter picktolight name and description for copying')
def set_copyptl(context):
    rand_copy_picktolight = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtCopyNewPickToLight").clear()
    context.driver.find_element(By.ID, "txtCopyNewPickToLight").send_keys(rand_copy_picktolight)
    rand_copy_picktolightdesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtCopyPickToLightDescription").clear()
    context.driver.find_element(By.ID, "txtCopyPickToLightDescription").send_keys(rand_copy_picktolightdesc)


@then('click on save btn to save the copied ptl')
def save_copyptl(context):
    context.driver.find_element(By.XPATH, btn_savecopy_xpath).click()


@then('Pick to Light should be copied successfully')
def verified_copied(context):
    time.sleep(1)
    assert 'Added Successfully.' in context.driver.page_source


@then('select ptl which you want to delete')
def delete_ptl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deleteptl_xpath).click()


@then('click on delete btn')
def delete_btn(context):
    context.driver.find_element(By.XPATH, btn_deleteclick_xpath).click()


@then('verify that the ptl is deleted successfully')
def verify_deleted(context):
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source


@then('click on pick to light to check its general properties')
def click_generalprop(context):
   time.sleep(1)
   context.driver.find_element(By.XPATH, btn_clickptl_xpath).click()


@then('verify the general properties')
def verify_generalproperties(context):
    time.sleep(2)
    assert 'Description' in context.driver.page_source

    assert 'Pick to Light LED No' in context.driver.page_source

