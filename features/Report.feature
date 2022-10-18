Feature: Push Pull Touch Report Page
  Scenario: Verify Report Page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Report Page
    Then verify the Report Page

  Scenario: Create New Report in Report Page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Report Page
    Then click on new btn in report page
    Then Enter Name as "Report-4" and Description as "desc"
    Then click on save report btn
    And report should be successfully created

  Scenario: Edit  Report in Report Page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Report Page
    Then click on checkbox of the report to edit
    Then click on edit btn in report page
    Then Edit Name as "Report-03" and Description as "desc"
    Then click on save report btn
    And report should be successfully edited

  Scenario: Verify The general properties of report
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Report Page
    Then click on checkbox for general properties
    Then Report General Properties should be displayed

  Scenario: Verify The global variables and verification on head webelements of report
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Report Page
    Then Global variables web elements should be verified
    Then Verification on head webelements need to be done

  Scenario: Delete  Report in Report Page
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Report Page
    Then click on checkbox of the report to delete the report
    Then click on delete btn in report page
    And report should be successfully deleted