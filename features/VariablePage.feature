Feature: Push Pull Touch Variable Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "OCUA4" and password "1234"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Variant page
    Then navigate to Variable Page

  Scenario: Verify Variable Page in Project
    Then Variable Page should load successfully

  Scenario: Verify Variable data in Project
    Then navigate to Variable Page
    Then Verify the data present in variable page