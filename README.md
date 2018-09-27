# selenium_chrome_smoke
Start 1C:Enterprise web-client with selenium and chromedriver, authenticate and take screenshot via BDD feature

```bash
pip install -r requirements.txt
behave
```

Example output

```
selenium_chrome_smoke>behave

DevTools listening on ws://127.0.0.1:60710/devtools/browser/c174d103-3f10-43f3-ac6b-faefcd3ccc56
Feature: Smoke test # features/smoke.feature:2

  Scenario: Smoke                            # features/smoke.feature:4
    Given I goto http://localhost/1c/demossl # features/steps/web_client.py:8
    When I enter user name Администратор     # features/steps/web_client.py:13
    And I wait until home page is opened     # features/steps/web_client.py:32
    Then I take screenshot to screenshot.png # features/steps/web_client.py:38

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
4 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m5.984s

```
