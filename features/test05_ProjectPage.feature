Feature: Push Pull Touch Project Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "OCUA4" and password "1234"
    And click on Sign In button
    Then navigate to Project Page

  Scenario: Verify Project Page in Project
    Then Project Page should load successfully


  Scenario: Create new Project in project page
    Then click on new btn for new project
    Then Enter Project Name and description
    Then Enter Unfreeze Passcode and Facility Name
    Then select HMI Message Popup Timer
    Then click Device Manager
    Then select System Group
    Then click on save btn to save new project
    Then Project should be created successfully


   Scenario: Edit Project in project page
    Then click on Edit btn for editing project
    Then Edit Project Name and description
    Then Edit Unfreeze Passcode and Facility Name
    Then Edit HMI Message Popup Timer
    Then click Device Manager
    Then Edit System Group
    Then click on save btn to save new project
    Then Project should be edited successfully


  Scenario: Copy Project in project page
    Then click on Copy btn for creating duplicate project
    Then Enter Project Name
    Then click on save btn to save duplicate project
    Then Project should be copied successfully


  Scenario: Delete Project in PPT page
    Then click on delete btn to delete project
    Then click on confirm delete btn to delete project
    Then Project should be deleted successfully