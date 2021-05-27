# CircleCI_FlaskApp

## Overview
This is a python3 project that has the following:
- A simple flask app which renders a template with a button titled "Who built this?"
- When this button is clicked, a new template is rendered with the text "Emmanuel Pius-Ogiji"
- The project contains unit tests which check the functionality on a low level
- The project also contains a BDD test that confirms this functionality. The test uses behave and selenium webdriver

The Feature is summarised as below:

### Feature: Simple Flask App

- Scenario: Render Text After Button is Clicked
    - Given I have my browser setup
    - When I access the homepage of the app
    - And I click the button that says Who built this?
    - Then Emmanuel Pius-Ogiji is displayed
    
## Usage
Note that the necessary python dependencies are available in the requirements.txt. These can be installed by running the command "pip install -r requirements.txt"
- To run the app locally, 
    - python ${PATH_TO_REPO}/src/app.py
- To run unit tests,
    - cd ${PATH_TO_REPO}
    - python -m unittest discover -s test.unit_test
- To run post_deploy_test, this requires chromium-chromedriver installed and added to path
    - cd ${PATH_TO_REPO}/test/post_deploy_test/features
    - behave -D url=${server_url}
    
The app is deployed to heroku at: https://flask-circleci-epo.herokuapp.com/