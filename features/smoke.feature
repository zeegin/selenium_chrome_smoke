
Feature: Smoke test

  Scenario: Smoke
    Given I goto http://localhost/1c/demossl
    When I enter user name Администратор
    And I wait until home page is opened
    Then I take screenshot to screenshot.png