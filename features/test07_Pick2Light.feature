Feature: Push Pull Touch Pick to Light Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "OCUA4" and password "1234"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Pick to Light page

  Scenario: Verify Pick to Light Page in Project
    Then Pick to Light Page should load successfully

    @Sanity
  Scenario: Create Pick to Light in Project
    Then click on new btn for p2l
    Then Enter picktolight name and description
    Then Enter number of LED
    Then click on save btn p2l
    Then pick to light should be created successfully

  Scenario: General Properties Pick to Light in Project
    Then verify the general properties

  Scenario: Edit Pick to Light in Project
    Then click on edit btn of pick to light
    Then edit the p2l and description
    Then Edit no of led
    Then click on save btn to save edited p2l
    Then Pick to Light should be edited successfully

  Scenario: Copy Pick to Light in Project
    Then click on copy btn to copy
    Then enter picktolight name and description for copying
    Then click on save btn to save the copied ptl
    Then Pick to Light should be copied successfully

  Scenario: Delete Pick to Light in Project
    Then click on delete btn
    Then verify that the ptl is deleted successfully