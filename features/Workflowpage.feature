Feature: Push Pull Touch Workflow Page
  Scenario: Verify Workflow Page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to workflow Page
    Then Workflow page should successfully load

  Scenario: Create new Workflow Page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to workflow Page
    Then click on new btn for new workflow
    Then Enter Workflow and description
    Then Save the workflow
    Then New workflow should be created successfully

  Scenario: Edit Workflow Page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    And navigate to workflow Page
    Then click on checkbox of one of the workflow
    Then click on Edit btn for editing
    Then edit workflow and description
    Then save the workflow
    Then Workflow should be edited successfully

  Scenario: Delete Workflow Page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    And navigate to workflow Page
    Then click on checkbox of one of the workflow
    Then click on delete btn for deleting the workflow
    Then workflow should successfully delete

  Scenario: General Properties of Workflow Page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    And navigate to workflow Page
    Then click on checkbox to verify general properties
    Then General Properties should be displayed