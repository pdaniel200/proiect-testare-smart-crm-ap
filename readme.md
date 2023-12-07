# Testing login, running and stopping the timer, creating and deleteing task and various operations on the app.smart-crm.ro webpage, Chrome, Firefox and Edge



# Version

* Python 3.10

# Run

1. Open a terminal
2. Go to the root directory of the project "/ap-testing-project/".
3. Create a virtual environment: `py -m venv venv`
4. Activate the virtual environment: `.\venv\Scripts\activate`
5. Download the required libraries: `pip install -r requirements.txt`

# Test execution

1. Open a terminal
2. For the version wich takes in consideration the config.yaml options to setup the browser type and the headless option start:
   From the project root directory run: `pytest Tests/test_login_smart_crm_config.py --html=Results/report_test_login_pt.html`
3. For the version with default chromedriver start:
   From the project root directory run: `pytest Tests/test_login_smart_crm.py --html=Results/report_test_login_smart_crm.html`

# You can choose a type of brower from wich yo can run the test chrome/firefox/edge
1. browser: chrome
2. browser: firefox
3. browser: edge

The tests will be executed in Chrome but can be modified in the "/data/config.yaml" file to also be executed in Firefox or Edge

# Browser visibility when running the test: True or False
1. headless: False - the browser will be visible while executing the test
2. headless: True - the browser will not be visible while executing the test.

# Results

To check the report, open '/results/report.html' once the test has finished.

# Screenshots are taken at every major step

To check the report, open '/Results/
