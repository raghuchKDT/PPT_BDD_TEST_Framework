Feature: Push Pull Touch Xcode Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "OCUA4" and password "1234"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Xcode Page

  Scenario: Verify Xcode Page in Project
    Then Xcode Page should load successfully

  Scenario: Create New Xcode in Project
    Then create new btn for xcode
    Then Enter xcode name , customer code and description
    Then select module which you want
    Then click save for saving XCode
    Then New Xcode should be successfully created


#  Scenario: General properties  Xcode in Project
#    Then verify the general properties of the xcode


  Scenario: Edit  Xcode in Project
    Then click on edit btn of xcode
    Then Edit xcode name, customer no and description
    Then click save for saving Edited XCode
    Then Edited xcode should load successfully


  Scenario: Copy  Xcode in Project
    Then click on copy btn
    Then select xcode from the list
    Then Enter xcode and customer no and description
    Then click save for saving Copied XCode
    Then Xcode should be successfully copied


  Scenario: Delete  Xcode in Project
    Then click on delete btn to delete the xcode
    Then click on confirm delete btn to delete the xcode
    Then verify that the xcode is deleted successfully
