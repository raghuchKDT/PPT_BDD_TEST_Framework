Feature: Push Pull Touch Variant Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "OCUA4" and password "1234"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Variant page

  Scenario: Verify Variant and Explorer Page in Project
    Then Verify that variant page and explorer page are loaded

  Scenario: Create new Variant in Project
    Then click on new btn to create variant
    Then enter the variant name and description
    Then click on save btn variant
    Then New variant should be created successfully


  Scenario: General properties Variant in Project
    Then Verify the general properties of the variant

  Scenario: Edit Variant in Project
    Then click on edit btn variant
    Then edit the variant name and description
    Then click on save btn variant
    Then Variant should be edited successfully

  Scenario: Copy Variant in Project
    Then click on copy btn variant
    Then enter variant name and desc
    Then click on save btn to copy the changes
    Then variant should be copied successfully

  Scenario: Delete Variant in Project
    Then click on delete btn variant
    Then Verify that the variant is deleted successfully
