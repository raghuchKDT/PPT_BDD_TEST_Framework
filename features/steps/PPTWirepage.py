from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

btn_wirepage_xpath = "//*[@id='pills-wire-tab']"
btn_newwire_xpath = "//*[@id='deChk2']/div[1]/div[1]/div[1]/button[1]"
click_color1_xpath = "//*[@id='drdcolor1']"
click_color2_xpath = "//*[@id='drdcolor2']"
click_color3_xpath = "//*[@id='drdcolor3']"
btn_p2l_xpath = "//*[@id='drdPickToLightId']"
btn_WLED_pinxpath = "//*[@id='txtNewWledPinName']"
btn_Savewire_xpath = "//*[@id='btn-add-wire']"
btn_checkbox01_wirexpath = "//*[@id='chkwire-163']"
btn_copywire_xpath = "//*[@id='btn-wire-copy']"
btn_saveas_wirexpath = "//*[@id='btn-copy-wire']"
btn_deletewire_xpath = "//*[@id='btn-wire-delete']"
btn_popupdeletewire_xpath = "//*[@id='btn-delete-wire']"
btn_checkbox04wire_deletexpath = "//*[@id='chkwire-158']"
btn_editbtnwire_deletexpath = "//*[@id='btn-wire-edit']"
btn_saveeditedwire_xpath = "//*[@id='btn-update-wire']"
btn_newcolorscheme_xpath = "//*[@id='deChk2']/div[2]/div[1]/div[1]/button[1]"
btn_savecolorscheme_xpath = "//*[@id='btn-add-wirecolorscheme']"
btn_selectcolorscheme_xpath = "//*[@id='txtNewWireSchemeColor']"
btn_checkbox01colorscheme_xpath = "//*[@id='chkwirecolor-12']"
btn_editcolorscheme_xpath = "//*[@id='btn-WireColorScheme-Edit']"
btn_selecteditcolorscheme_xpath = "//*[@id='txtNewWireSchemeColor']"
btn_deletewirescheme_xpath = "//*[@id='btn-WireColorScheme-Delete']"
btn_deletepopupwirescheme_xpath = "//*[@id='btn-delete-wirecolorscheme']"


@then('navigate to wire page')
def Wire_page(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_wirepage_xpath).click()


@then('Wire Page should load successfully')
def verify_wirepage(context):
    time.sleep(1)
    assert 'Wire' in context.driver.page_source


@then('click on new btn for new wire')
def new_wire(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newwire_xpath).click()


@then('Enter wire ID and Group ID')
def set_wire(context):
    rand_wire_id = ''.join((random.choice('12345678910') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewWireId").clear()
    context.driver.find_element(By.ID, "txtNewWireId").send_keys(rand_wire_id)
    rand_group_id = ''.join((random.choice('12345678910') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "drdGrpId").clear()
    context.driver.find_element(By.ID, "drdGrpId").send_keys(rand_group_id)


@then('select color 1 , 2 and 3')
def set_color(context):
    context.driver.find_element(By.XPATH, click_color1_xpath).click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, click_color2_xpath).click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, click_color3_xpath).click()


@then('Set the Push min and max value')
def Pushminmax(context):
    rand_push_minval = ''.join((random.choice('1234567') for i in range(1)))
    context.driver.find_element(By.ID, "txtNewPushMinValue").clear()
    context.driver.find_element(By.ID, "txtNewPushMinValue").send_keys(rand_push_minval)
    rand_push_maxval = ''.join((random.choice('123456798') for i in range(1)))
    context.driver.find_element(By.ID, "txtNewPushMaxValue").clear()
    context.driver.find_element(By.ID, "txtNewPushMaxValue").send_keys(rand_push_maxval)


@then('set Pull min and max value')
def setpull_value(context):
    rand_pull_minval = ''.join((random.choice('123456789') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewPullMinValue").clear()
    context.driver.find_element(By.ID, "txtNewPullMinValue").send_keys(rand_pull_minval)
    rand_pull_maxval = ''.join((random.choice('123456789') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewPullMaxValue").clear()
    context.driver.find_element(By.ID, "txtNewPullMaxValue").send_keys(rand_pull_maxval)


@then('select Picktolight and WLED pin')
def set_WLEDpin(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_p2l_xpath).click()
    context.driver.find_element(By.XPATH, btn_WLED_pinxpath).click()


@then('click on save for creating new wire')
def save_wireid(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_Savewire_xpath).click()


@then('verify that new wire is created successfully')
def verified_savedwire(context):
    time.sleep(1)
    assert 'Wire Added successfully.' in context.driver.page_source


@then('click on checkbox which you want to copy wire')
def checkbox01_wire(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox01_wirexpath).click()


@then('click on copy btn wire')
def copy_wire(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_copywire_xpath).click()


@then('Enter wire id name')
def copy_wireid(context):
    rand_copywire_id = ''.join((random.choice('12345678910') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtCopyNewWireId").clear()
    context.driver.find_element(By.ID, "txtCopyNewWireId").send_keys(rand_copywire_id)


@then('click on save as btn to save the copied wire')
def saveas_wireid(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_saveas_wirexpath).click()


@then('Wire should be copied successfully')
def verify_copiedwire(context):
    time.sleep(1)
    assert 'New wire created successfully' in context.driver.page_source


@then('click on checkbox which you want to delete wire')
def delete_checkbox(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox04wire_deletexpath).click()


@then('click on delete btn for deleting the wire')
def delete_wire(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletewire_xpath).click()


@then('Verify if the wire is deleted successfully')
def verify_deletedwire(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_popupdeletewire_xpath).click()
    time.sleep(1)
    assert 'wire deleted successfully' in context.driver.page_source


@then('click on checkbox which you want to edit the wire')
def editwire_id(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox04wire_deletexpath).click()


@then('click on edit btn wire id')
def edit_btnwire(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editbtnwire_deletexpath).click()


@then('edit wire ID and Group ID')
def editgroup_id(context):
    rand_editwire_id = ''.join((random.choice('12345678910') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewWireId").clear()
    context.driver.find_element(By.ID, "txtNewWireId").send_keys(rand_editwire_id)
    rand_editgroup_id = ''.join((random.choice('12345678910') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "drdGrpId").clear()
    context.driver.find_element(By.ID, "drdGrpId").send_keys(rand_editgroup_id)


@then('select color 1 , 2 and 3 to edit')
def edit_colour(context):
    context.driver.find_element(By.XPATH, click_color1_xpath).click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, click_color2_xpath).click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, click_color3_xpath).click()


@then('Set the Push min and max value to edit')
def edit_pushvalues(context):
    time.sleep(1)
    rand_push_minval = ''.join((random.choice('1234567') for i in range(1)))
    context.driver.find_element(By.ID, "txtNewPushMinValue").clear()
    context.driver.find_element(By.ID, "txtNewPushMinValue").send_keys(rand_push_minval)
    rand_push_maxval = ''.join((random.choice('123456798') for i in range(1)))
    context.driver.find_element(By.ID, "txtNewPushMaxValue").clear()
    context.driver.find_element(By.ID, "txtNewPushMaxValue").send_keys(rand_push_maxval)


@then('set Pull min and max value to edit')
def edit_pullvalues(context):
    rand_editpull_minval = ''.join((random.choice('123456789') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewPullMinValue").clear()
    context.driver.find_element(By.ID, "txtNewPullMinValue").send_keys(rand_editpull_minval)
    rand_editpull_maxval = ''.join((random.choice('123456789') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewPullMaxValue").clear()
    context.driver.find_element(By.ID, "txtNewPullMaxValue").send_keys(rand_editpull_maxval)


@then('select Picktolight and WLED pin to edit')
def edit_LEDno(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_p2l_xpath).click()
    context.driver.find_element(By.XPATH, btn_WLED_pinxpath).click()


@then('click on save after editing the wire')
def edit_savewrie(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_saveeditedwire_xpath).click()


@then('verify that wire is edited successfully')
def verify_Editedwire(context):
    time.sleep(1)
    assert 'Wire Updated successfully.' in context.driver.page_source


@then('click on new btn for new wire color scheme')
def new_colorscheme(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_newcolorscheme_xpath).click()


@then('Enter color name and abbreviation to create')
def enter_colorname(context):
    rand_color_name = ''.join((random.choice('123456789') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewColorSchemeName").clear()
    context.driver.find_element(By.ID, "txtNewColorSchemeName").send_keys(rand_color_name)
    rand_abbreviation = ''.join((random.choice('123456789') for i in range(1)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtColorAbbreviation").clear()
    context.driver.find_element(By.ID, "txtColorAbbreviation").send_keys(rand_abbreviation)


@then('click on colour btn to select color')
def select_colorscheme(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_selectcolorscheme_xpath).click()


@then('click on save btn to save colour scheme')
def save_colorscheme(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_savecolorscheme_xpath).click()


@then('wire colour should be created successfully')
def verify_color(context):
    time.sleep(1)
    assert 'Color Scheme Added successfully.' in context.driver.page_source


@then('click on checkbox to edit the color scheme')
def edit_colorscheme(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox01colorscheme_xpath).click()


@then('click on edit btn to edit the color scheme')
def edit_btncolor(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_editcolorscheme_xpath).click()


@then('Edit the name and abbreviation of the color')
def edit_nameandcolor(context):
    rand_editcolor_name = ''.join((random.choice('bluegraywhite') for i in range(4)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtNewColorSchemeName").clear()
    context.driver.find_element(By.ID, "txtNewColorSchemeName").send_keys(rand_editcolor_name)
    rand_editabbreviation = ''.join((random.choice('1abcdiehfkwdf') for i in range(4)))
    time.sleep(1)
    context.driver.find_element(By.ID, "txtColorAbbreviation").clear()
    context.driver.find_element(By.ID, "txtColorAbbreviation").send_keys(rand_editabbreviation)


@then('select the color to edit')
def edit_color(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_selecteditcolorscheme_xpath).click()


@then('Verify that the color is edited successfully')
def verify_colorscheme(context):
    time.sleep(1)
    assert 'Wire Color Scheme Updated successfully.' in context.driver.page_source


@then('click on the checkbox of color scheme you want to delete')
def checkbox_deletewire(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox01colorscheme_xpath).click()


@then('click on delete btn to delete wire color')
def delete_wirescheme(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletewirescheme_xpath).click()


@then('verify the wire color scheme is deleted successfully')
def verify_deletedscheme(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletepopupwirescheme_xpath).click()
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source
