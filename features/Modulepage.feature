Feature: Push Pull Touch Module Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "OCUA4" and password "1234"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Module page

  Scenario: Verify Module Page in Project
    Then Module Page should load successfully

    @Sanity
  Scenario: Create new Module in module page
    Then click on new btn for new module
    Then Enter Module Name and description
    Then Enter no of cavity and no of switch
    Then Enter cavity LED no and choose a png file from the folder
    Then click on save btn in module
    Then Module should be created successfully

  Scenario: copy Module in module page
    Then click on module which you want to copy
    Then click on copy btn to copy module
    Then Enter module name and description to copy
    Then click on save btn to copy the module

  Scenario: Delete Module in module page
    Then click on the module you want to delete
    Then click on delete btn to delete module
    Then Module should successfully be deleted

  Scenario: General Properties of Module in module page
    Then click on module which you want to see general properties
    Then General properties of the module should be displayed
