"""Simple unit tests for the blog app.

This module demonstrates how to test Django views with ``TestCase``.  Each
test runs inside its own transaction and uses the built-in test client to
simulate HTTP requests.
"""

from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogIndexViewTests(TestCase):
    """Tests for the blog index view using Django's ``TestCase``.

    ``TestCase`` sets up a temporary database and a special ``self.client``
    object for simulating HTTP requests.  Every method prefixed with
    ``test_`` is run as an isolated test case.
    """

    def setUp(self) -> None:
        """Create a sample ``Post`` before each test.

        Steps:
        1. Call ``Post.objects.create`` with a title and body.
        2. Store the resulting object on ``self.post`` so tests can use it.
        """
        self.post = Post.objects.create(title="Test Post", body="This is a test post")

    def test_index_returns_success(self):
        """The index view should respond with HTTP 200.

        Steps:
        1. Build the index URL with ``reverse``.
        2. Issue a ``GET`` request using the test client.
        3. Assert that ``response.status_code`` equals ``200``.
        """
        response = self.client.get(reverse("blog_index"))
        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        """The index view should render ``blog/index.html``.

        Steps:
        1. Send a GET request to the index URL.
        2. Use ``assertTemplateUsed`` to confirm the response used that
           template.
        """
        response = self.client.get(reverse("blog_index"))
        self.assertTemplateUsed(response, "blog/index.html")

