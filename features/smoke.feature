
Feature: Smoke test

  Scenario: Smoke
    Given I goto http://localhost/1c/demossl
    When I enter user name Администратор
    Then I wait until home page is opened
    