Feature: Push Pull Touch Role Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "OCUA4" and password "1234"
    And click on Sign In button
    Then navigate to User Manager Page
    Then navigate to role Page

  Scenario: Verify Role Page in user manager
    Then Role page should successfully load

    @Sanity
  Scenario: Create new Role
    Then click on new btn for create new role
    Then Enter Role name
    Then save the role by clicking save btn
    Then New role should be created successfully

   Scenario: Edit Role name in role page
    Then click on checkbox to edit the role
    Then click on edit btn to edit role
    Then Edit Role name
    Then save the role by clicking save btn
    Then role should be edited successfully

  Scenario: Delete Role name in role page
    Then click on checkbox to delete the role
    Then click on delete btn to delete role
    Then role should be successfully deleted

  Scenario: Verify the Access Section in role page
    Then Click on checkmark of which access section you want to see
    Then Verify web elements in access section present