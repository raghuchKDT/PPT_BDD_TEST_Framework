Feature: Push Pull Touch Wire Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage
    And Enter username "OCUA4" and password "1234"
    And click on Sign In button
    Then navigate to Project Page
    Then navigate to Variant page
    Then navigate to wire page

  Scenario: Verify Wire Page in Project
    Then Wire Page should load successfully

    @Sanity
  Scenario: Create New wire in Project
    Then click on new btn for new wire
    Then Enter wire ID and Group ID
    Then select color 1 , 2 and 3
    Then Set the Push min and max value
    Then set Pull min and max value
    Then select Picktolight and WLED pin
    Then click on save for creating new wire
    Then verify that new wire is created successfully


  Scenario: Copy wire in Project
    Then click on checkbox which you want to copy wire
    Then click on copy btn wire
    Then Enter wire id name
    Then click on save as btn to save the copied wire
    Then Wire should be copied successfully

  Scenario: Edit wire in Project
    Then click on checkbox which you want to edit the wire
    Then click on edit btn wire id
    Then edit wire ID and Group ID
    Then select color 1 , 2 and 3 to edit
    Then Set the Push min and max value to edit
    Then set Pull min and max value to edit
    Then select Picktolight and WLED pin to edit
    Then click on save after editing the wire
    Then verify that wire is edited successfully

  Scenario: Delete wire in Project
    Then click on checkbox which you want to delete wire
    Then click on delete btn for deleting the wire
    Then Verify if the wire is deleted successfully

     @Integration  @Sanity
  Scenario: Create New wire color scheme in Project
    Then click on new btn for new wire color scheme
    Then Enter color name and abbreviation to create
    Then click on colour btn to select color
    Then click on save btn to save colour scheme
    Then wire colour should be created successfully


  Scenario: Edit wire color scheme in Project
    Then click on checkbox to edit the color scheme
    Then click on edit btn to edit the color scheme
    Then Edit the name and abbreviation of the color
    Then select the color to edit
    Then Verify that the color is edited successfully

  Scenario: Delete wire color scheme in Project
    Then click on the checkbox of color scheme you want to delete
    Then click on delete btn to delete wire color
    Then verify the wire color scheme is deleted successfully
