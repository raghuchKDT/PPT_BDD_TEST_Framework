Feature: Push Pull Touch Variant Page
  Scenario: Verify Variant and Explorer Page in Project
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Variant page
    Then Verify that variant page and explorer page are loaded

  Scenario: Create new Variant in Project
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Variant page
    Then click on new btn to create variant
    Then enter the variant name and description
    Then click on save btn variant
    Then New variant should be created successfully

#  Scenario: Edit Variant in Project
#    Given I launch chrome browser
#    When I open PushPullTouch homepage
#    And Enter username "admin" and password "admin"
#    And click on Sign In button
#    Then navigate to Project Page
#    Then navigate to Variant page
#    Then select the checkbox
#    Then click on edit btn variant
#    Then edit the variant name and description
#    Then click on save btn variant
#    Then Variant should be edited successfully
#
#  Scenario: Copy Variant in Project
#    Given I launch chrome browser
#    When I open PushPullTouch homepage
#    And Enter username "admin" and password "admin"
#    And click on Sign In button
#    Then navigate to Project Page
#    Then navigate to Variant page
#    Then select the checkbox
#    Then click on copy btn variant
#    Then enter variant name and desc
#    Then click on save btn to copy the changes
#    Then variant should be copied successfully
#
#  Scenario: Delete Variant in Project
#    Given I launch chrome browser
#    When I open PushPullTouch homepage
#    And Enter username "admin" and password "admin"
#    And click on Sign In button
#    Then navigate to Project Page
#    Then navigate to Variant page
#    Then select the checkbox
#    Then click on delete btn variant
#    Then Verify that the variant is deleted successfully


  Scenario: General properties Variant in Project
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "admin" and password "admin"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Variant page
    Then Verify the general properties of the variant