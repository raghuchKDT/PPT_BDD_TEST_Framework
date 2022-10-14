Feature: Push Pull Touch Variable Page
  Scenario: Verify Variable Page in Project
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Variant page
    Then navigate to Variable Page
    Then Variable Page should load successfully

  Scenario: Verify Variable data in Project
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Variant page
    Then navigate to Variable Page
    Then Verify the data present in variable page