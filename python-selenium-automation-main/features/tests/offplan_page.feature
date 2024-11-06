
Feature: Off-Plan Page

  Scenario: User can see titles and pictures on each product inside the off plan page
    Given Open the main page
    And Log in to the page
    When Click on “off plan” at the left side menu
    Then Verify the right page opens
    Then Verify each product on this page contains a title and picture visible