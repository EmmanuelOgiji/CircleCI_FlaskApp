from unittest import TestCase

from assertpy import assert_that

from src.app import app


class SetupTestCase(TestCase):
    def setUp(self):
        self.tester = app.test_client(self)


class FlaskAppTests(SetupTestCase):
    def test_home_page_gives_200_response(self):
        response = self.tester.get('/')
        assert_that(response.status_code).is_equal_to(200)

    def test_author_page_gives_200_response(self):
        response = self.tester.get('/author')
        assert_that(response.status_code).is_equal_to(200)

    def test_author_page_contains_the_right_text(self):
        response = self.tester.get('/author')
        assert_that(response.data.decode('utf-8')).contains("Emmanuel Pius-Ogiji")
