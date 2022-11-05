Feature: Push Pull Touch Connection List Page
#  Background: common steps
#    Given I launch chrome browser
#    When I open PushPullTouch homepage
#    And Enter username "admin" and password "admin"
#    And click on Sign In button
#    Then navigate to Project Page
#    Then navigate to Variant page
#    Then navigate to connection list page

#  Scenario: Verify Connection List Page in Project
#    Then Connection list Page should load successfully
#
#  Scenario: Create new  Connection List in Project
#    Then click on new btn to create connection list
#    Then Enter con list name and description
#    Then click on save btn to create new con list
#    Then New connection list should be created successfully
#
#
  Scenario: Edit  Connection List in Project
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Variant page
    Then navigate to connection list page
    Then Click on one of the checkbox you want to edit list
    Then click on edit btn to edit con list
    Then Edit the con list name and description
    Then click on save to update the con list
    Then Connection list should be edited successfully
#
#
#  Scenario: Copy Connection List in Project
#    Then Click on one of the checkbox you want to copy list
#    Then click on copy btn to copy con list
#    Then Give the con list name and description
#    Then click on save as to copy the con list
#    Then Connection list should be copied successfully
#
#  Scenario: Delete Connection List in Project
#    Then Click on one of the checkbox you want to delete list
#    Then click on delete btn to delete the connection list
#    Then Verify that connection list is deleted successfully
#
#  Scenario: Create new  Connection List wire associated in Project
#    Then click on checkmark on con_list
#    Then click on new btn to create con list
#    Then Enter Wire Id and sequence Id
#    Then click on from xcode
#    Then click on xcode you to select and pin number
#    Then click on save btn to create new con list with wire Id
#    Then Verify that the connection list Wire Id should be created successfully
#
#  Scenario: Edit Connection List wire associated in Project
#    Then click on checkmark on con_list
#    Then click on edit btn to create con list
#    Then Enter Wire Id and sequence Id
#    Then click on from xcode
#    Then click on xcode you to select and pin number
#    Then click on save btn to edit con list with wire Id
#    Then Verify that the connection list Wire Id should be edited successfully


#  Scenario: Delete Connection List Wire Id in Project
#    Then click on checkmark on con_list
#    Then click on delete btn to delete con list
#    Then Verify that con list is deleted successfully