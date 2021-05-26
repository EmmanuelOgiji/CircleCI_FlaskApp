Feature: Simple Flask App

Scenario: Render Text After Button is Clicked
    Given I have my browser driver setup
    When I access the homepage of the app
    And I click the button that says Who built this?
    Then Emmanuel Pius-Ogiji is displayed