from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_workflow_xpath = "//*[@id='pills-workflow-tab']"
btn_neworkflow_xpath = "//*[@id='bntGoToCreateWorkflow']"
btn_saveworkflow_xpath = "//*[@id='btn-WorkSave']"
btn_checkbox2_xpath = "//*[@id='tblWorkflow']/tbody/tr[2]/td[1]/label/span"
btn_editworkflow_xpath = "//*[@id='btn-WorkEdit']"
btn_deleteworkflow_xpath = "//*[@id='btn-Workdelete']"
btn_deletepopupworkflow_xpath = "//*[@id='btn-delete-workflow']"
btn_checkbox1_xpath = "//*[@id='tblWorkflow']/tbody/tr[1]/td[1]/label/span"


@then('navigate to workflow Page')
def workflow_xpath(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_workflow_xpath).click()


@when('navigate to workflow Page')
def workflow_xpath(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_workflow_xpath).click()


@then('Workflow page should successfully load')
def verify_workflowpage(context):
    time.sleep(1)
    assert 'Workflow' in context.driver.page_source


@then('click on new btn for new workflow')
def new_workflow(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_neworkflow_xpath).click()


@then('Save the workflow')
def save_workflow(context):
    context.driver.find_element(By.XPATH, btn_saveworkflow_xpath).click()


@then('New workflow should be created successfully')
def verify_newworkflow(context):
    time.sleep(1)
    assert 'Data Added Successfully.' in context.driver.page_source


@then('click on checkbox of one of the workflow')
def checkbox_03(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox2_xpath).click()


@then('click on Edit btn for editing')
def edit_workflow(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editworkflow_xpath).click()


@then('Workflow should be edited successfully')
def edit_workflow(context):
    time.sleep(2)
    assert 'Data Added Successfully.' in context.driver.page_source


@then('click on delete btn for deleting the workflow')
def delete_workflow(context):
    context.driver.find_element(By.XPATH, btn_deleteworkflow_xpath).click()


@then('workflow should successfully delete')
def verify_deletedworkflow(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletepopupworkflow_xpath).click()
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source


@then('click on checkbox to verify general properties')
def checkbox_generalprop(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox1_xpath).click()


@then('General Properties should be displayed')
def general_prop(context):
    time.sleep(1)
    assert 'Name' in context.driver.page_source
    assert 'Description' in context.driver.page_source


@then('Enter Workflow and description')
def set_newworkflow(context):
    rand_new_workflow = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    context.driver.find_element(By.ID, "workflowName").clear()
    context.driver.find_element(By.ID, "workflowName").send_keys(rand_new_workflow)
    rand_new_workflowdesc = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    context.driver.find_element(By.ID, "workflowDesc").clear()
    context.driver.find_element(By.ID, "workflowDesc").send_keys(rand_new_workflowdesc)


@then('edit workflow and description')
def set_editworkflow(context):
    rand_edit_workflow = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    context.driver.find_element(By.ID, "workflowName").clear()
    context.driver.find_element(By.ID, "workflowName").send_keys(rand_edit_workflow)
    rand_edit_workflowdesc = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    context.driver.find_element(By.ID, "workflowDesc").clear()
    context.driver.find_element(By.ID, "workflowDesc").send_keys(rand_edit_workflowdesc)

