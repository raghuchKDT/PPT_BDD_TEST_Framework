Feature: Push Pull Touch User Manager Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to User Manager Page

  Scenario: Verify User Manager Page
    Then verify the user manager Page

  Scenario: Create New User in User Manager
    Then click on new btn in user manager
    Then Enter username and password
    Then click on save btn
    And user should be successfully created

  Scenario: Edit User in User Manager
    Then click on checkmark to edit the user
    Then click on edit btn in user
    Then Edit username and password
    Then click on save btn
    And User should be edited successfully

   Scenario: Delete User in User Manager
    Then click on checkmark to delete the user
    Then click on delete btn in user
    And User should be deleted successfully

  Scenario: Verify Properties in User Manager
    Then Verify the headlines in user manager page
    Then Verify the General Properties of user

  Scenario: Verify the Access Section in user manager
    Then Verify web elements in access section present
