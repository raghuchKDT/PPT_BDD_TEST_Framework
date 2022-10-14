from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_variable_xpath = "//*[@id='pills-variantglobalvar-tab']"


@then('navigate to Variable Page')
def variable_Screen(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_variable_xpath).click()


@then('Variable Page should load successfully')
def verify_variablescreen(context):
    time.sleep(1)
    assert 'Variable' in context.driver.page_source


@then('Verify the data present in variable page')
def variable_dynamicdata(context):
    time.sleep(1)
    table = context.driver.find_element(By.ID, "tblVariantGlobalVar")
    body = table.find_element(By.TAG_NAME, "tbody")
    cells = body.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text)

