"""
Requires chromedriver, this should also be approved
"""
from assertpy import assert_that
from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@given(u'I have my webdriver setup')
def step_impl(context):
    # setup webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # set as headless as we don't need to view UI
    options.add_argument('--disable-dev-shm-usage')  # set flag to reduce memory usage
    context.driver = webdriver.Chrome(
        options=options
    )


@when(u'I access the homepage of the app')
def step_impl(context):
    # get url from command line userdata
    url = context.config.userdata['url']

    # go to url
    context.driver.get(url)

    # wait for button to appear with max timeout of 15 secs
    WebDriverWait(context.driver, 15).until(
        ec.presence_of_element_located((By.ID, "testButton"))
    )


@when(u'I click the button that says Who built this?')
def step_impl(context):
    # find button
    button = context.driver.find_element_by_id("testButton")

    # click button
    button.click()

    # wait for page to render
    WebDriverWait(context.driver, 15).until(
        ec.visibility_of_all_elements_located
    )


@then(u'Emmanuel Pius-Ogiji is displayed')
def step_impl(context):
    # check that page contains "Emmanuel Pius-Ogiji"
    assert_that(context.driver.page_source).contains("Emmanuel Pius-Ogiji")


def after_all(context):
    # Clean up
    context.driver.quit()

