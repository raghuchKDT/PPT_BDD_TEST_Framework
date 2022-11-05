Feature: Push Pull Touch Label Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Label Page

  Scenario: Verify Label Page in Project
    Then Label page should successfully load

  Scenario: Create new Label in Project
    Then click on new btn for creating new label
    Then Enter Label and description
    Then click on save btn to save the label
    Then Label should be created successfully

  Scenario: Edit Label in Project
    Then click on checkbox to edit label
    Then click on edit btn to edit the label
    Then Edit Label and description
    Then click on save btn to save the label
    Then Label should be edited successfully

  Scenario: Delete Label in Project
    Then click on checkbox to delete label
    Then click on delete btn to delete the label
    Then Label should be deleted successfully

  Scenario: global variables Label in Project
    Then verify the global variables in label page

