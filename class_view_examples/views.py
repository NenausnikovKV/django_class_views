from datetime import datetime

from django import shortcuts
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, RedirectView, FormView

from .forms import ContactForm
from .models import Publisher


class StandardMethodRequest(View):
    # salutation may be redefined when binding an adress
    salutation = "Hello"

    def get(self, request):
        message = f"Response fo get request {self.salutation}"
        return HttpResponse(message)

    def post(self, request):
        message = f"Response fo post request {self.salutation}"
        return HttpResponse("Response fo post request")

    def head(self, request):

        http_response = HttpResponse(
            headers={"Head-greeting": "head_hello"},
        )
        return http_response


class SimpleTemplate(TemplateView):
    template_name = "class_view_examples/simple_template.html"
    extra_context = {"extra_context": "Extra context"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"custom_context": "Custom context"})
        return context


class SimpleRedirectView(RedirectView):
    permanent = False
    query_string = False
    # url = shortcuts.reverse("class_view_examples:redirect_page")
    pattern_name = "class_view_examples:redirect_page"

    def get_redirect_url(self, *args, **kwargs):
        # some helpful work
        return super().get_redirect_url(*args, **kwargs)


class RedirectStump(View):

    @staticmethod
    def get(request):
        return HttpResponse("Redirect stump")


class PublisherListView(ListView):
    """
        Standard ListView
        default path to list template
        template_name = "class_view_examples/publisher_list.html"
    """
    model = Publisher
    context_object_name = "all_publishers"


class ContactFormView(FormView):
    template_name = "class_view_examples/contact_form.html"
    form_class = ContactForm
    success_url = shortcuts.reverse("class_view_examples:redirect_page")

    def form_valid(self, form):
        return super().form_valid(form)
