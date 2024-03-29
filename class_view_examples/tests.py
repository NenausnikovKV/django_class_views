from django import shortcuts
from django.test import TestCase, Client

from . import forms
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

    def test_redirect_stump(self):
        address = shortcuts.reverse("class_view_examples:redirect_page")
        response = self.client.get(address)
        self.assertContains(response, text="Redirect stump")

    def test_redirect_class_view(self):
        address = shortcuts.reverse("class_view_examples:class_redirect_view")
        correct_redirect_address = shortcuts.reverse("class_view_examples:redirect_page")
        response = self.client.get(address)
        self.assertRedirects(response, correct_redirect_address)

    def test_publisher_view_list(self):
        # todo rewrite create and remove publisher model as 'with as'
        publisher_name = "Fyodor"
        Publisher.objects.create(name=publisher_name, address="Vorkuta")

        address = shortcuts.reverse("class_view_examples:publisher_view")
        response = self.client.get(address)
        self.assertContains(response, text="Publishers", status_code=200)
        self.assertContains(response, text=publisher_name, status_code=200)
        self.assertTemplateUsed(response, template_name="class_view_examples/publisher_list.html")

        Publisher.objects.filter(name=publisher_name).delete()

    def test_publisher_view_detail(self):
        publisher_name = "Fyodor"
        publisher = Publisher.objects.create(name=publisher_name, address="Vorkuta")
        famous_author = Author.objects.create(name="Someone famous")
        book = Book.objects.create(title="Tails", publisher=publisher)
        book.authors.set([famous_author])

        address = shortcuts.reverse("class_view_examples:publisher_detail", args=(1,))
        response = self.client.get(address)
        self.assertContains(response, text=publisher.name)
        self.assertContains(response, text=book.title)

        Publisher.objects.filter(name=publisher_name).delete()

    def test_contact_form_view(self):
        address = shortcuts.reverse("class_view_examples:contact_form")
        response = self.client.get(address)
        self.assertContains(response, text="Name")
        self.assertTemplateUsed(response, template_name="class_view_examples/contact_form.html")

        post_data = {"name": "Lucy", "message": "Hi"}
        response = self.client.post(address, data=post_data)
        redirect_address = shortcuts.reverse("class_view_examples:redirect_page")
        self.assertRedirects(response, redirect_address)

        # message is a required field
        not_valid_data = {"name": "Lucy", "message": ""}
        response = self.client.post(address, data=not_valid_data)
        redirect_address = shortcuts.reverse("class_view_examples:redirect_page")
        self.assertTemplateUsed(response, template_name="class_view_examples/contact_form.html")

    def test_unbound_contact_form(self):
        unbound_form = forms.ContactForm()
        self.assertFalse(unbound_form.is_bound)
        name_field = unbound_form["name"]
        message_field = unbound_form["message"]
        self.assertEquals(name_field.initial, "Ivan")
        self.assertEquals(message_field.initial, "Ivan message")

    def test_bound_contact_form(self):
        bound_form = forms.ContactForm({"name": "Alex", "message": "hello"})
        self.assertTrue(bound_form.is_bound)
        self.assertTrue(bound_form.is_valid())
        incorrect_form = forms.ContactForm({"name": "", "message": "hello"})
        self.assertFalse(incorrect_form.is_valid())
        self.assertFormError(incorrect_form, field="name", errors="This field is required.")


    def test_author_crud(self):
        name = "Emperor"
        author = Author.objects.create(name=name)
        next_pk = author.pk + 1

        detail_address = shortcuts.reverse("class_view_examples:author_detail", kwargs={"pk": author.pk})
        detail_response = self.client.get(detail_address)
        self.assertTemplateUsed(detail_response, template_name="class_view_examples/author_detail.html")
        self.assertContains(detail_response, text=name)

        create_address = shortcuts.reverse("class_view_examples:author_add")
        create_get_response = self.client.get(create_address)
        self.assertTemplateUsed(create_get_response, template_name="class_view_examples/author_form.html")
        create_name = "son of Emperor"
        create_post_response = self.client.post(create_address, data={"name": create_name})
        new_author_detail_address = shortcuts.reverse("class_view_examples:author_detail", kwargs={"pk": next_pk})
        self.assertRedirects(create_post_response, new_author_detail_address)

        update_address = shortcuts.reverse("class_view_examples:author_update", kwargs={"pk": next_pk})
        update_get_response = self.client.get(update_address)
        self.assertTemplateUsed(update_get_response, template_name="class_view_examples/author_form.html")
        update_name = "daughter of Emperor"
        update_post_response = self.client.post(update_address, data={"name": update_name})
        new_author_detail_address = shortcuts.reverse("class_view_examples:author_detail", kwargs={"pk": next_pk})
        self.assertRedirects(update_post_response, new_author_detail_address)

        delete_address = shortcuts.reverse("class_view_examples:author_delete", kwargs={"pk": next_pk})
        delete_get_response = self.client.get(delete_address)
        self.assertTemplateUsed(delete_get_response, template_name="class_view_examples/author_confirm_delete.html")
        delete_post_response = self.client.post(delete_address, data={"pk": next_pk})
        correct_redirect_address = shortcuts.reverse("class_view_examples:redirect_page")
        self.assertRedirects(delete_post_response, correct_redirect_address)

        author.delete()
