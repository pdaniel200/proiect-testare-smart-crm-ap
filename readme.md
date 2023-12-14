# Test for creating and deleteing tasks and various operations, using Chrome, Firefox and Edge



# Version
* Python 3.10

# Run
1. Open a terminal
2. Go to the root directory of the project "/proiect-testare-smart-crm-ap/".
3. Create a virtual environment: `py -m venv venv`
4. Activate the virtual environment: `.\venv\Scripts\activate`
5. Download the required libraries: `pip install -r requirements.txt`

# Test execution
1. Open a terminal
2. From the project root directory run: `pytest Tests/test_smart_crm_config.py --html=Results/report_test_smart_crm.html`
   if you just type: `pytest Tests/test_smart_crm_config.py` the result files would be stored on the folder `Results` and in the html test report filename will include the browser type: `report_test_smart_crm_browser_` + {browser_type} + `.html`


# You can choose a type of browser from wich yo can run the test chrome/firefox/edge
1. browser: chrome
2. browser: firefox
3. browser: edge

The tests will be executed in Chrome but can be modified in the "/data/config.yaml" file to also be executed in Firefox or Edge

# Browser visibility when running the test: True or False
1. headless: False - the browser will be visible while executing the test
2. headless: True - the browser will not be visible while executing the test.

# Option to test with the local webdriver or remote with WebDriver Manager
1. webdriver: local - the webdriver will be launched from the drvweb folder
2. webdriver: remote - the webdriver will be installed by WebDriver Manager

# Results
To check the report, open '/results/report.html' once the test has finished.

# Screenshots are taken at every major step
To check the report, open '/Results/
