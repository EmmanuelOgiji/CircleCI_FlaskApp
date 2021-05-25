"""
As a user of this app,
when I click the button that says 'Who built this?'
then I get the name of who developed this "Emmanuel Pius-Ogiji"

Git testing
"""
import logging

from flask import Flask, render_template, request, render_template_string

logger = logging.getLogger()
logging.basicConfig(level="INFO")
logger.setLevel("INFO")

app = Flask(__name__)


@app.route('/')
def home_page():
    logger.info("Rendering home page")
    return render_template("home.html")


@app.route('/', methods=['POST'])
def button_click():
    if request.form.get('action1') == 'Who built this?':
        return render_template_string("Emmanuel Pius-Ogiji")


if __name__ == '__main__':
    app.run()
