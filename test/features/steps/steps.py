"""
Requires chromedriver, this should also be approved
"""
from assertpy import assert_that
from behave import *

from selenium import webdriver

url = "http://127.0.0.1:5000/"


@given(u'I access the app')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@when(u'I click the button that says Who built this?')
def step_impl(context):
    button = context.driver.find_element_by_id("testButton")
    button.click()


@then(u'Emmanuel Pius-Ogiji is rendered')
def step_impl(context):
    assert_that(context.driver.page_source).contains("Emmanuel Pius-Ogiji")
