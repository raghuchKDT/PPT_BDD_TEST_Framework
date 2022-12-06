from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


btn_project_link_text = "Project"
btn_newproject_xpath = "//*[@id='bntGoToCreateProject']"
btn_selectPopupTimer_xpath = "//*[@id='popupTimer']/option[6]"
selectDeviceManager_xpath = "//*[@id='headingTwo']/h6/a"
selectSystemGroup_xpath = "//*[@id='systemGroup']/option[2]"
unselect_project_xpath = "//*[@id='tblProject']/tbody/tr[1]/td[1]/label/span"
select_project_xpath = "//*[@id='tblProject']/tbody/tr[3]/td[1]/label/span"
btn_saveproject_xpath = "//*[@id='btn-Save']"
btn_editproject_xpath = "//*[@id='btn-Edit']"
btn_EditPopupTimer_xpath = "//*[@id='popupTimer']/option[7]"
editSystemGroup_xpath = "//*[@id='systemGroup']/option[1]"
btn_copyproject_xpath = "//*[@id='btn-SaveAs']"
btn_savecopyproject_xpath = "//*[@id='btn-saveas-project']"
btn_delete_project_xpath = "//*[@id='btn-delete']"
btn_confirmdelete_project_xpath = "//*[@id='btn-delete-project']"


@then('Project Page should load successfully')
def step_impl(context):
    time.sleep(2)
    assert 'Project' in context.driver.page_source


@then('click on new btn for new project')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newproject_xpath).click()


@then('Enter Project Name and description')
def set_newproject(context):
    rand_new_project = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "ProjName").clear()
    context.driver.find_element(By.ID, "ProjName").send_keys(rand_new_project)
    rand_new_projectdesc = ''.join((random.choice('qwertysdfgio') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "Projdesc").clear()
    context.driver.find_element(By.ID, "Projdesc").send_keys(rand_new_projectdesc)


@then('Enter Unfreeze Passcode and Facility Name')
def set_projectdetails(context):
    time.sleep(1)
    rand_newUnfreeze_pass = ''.join((random.choice('abcdefghijk') for i in range(5)))
    context.driver.find_element(By.ID, "unfreezepass").clear()
    context.driver.find_element(By.ID, "unfreezepass").send_keys(rand_newUnfreeze_pass)
    rand_newFacility_name = ''.join((random.choice('lkjhgfdsp') for i in range(6)))
    context.driver.find_element(By.ID, "facilityName").clear()
    context.driver.find_element(By.ID, "facilityName").send_keys(rand_newFacility_name)


@then('select HMI Message Popup Timer')
def set_popuptimer(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_selectPopupTimer_xpath).click()


@then('click Device Manager')
def set_DeviceManager(context):
    time.sleep(2)
    element = context.driver.find_element(By.XPATH, "//*[@id='headingTwo']/h6/a")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    context.driver.find_element(By.XPATH, selectDeviceManager_xpath).click()


@then('select System Group')
def set_SystemGroup(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, selectSystemGroup_xpath).click()


@then('click on save btn to save new project')
def save_btn(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_saveproject_xpath).click()


@then('Project should be created successfully')
def verify_Project(context):
    time.sleep(3)
    assert 'Updated Successfully!' in context.driver.page_source


@then('select Project')
def select_project(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, select_project_xpath).click()


@then('click on Edit btn for editing project')
def step_clickEditbtn(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editproject_xpath).click()


@then('Edit Project Name and description')
def set_editproject(context):
    rand_edit_project = ''.join((random.choice('aeiourtnbqs') for i in range(5)))
    time.sleep(2)
    context.driver.find_element(By.ID, "ProjName").clear()
    context.driver.find_element(By.ID, "ProjName").send_keys(rand_edit_project)
    rand_edit_projectdesc = ''.join((random.choice('qwertysdfghj') for i in range(7)))
    time.sleep(2)
    context.driver.find_element(By.ID, "Projdesc").clear()
    context.driver.find_element(By.ID, "Projdesc").send_keys(rand_edit_projectdesc)


@then('Edit Unfreeze Passcode and Facility Name')
def set_editprojectdetails(context):
    time.sleep(2)
    rand_editUnfreeze_pass = ''.join((random.choice('hijklmnop') for i in range(5)))
    context.driver.find_element(By.ID, "unfreezepass").clear()
    context.driver.find_element(By.ID, "unfreezepass").send_keys(rand_editUnfreeze_pass)
    rand_editFacility_name = ''.join((random.choice('qwaszxcvmnd') for i in range(6)))
    time.sleep(1)
    context.driver.find_element(By.ID, "facilityName").clear()
    context.driver.find_element(By.ID, "facilityName").send_keys(rand_editFacility_name)


@then('Edit HMI Message Popup Timer')
def set_editpopuptimer(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_EditPopupTimer_xpath).click()


@then('Edit System Group')
def set_editSystemGroup(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, editSystemGroup_xpath).click()


@then('Project should be edited successfully')
def verify_EditedProject(context):
    time.sleep(3)
    assert 'Updated Successfully!' in context.driver.page_source


@then('click on Copy btn for creating duplicate project')
def step_clickCopybtn(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_copyproject_xpath).click()


@then('Enter Project Name')
def set_projectname(context):
    rand_copy_project = ''.join((random.choice('aeiourtnqw') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewProjectName").clear()
    context.driver.find_element(By.ID, "txtNewProjectName").send_keys(rand_copy_project)


@then('click on save btn to save duplicate project')
def copysave_btn(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_savecopyproject_xpath).click()


@then('Project should be copied successfully')
def verify_CopyProject(context):
    time.sleep(3)
    assert 'Data Added Successfully.' in context.driver.page_source


@then('unselect default project')
def unselect_proj(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, unselect_project_xpath).click()


@then('select project to delete')
def select_proj(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, select_project_xpath).click()


@then('click on delete btn to delete project')
def delete_btn(context):
    context.driver.implicitly_wait(5)
    # time.sleep(2)
    context.driver.find_element(By.XPATH, btn_delete_project_xpath).click()


@then('click on confirm delete btn to delete project')
def confirmdelete_btn(context):
    context.driver.implicitly_wait(5)
    # time.sleep(3)
    context.driver.find_element(By.XPATH, btn_confirmdelete_project_xpath).click()


@then('Project should be deleted successfully')
def verify_ProjectDelete(context):
    time.sleep(2)
    assert 'Deleted Successfully.' in context.driver.page_source

