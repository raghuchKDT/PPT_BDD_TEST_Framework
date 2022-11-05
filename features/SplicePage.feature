Feature: Push Pull Touch Splice Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Variant page
    Then navigate to Splice Page

  Scenario: Verify Splice Page in Project
    Then Splice Page should load successfully

  Scenario: Create new Splice in Project
    Then click on new btn for creating splice
    Then Enter the splice name
    Then click on save for saving splice name
    Then New Splice should be created successfully

  Scenario: Edit Splice in Project
    Then click on checkbox which you want to edit
    Then click on edit btn of splice
    Then Edit the splice name
    Then click on save of splice
    Then Edited splice should load successfully

  Scenario: Copy Splice in Project
    Then click on checkbox which you want to copy
    Then click on copy btn of splice
    Then enter the name of splice
    Then click on save btn splice
    Then copied splice should load successfully


  Scenario: Delete Splice in Project
    Then click on checkbox which you want to delete
    Then click on delete btn of splice
    Then Verify that the splice is deleted successfully
