Feature: Push Pull Touch Switch Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "OCUA4" and password "1234"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to switch page

  Scenario: Verify switch Page
    Then Switch Page should load successfully

    @Sanity
  Scenario: Create New Switch in switch page
    Then click on new btn for new switch
    Then Enter switch name
    And click on save
    Then New switch should be created successfully

  Scenario: Edit Switch in switch page
    And click on checkbox of switch
    Then click on edit btn for editing switch
    Then Edit switch name
    Then click on save
    Then switch should be edited successfully

  Scenario: Delete Switch in switch page
    And click on checkbox of switch
    Then click on delete btn for deleting the switch
    Then switch should be deleted successfully
