from django import shortcuts
from django.test import TestCase, Client

from .models import Publisher, Book, Author


class ClassViewTEst(TestCase):
    client = Client()


    def test_standard_method_request(self):
        # todo add test for salutation
        address = shortcuts.reverse("class_view_examples:standard_method")
        get_response = self.client.get(address)
        self.assertContains(get_response, text="get")
        post_response = self.client.post(address)
        self.assertContains(post_response, text="post", status_code=200)
        head_response = self.client.head(address)
        self.assertEquals(head_response.headers["Head-greeting"], "head_hello")


    def test_simple_template(self):
        address = shortcuts.reverse("class_view_examples:simple_template")
        response = self.client.get(address)
        self.assertContains(response, text="Hello", status_code=200)
        self.assertContains(response, text="Extra context")
        self.assertContains(response, text="Custom context")


    def test_publisher_view_list(self):
        # todo rewrite create and remove publisher model as 'with as'
        publisher_name = "Fyodor"
        Publisher.objects.create(name=publisher_name, address="Vorkuta")

        address = shortcuts.reverse("class_view_examples:publisher_view")
        response = self.client.get(address)
        self.assertContains(response, text="Publishers", status_code=200)
        self.assertContains(response, text=publisher_name, status_code=200)

        Publisher.objects.filter(name=publisher_name).delete()


    def test_publisher_view_detail(self):
        publisher_name = "Fyodor"
        publisher = Publisher.objects.create(name=publisher_name, address="Vorkuta")
        famous_author = Author.objects.create(name="Someone famous")
        book = Book.objects.create(title="Tails", authors=[famous_author], publiser=publisher)

        address = shortcuts.reverse("class_view_examples:publisher_detail")
        response = self.client.get(address)
        self.assertContains(response, text=publisher.name)
        self.assertContains(response, text=book.name)

        Publisher.objects.flilter(name=publisher_name).delete()


