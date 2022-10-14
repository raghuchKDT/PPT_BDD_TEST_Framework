Feature: Push Pull Touch Role Page
  Scenario: Verify Role Page in user manager
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to User Manager Page
    Then navigate to role Page
    Then Role page should successfully load

  Scenario: Create new Role
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to User Manager Page
    Then navigate to role Page
    Then click on new btn for create new role
    Then Enter Role name
    Then save the role by clicking save btn
    Then New role should be created successfully

   Scenario: Edit Role name in role page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to User Manager Page
    Then navigate to role Page
    Then click on checkbox to edit the role
    Then click on edit btn to edit role
    Then Edit Role name
    Then save the role by clicking save btn
    Then role should be edited successfully

  Scenario: Delete Role name in role page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to User Manager Page
    Then navigate to role Page
    Then click on checkbox to delete the role
    Then click on delete btn to delete role
    Then role should be successfully deleted

