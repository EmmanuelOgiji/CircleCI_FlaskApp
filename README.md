# CircleCI_FlaskApp

## Overview
This is a project that has the following:
- A simple flask app which renders a template with a button titled "Who built this?"
- When this button is clicked, a new template is rendered with the text "Emmanuel Pius-Ogiji"
- The project also contains a BDD test that confirms this functionality. The test uses behave and selenium webdriver

The Feature is summarised as below:

### Feature: Simple Flask App

- Scenario: Render Text After Button is Clicked
    - Given I have my chromium browser and chrome setup
    - When I access the homepage of the app
    - And I click the button that says Who built this?
    - Then Emmanuel Pius-Ogiji is displayed
    
## Usage
Note that the necessary python dependencies are available in the requirements.txt
- To run the app locally, 
    - python ${PATH_TO_REPO}/src/app.py
- To run tests, this requires chromium-chromedriver installed and added to path
    - cd ${PATH_TO_REPO}/test/features
    - behave -D url=${server_url}