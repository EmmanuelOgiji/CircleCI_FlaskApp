"""
Requires chromedriver, this should also be approved
"""
from assertpy import assert_that
from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@given(u'I access the app')
def step_impl(context):
    url = context.config.userdata['url']
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    WebDriverWait(context.driver, 15).until(ec.presence_of_element_located((By.ID, "testButton")))


@when(u'I click the button that says Who built this?')
def step_impl(context):
    button = context.driver.find_element_by_id("testButton")
    button.click()
    WebDriverWait(context.driver, 15).until(ec.visibility_of_all_elements_located)


@then(u'Emmanuel Pius-Ogiji is rendered')
def step_impl(context):
    assert_that(context.driver.page_source).contains("Emmanuel Pius-Ogiji")
