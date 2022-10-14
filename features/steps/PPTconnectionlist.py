from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_conlist_xpath = "//*[@id='pills-connectionlist-tab']"
btn_newconlist_xpath = "//*[@id='bntCreateConnectionListDetail']"
btn_savelist_xpath = "//*[@id='btn-add-connectionDet']"
btn_checkbox01list_xpath = "//*[@id='conPlbl-46']/span"
btn_editlist_xpath = "//*[@id='bntEditConnectionListDetail']"
btn_saveeditedlist_xpath = "//*[@id='btn-update-connectionDet']"
btn_copylist_xpath = "//*[@id='btn-wire-copy']"
btn_savecopylist_xpath = "//*[@id='btn-copy-connection']"
btn_deletelist_xpath = "//*[@id='btn-connectionlistDetaildelete']"
btn_popupdeletelist_xpath = "//*[@id='btn-delete-connectionlist']"
btn_checkmarklist_xpath = "//*[@id='conPlbl-50']/span"
btn_newlistcon_xpath = "//*[@id='bntCreateConnecctionList']"
btn_fromxcode_xpath = "//*[@id='addConnectionListModal']/div/div/div[2]/input[2]"
btn_selectxcode_xpath = "//*[@id='drdConnectionListWireId']"
btn_selectpinnumber_xpath = "//*[@id='drdFromPinName']"
btn_savewireid_xpath = "//*[@id='btn-add-connection']"
btn_editconlist_xpath = "//*[@id='bntEditConnectionList']"
btn_saveeditedconlist_xpath = "//*[@id='btn-update-connection']"
btn_deleteconlist_xpath = "//*[@id='btn-connectionlistdelete']"
btn_popupdeleteconlist_xpath = "//*[@id='btn-delete-connectionlist']"


@then('navigate to connection list page')
def connectionlist_page(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_conlist_xpath).click()


@then('Connection list Page should load successfully')
def Verify_conlistpage(context):
    time.sleep(1)
    assert 'Connection List' in context.driver.page_source


@then('click on new btn to create connection list')
def new_conlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newconlist_xpath).click()


@then('Enter con list name and description')
def set_namendesc(context):
    rand_new_conname = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewConnectionListName").clear()
    context.driver.find_element(By.ID, "txtNewConnectionListName").send_keys(rand_new_conname)
    rand_new_conlistdesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewConnectionListDescription").clear()
    context.driver.find_element(By.ID, "txtNewConnectionListDescription").send_keys(rand_new_conlistdesc)


@then('click on save btn to create new con list')
def save_conlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_savelist_xpath).click()


@then('New connection list should be created successfully')
def verify_conlist(context):
    time.sleep(1)
    assert 'Connection List Details Added successfully.' in context.driver.page_source


@then('Click on one of the checkbox you want to edit list')
def checkbox01_conlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox01list_xpath).click()


@then('click on edit btn to edit con list')
def edit_conlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editlist_xpath).click()


@then('Edit the con list name and description')
def edit_namendesc(context):
    rand_edit_conname = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewConnectionListName").clear()
    context.driver.find_element(By.ID, "txtNewConnectionListName").send_keys(rand_edit_conname)
    rand_edit_conlistdesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewConnectionListDescription").clear()
    context.driver.find_element(By.ID, "txtNewConnectionListDescription").send_keys(rand_edit_conlistdesc)


@then('click on save to update the con list')
def save_Editedlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_saveeditedlist_xpath).click()


@then('Connection list should be edited successfully')
def verify_editedlist(context):
    time.sleep(1)
    assert 'Connection List Details Added successfully.' in context.driver.page_source


@then('Click on one of the checkbox you want to copy list')
def copy_checkbox(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox01list_xpath).click()


@then('click on copy btn to copy con list')
def copy_list(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_copylist_xpath).click()


@then('Give the con list name and description')
def copyname_Desc(context):
    rand_copy_conname = ''.join((random.choice('aeiourtnsclp') for i in range(5)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtCopyNewConnectionName").clear()
    context.driver.find_element(By.ID, "txtCopyNewConnectionName").send_keys(rand_copy_conname)
    rand_copy_conlistdesc = ''.join((random.choice('aeiourtnsclp') for i in range(7)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtCopyNewConnectionListDescription").clear()
    context.driver.find_element(By.ID, "txtCopyNewConnectionListDescription").send_keys(rand_copy_conlistdesc)


@then('click on save as to copy the con list')
def copy_savelist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_savecopylist_xpath).click()


@then('Connection list should be copied successfully')
def verify_copiedlist(context):
    time.sleep(1)
    assert 'Connection List Details Updated successfully.' in context.driver.page_source


@then('Click on one of the checkbox you want to delete list')
def delete_checkbox(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox01list_xpath).click()


@then('click on delete btn to delete the connection list')
def delete_conlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletelist_xpath).click()


@then('Verify that connection list is deleted successfully')
def verify_deletedlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_popupdeletelist_xpath).click()
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source


@then('click on checkmark on conlist')
def checkmark_list(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkmarklist_xpath).click()


@then('click on new btn to create con list')
def click_newconlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newlistcon_xpath).click()


@then('Enter Wire Id and sequence Id')
def setwireid_sequenceid(context):
    time.sleep(1)
    rand_newcon_list = ''.join((random.choice('aeiournstlcp') for i in range(5)))

    context.driver.find_element(By.XPATH, "//*[@id='drdConnectionListWireId']").clear()
    context.driver.find_element(By.XPATH, "//*[@id='drdConnectionListWireId']").send_keys(rand_newcon_list)
    time.sleep(1)
    rand_sequence_id = ''.join((random.choice('airhiiwdhudufh') for i in range(5)))

    context.driver.find_element(By.XPATH, "//*[@id='txtSequenceId']").clear()
    context.driver.find_element(By.XPATH, "//*[@id='txtSequenceId']").send_keys(rand_sequence_id)


@then('click on from xcode')
def xcode(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_fromxcode_xpath).click()


@then('click on xcode you to select and pin number')
def pinnumber(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_selectxcode_xpath).click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_selectpinnumber_xpath).click()


@then('click on save btn to create new con list with wire Id')
def save_conlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_savewireid_xpath).click()


@then('Verify that the connection list Wire Id should be created successfully')
def verify_newwire(context):
    time.sleep(1)
    assert 'Connection List Details Added successfully.' in context.driver.page_source


@then('click on edit btn to create con list')
def edit_conlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editconlist_xpath).click()


@then('click on save btn to edit con list with wire Id')
def save_editedconlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_saveeditedconlist_xpath).click()


@then('Verify that the connection list Wire Id should be edited successfully')
def verify_editedconlist(context):
    time.sleep(1)
    assert 'Connection List Updated successfully.' in context.driver.page_source


@then('click on delete btn to delete con list')
def delete_conlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deleteconlist_xpath).click()


@then('Verify that con list is deleted successfully')
def verify_deletedconlist(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_popupdeleteconlist_xpath).click()
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source

