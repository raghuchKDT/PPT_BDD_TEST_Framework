from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_variant_linktext = "Variant"
btn_newvariant_xpath = "//*[@id='bntGoToCreateVariant']"
btn_savevariant_xpath = "//*[@id='btn-VarSave']"
btn_checkboxvar_xpath = ""


@then('navigate to Variant page')
def variant_page(context):
    context.driver.find_element(By.LINK_TEXT, btn_variant_linktext).click()


@then('Verify that variant page and explorer page are loaded')
def verify_page(context):
    time.sleep(1)
    assert 'Variant' in context.driver.page_source
    assert 'Explorer' in context.driver.page_source


@then('click on new btn to create variant')
def new_btnvariant(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newvariant_xpath).click()


@then('enter the variant name and description')
def set_newvariant(context):
    rand_new_variant = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "varName").clear()
    context.driver.find_element(By.ID, "varName").send_keys(rand_new_variant)
    rand_new_variantdesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "varDesc").clear()
    context.driver.find_element(By.ID, "varDesc").send_keys(rand_new_variantdesc)


@then('click on save btn variant')
def save_variant(context):
    context.driver.find_element(By.XPATH, btn_savevariant_xpath).click()


@then('New variant should be created successfully')
def verify_variant(context):
    time.sleep(2)
    assert 'Updated Successfully.' in context.driver.page_source


@then('select the checkbox')
def checkbox_variant(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkboxvar_xpath).click()


@then('click on edit btn variant')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then click on edit btn variant')


@then('edit the variant name and description')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then edit the variant name and description')


@then('Variant should be edited successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Variant should be edited successfully')


@then('click on copy btn variant')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then click on copy btn variant')


@then(u'enter variant name and desc')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then enter variant name and desc')


@then(u'click on save btn to copy the changes')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then click on save btn to copy the changes')


@then('variant should be copied successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then variant should be copied successfully')


@then('click on delete btn variant')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then click on delete btn variant')


@then('Verify that the variant is deleted successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify that the variant is deleted successfully')


@then('Verify the general properties of the variant')
def General_properties(context):
    time.sleep(1)
    Varprop = context.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div[2]/div[2]/div[1]/div/div[3]/div[1]")
    print(len(Varprop))
    expected = ['Variant Name', 'Description', 'Date Created']
    contents = []
    for var in Varprop:
        contents.append(var.text)
    for expvar in expected:
        assert (expvar in contents[0]) == True
