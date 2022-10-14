Feature: Push Pull Touch Switch Page
  Scenario: Verify switch Page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to switch page
    Then Switch Page should load successfully

  Scenario: Create New Switch in switch page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to switch page
    Then click on new btn for new switch
    Then Enter switch name
    And click on save
    Then New switch should be created successfully

  Scenario: Edit Switch in switch page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to switch page
    And click on checkbox of switch
    Then click on edit btn for editing switch
    Then Edit switch name
    Then click on save
    Then switch should be edited successfully

  Scenario: Delete Switch in switch page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to switch page
    And click on checkbox of switch
    Then click on delete btn for deleting the switch
    Then switch should be deleted successfully
