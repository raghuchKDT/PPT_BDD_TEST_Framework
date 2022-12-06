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


@then('Verify web elements in access section present')
def verify_accessSection(context):

    # Validation of User Management in Access Section

    assert 'User Management' in context.driver.page_source

    # expected_el1 = ['User Management']
    # data_base_el1 = context.driver.find_elements(By.XPATH, "//*[@id='3']/label")
    # print(len(data_base_el1))
    # for idx, base_el1 in enumerate(data_base_el1):
    #     print(idx, base_el1.text)
    #     assert (expected_el1[idx] == base_el1.text)

    # Validation of Info in Access Section

    assert 'Info' in context.driver.page_source

    # expected_el2 = ['Info']
    # data_base_el2 = context.driver.find_elements(By.XPATH, "//*[@id='1']/label")
    # for idx, base_el2 in enumerate(data_base_el2):
    #     print(idx, base_el2.text)
    #     assert (expected_el2[idx] == base_el2.text)


    # Validation of Project in Access Section

    assert 'Project' in context.driver.page_source

    # expected_el3 = ['Project']
    # data_base_el3 = context.driver.find_elements(By.XPATH, "//*[@id='2']/label")
    # for idx, base_el3 in enumerate(data_base_el3):
    #     print(idx, base_el3.text)
    #     assert (expected_el3[idx] == base_el3.text)

    # Validation of System in Access Section

    assert 'System' in context.driver.page_source

    # expected_el4 = ['System']
    # data_base_el4 = context.driver.find_elements(By.XPATH, "//*[@id='6']/label")
    # for idx, base_el4 in enumerate(data_base_el4):
    #     print(idx, base_el4.text)
    #     assert (expected_el4[idx] == base_el4.text)

    # Validation of Report in Access Section

    assert 'Report' in context.driver.page_source

    # expected_el5 = ['Report']
    # data_base_el5 = context.driver.find_elements(By.XPATH, "//*[@id='7']/label")
    # for idx, base_el5 in enumerate(data_base_el5):
    #     print(idx, base_el5.text)
    #     assert (expected_el5[idx] == base_el5.text)

    # Validation of Project (Web HMI) in Access Section

    assert 'Project' in context.driver.page_source

    # expected_el6 = ['Project']
    # data_base_el6 = context.driver.find_elements(By.XPATH, "//*[@id='5']/label")
    # for idx, base_el6 in enumerate(data_base_el6):
    #     print(idx, base_el6.text)
    #     assert (expected_el6[idx] == base_el6.text)

    # Validation of Diagnostics (Web HMI) in Access Section

    assert 'Diagnostics' in context.driver.page_source

    # expected_el7 = ['Diagnostics']
    # data_base_el7 = context.driver.find_elements(By.XPATH, "//*[@id='8']/label")
    # for idx, base_el7 in enumerate(data_base_el7):
    #     print(idx, base_el7.text)
    #     assert (expected_el7[idx] == base_el7.text)


    # Validation of Settings (Web HMI) in Access Section

    assert 'Settings' in context.driver.page_source
    # expected_el8 = ['Settings']
    # data_base_el8 = context.driver.find_elements(By.XPATH, "//*[@id='4']/label")
    # for idx, base_el8 in enumerate(data_base_el8):
    #     print(idx, base_el8.text)
    #     assert (expected_el8[idx] == base_el8.text)
