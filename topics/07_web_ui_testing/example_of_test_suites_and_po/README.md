# Introduction
This folder contains filew with PO and test suites to demo different version of Web UI automation tests


## Files

1) selenium_test_demo.py:
It is a simple example of selenium webdriver test

CL command
```bash
python .\selenium_test_demo.py
```

2) test_login_page_not_pytest.py
- The separated Playwright suit (without pytest)

CL command
```bash
python .\test_login_page_not_pytest.py
```

3) login_page_object.py - PO for test suit test_login_page.py
- It uses Pytest fixture

CL command
```bash
pytest .\test_login_page.py
```

4) product_page_object.py - PO for test suit test_product_page.py
- It use Pytest fixture and consume data from conftest.py
- It incorporates functionality of login_page_object.py and test suit test_login_page.py

CL command
```bash
pytest .\test_product_page.py
```

5) conftest.py
- It is a service file that is required for Pytest. It is consumed by test_product_page.py
