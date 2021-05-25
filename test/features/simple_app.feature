Feature: Simple Flask App

Scenario: Render Text After Button is Pressed
    Given I access the app
    When I click the button that says Who built this?
    Then Emmanuel Pius-Ogiji is rendered