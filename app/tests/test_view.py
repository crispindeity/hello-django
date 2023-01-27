from django.test import TestCase


class TestView(TestCase):
    def test_add_view(self) -> None:
        result = self.client.get("/app")
        self.assertEqual(result.status_code, 301)
