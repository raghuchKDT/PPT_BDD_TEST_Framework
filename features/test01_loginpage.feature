Feature: Push Pull Touch Login and Info Page
  Background: common steps
    Given I launch chrome browser
    When I open PushPullTouch homepage

  Scenario: Logo presence on PushPullTouch Login page
    Then Verify that the logo present on the page

  Scenario: Login to PPT with valid parameters
    When Enter username "OCUA4" and password "1234"
    When click on Sign In button
    Then User must successfully login to PPT webpage

  Scenario: Verify Info page of PPT
    When Enter username "OCUA4" and password "1234"
    When click on Sign In button
    Then Verify the Info Page in PPT
    Then Info Page should have recent project
    Then verify recent project page contents

  Scenario: Verify Version History in Info Page of PPT
    When Enter username "OCUA4" and password "1234"
    When click on Sign In button
    Then Verify the Info Page in PPT
    Then Verify the version history in Info Page
    Then Verify the contents on version history webpage

  Scenario:Verify Options in Info Page of PPT
    When Enter username "OCUA4" and password "1234"
    When click on Sign In button
    Then Verify the Info Page in PPT
    Then Verify the Options page in Info page
    Then Verify the contents in options page