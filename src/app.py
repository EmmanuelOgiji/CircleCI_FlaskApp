"""
Scenario: Render Text After Button is Clicked
    Given I have my browser setup
    When I access the homepage of the app
    And I click the button that says Who built this?
    Then Emmanuel Pius-Ogiji is displayed

Git testing
"""
import logging

from flask import Flask, render_template, render_template_string

logger = logging.getLogger()
logging.basicConfig(level="INFO")
logger.setLevel("INFO")

app = Flask(__name__)


@app.route('/')
def home_page():
    logger.info("Rendering home page")
    return render_template("home.html")


@app.route('/author')
def button_click():
    logger.info("Rendering author page")
    return render_template_string("Emmanuel Pius-Ogiji")


if __name__ == '__main__':
    app.run()  # pragma: no cover
