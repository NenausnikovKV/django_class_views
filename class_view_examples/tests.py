from django import shortcuts
from django.test import TestCase, Client


class ClassViewTEst(TestCase):
    client = Client()

    def test_simple_template(self):
        address = shortcuts.reverse("class_view_examples:simple_template")
        response = self.client.get(address)
        self.assertContains(response, text="Hello", status_code=200)

    def test_standard_method_request(self):
        address = shortcuts.reverse("class_view_examples:standard_method")
        get_response = self.client.get(address)
        self.assertContains(get_response, text="get", status_code=200)
        post_response = self.client.post(address)
        self.assertContains(post_response, text="post", status_code=200)

        head_response = self.client.head(address)
        self.assertEquals(head_response.headers["Head-greeting"], "head_hello")

    def test_publisher_view_list(self):
        address = shortcuts.reverse("class_view_examples:publisher_view")
        get_response = self.client.get(address)
        self.assertContains(get_response, text="Publishers", status_code=200)



