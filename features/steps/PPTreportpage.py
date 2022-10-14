from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

click_Report_xpath = "//*[@id='five']/span"
btn_newreport_xpath = "//*[@id='bntGoToCreateReport']"
btn_savereport_xpath = "//*[@id='btn-reportSave']"
btn_checkbox3_xpath = "//*[@id='tblReport']/tbody/tr[1]/td[1]/label/span"
btn_editreport_xpath = "//*[@id='btn-reportEdit']"
btn_deletereport_xpath = "//*[@id='btn-reportdelete']"
btn_deletepopupreport_xpath = "//*[@id='btn-delete-report']"
btn_heckbox01_xpath = "//*[@id='tblReport']/tbody/tr[1]/td[1]/label/span"


@then('navigate to Report Page')
def report_page(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, click_Report_xpath).click()


@then('verify the Report Page')
def verify_report(context):
    time.sleep(2)
    assert 'Report' in context.driver.page_source


@then('click on new btn in report page')
def new_btn_report(context):
    context.driver.find_element(By.XPATH, btn_newreport_xpath).click()


@then('Enter Name as "{name}" and Description as "{desc}"')
def new_report(context, name, desc):
    context.driver.find_element(By.ID, "reportName").clear()
    context.driver.find_element(By.ID, "reportName").send_keys(name)
    context.driver.find_element(By.ID, "description").clear()
    context.driver.find_element(By.ID, "description").send_keys(desc)


@then('click on save report btn')
def save_btn_report(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_savereport_xpath).click()


@then('report should be successfully created')
def verify_newreport(context):
    time.sleep(2)
    assert 'Updated Successfully.' in context.driver.page_source


@then('click on checkbox of the report to edit')
def click_checkbox(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_checkbox3_xpath).click()


@then('click on edit btn in report page')
def click_Editreport(context):
    context.driver.find_element(By.XPATH, btn_editreport_xpath).click()


@then('Edit Name as "{Name}" and Description as "{Desc}"')
def edit_report(context, Name, Desc):
    context.driver.find_element(By.ID, "reportName").clear()
    context.driver.find_element(By.ID, "reportName").send_keys(Name)
    context.driver.find_element(By.ID, "description").clear()
    context.driver.find_element(By.ID, "description").send_keys(Desc)


@then('report should be successfully edited')
def Verify_editedreport(context):
    time.sleep(2)
    assert 'Updated Successfully.' in context.driver.page_source


@then('click on checkbox of the report to delete the report')
def click_checkbox3(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_checkbox3_xpath).click()


@then('click on delete btn in report page')
def click_delete_report(context):
    context.driver.find_element(By.XPATH, btn_deletereport_xpath).click()


@then('report should be successfully deleted')
def verify_deletedreport(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_deletepopupreport_xpath).click()
    time.sleep(1)
    assert 'Deleted Successfully.' in context.driver.page_source


@then('click on checkbox for general properties')
def checkbox_1(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, btn_heckbox01_xpath).click()


@then('Report General Properties should be displayed')
def verify_generalprop(context):
    exp_ele = ['Name']
    data_bas_ele = context.driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div/div[1]/div/div/div[1]/div/h5")

    for idx, bas_ele in enumerate(data_bas_ele):
        print(idx, bas_ele.text)
        assert (exp_ele[idx] == bas_ele.text)

    exp_ele = ['Description']
    data_bas_ele = context.driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div/div[1]/div/div/div[3]/div/h5")

    for idx, bas_ele in enumerate(data_bas_ele):
        print(idx, bas_ele.text)
        assert (exp_ele[idx] == bas_ele.text)

    exp_ele = ['Separator']
    data_bas_ele = context.driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div/div[1]/div/div/div[5]/div/h5")

    for idx, bas_ele in enumerate(data_bas_ele):
        print(idx, bas_ele.text)
        assert (exp_ele[idx] == bas_ele.text)

    exp_ele = ['Created date']
    data_bas_ele = context.driver.find_elements(By.XPATH, "//*[@id='collapseOne']/div/div[1]/div/div/div[7]/div/h5")

    for idx, bas_ele in enumerate(data_bas_ele):
        print(idx, bas_ele.text)
        assert (exp_ele[idx] == bas_ele.text)


@then('Global variables web elements should be verified')
def verify_globalvariables(context):
    time.sleep(2)
    exp_ele7 = ['VariableName\nType\nProtocol\ncount_pass\nvar\n@countpass@\ncount_fail\nvar\n@countfail@\nlot_size\nvar\n@lotsize@\nlot_counter\nvar\n@lotcounter@\ntext1\nvar\n@text1@\ntext2\nvar\n@text2@\ntext3\nvar\n@text3@\ntext4\nvar\n@text4@\ntext5\nvar\n@text5@\nbarcode1\nvar\n@barcode1@\nbarcode2\nvar\n@barcode2@\nbarcode3\nvar\n@barcode3@\nWire_ID\nvar\n@wireID@\nmeasure_push_min_value\nvar\n@push_min_value@\nmeasure_push_max_value\nvar\n@push_max_value@\nmeasure_pull_min_value\nvar\n@pull_min_value@\nmeasure_pull_max_value\nvar\n@pull_max_value@\ndate\nsys\n@date@\ntime\nsys\n@time@\nvariant_name\nsys\n@variant@\nproject_name\nsys\n@project@\nuser_name\nsys\n@username@\ntotal_test_pass\nsys\n@test_pass@\ntotal_test_fail\nsys\n@test_fail@']
    data_bas_ele7 = context.driver.find_elements(By.XPATH, "//*[@id='pills-report']/div/div/div[3]/div")

    for idx, bas_ele7 in enumerate(data_bas_ele7):
        print(idx, bas_ele7.text)
        assert (exp_ele7[idx] == bas_ele7.text)


@then('Verification on head webelements need to be done')
def verify_webelements(context):
    exp_ele4 = ['Report Name']
    data_bas_ele4 = context.driver.find_elements(By.XPATH, "//*[@id='tblReport']/thead/tr/th[2]")

    for idx, bas_ele4 in enumerate(data_bas_ele4):
        print(idx, bas_ele4.text)
        assert (exp_ele4[idx] == bas_ele4.text)

    exp_ele5 = ['Index\nVariable Name']
    data_bas_ele5 = context.driver.find_elements(By.XPATH, "//*[@id='pills-report']/div/div/div[2]/div")

    for idx, bas_ele5 in enumerate(data_bas_ele5):
        print(idx, bas_ele5.text)
        assert (exp_ele5[idx] == bas_ele5.text)

    exp_ele6 = ['VariableName\nType\nProtocol']
    data_bas_ele6 = context.driver.find_elements(By.XPATH, "//*[@id='ViewAllGlobalVariable']/div/div[1]")

    for idx, bas_ele6 in enumerate(data_bas_ele6):
        print(idx, bas_ele6.text)
        assert (exp_ele6[idx] == bas_ele6.text)
