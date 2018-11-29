# selenium_chrome_smoke
Start 1C:Enterprise web-client with selenium and chromedriver, authenticate and wait until home page is opened via BDD feature

```bash
pip install -r requirements.txt
behave
```

Example output

```
selenium_chrome_smoke>behave

DevTools listening on ws://127.0.0.1:61075/devtools/browser/81f1cd0d-549c-4cfd-8f5c-3484dda598b2
Feature: Smoke test # features/smoke.feature:2

  Scenario: Smoke                            # features/smoke.feature:4
    Given I goto http://localhost/1c/demossl # features/steps/web_client.py:8
    When I enter user name Администратор     # features/steps/web_client.py:13
    Then I wait until home page is opened    # features/steps/web_client.py:32

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m5.795s

```

Example run with allure and junit report
```bash
pip install -r requirements.txt
pip install allure-behave
behave -f allure_behave.formatter:AllureFormatter -o allure_result  --junit --junit-directory junit
allure serve allure_result
```

[Youtube guide](https://youtu.be/fxlNoI-2Acc)