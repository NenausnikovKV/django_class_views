from django import shortcuts
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, FormView

from .forms import ContactForm
from .models import Publisher


class RootPage(TemplateView):

    # addresses = {
    #     "standard_methods/": reverse_lazy("class_view_examples:standard_method"),
    #     "simple_template/": reverse_lazy("class_view_examples:simple_template"),
    #     "redirection/": reverse_lazy("class_view_examples:class_redirect_view"),
    #     "redirect_stump/": reverse_lazy("class_view_examples:redirect_page"),
    #     "publisher_list/": reverse_lazy("class_view_examples:publisher_view"),
    #     "publisher_detail/<int:pk>/": reverse_lazy("class_view_examples:publisher_detail"),
    #     "contact_form/": reverse_lazy("class_view_examples:contact_form"),
    #     "author_detail/<int:pk>/": reverse_lazy("class_view_examples:author_detail"),
    #     "author/add/": reverse_lazy("class_view_examples:author_add"),
    #     "author/<int:pk>/": reverse_lazy("class_view_examples:author_update"),
    #     "author/<int:pk>/delete/": reverse_lazy("class_view_examples:author_delete"),
    # }

    template_name = "class_view_examples/root_template.html"
    # extra_context = {"addresses": addresses}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_full_url = self.request.build_absolute_uri

        addresses = {
            "standard_methods/": self.request.build_absolute_uri(reverse_lazy("class_view_examples:standard_method")),
            "simple_template/": get_full_url(reverse_lazy("class_view_examples:simple_template")),
            "redirection/": get_full_url(reverse_lazy("class_view_examples:class_redirect_view")),
            "redirect_stump/": get_full_url(reverse_lazy("class_view_examples:redirect_page")),
            "publisher_list/": get_full_url(reverse_lazy("class_view_examples:publisher_view")),
            "publisher_detail/<int:pk>/": get_full_url(reverse_lazy("class_view_examples:publisher_detail", args=(1, ))),
            "contact_form/": get_full_url(reverse_lazy("class_view_examples:contact_form")),
            "author_detail/<int:pk>/": get_full_url(reverse_lazy("class_view_examples:author_detail", args=(1, ))),
            "author/add/": get_full_url(reverse_lazy("class_view_examples:author_add")),
            "author/<int:pk>/": get_full_url(reverse_lazy("class_view_examples:author_update", args=(1, ))),
            "author/<int:pk>/delete/": get_full_url(reverse_lazy("class_view_examples:author_delete", args=(1, ))),
        }
        context.update({"addresses": addresses})
        return context


class StandardMethodRequest(View):
    # salutation may be redefined when binding an adress
    salutation = "Hello"

    def get(self, request):
        message = f"Response fo get request {self.salutation}"
        return HttpResponse(message)

    def post(self, request):
        message = f"Response fo post request {self.salutation}"
        return HttpResponse(message)

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


class PublisherDetailView(DetailView):
    model = Publisher
    # context_object_name = "publisher"

    def get_context_data(self, **kwargs):
        # some useful work
        context = super().get_context_data(**kwargs)
        return context


class ContactFormView(FormView):
    template_name = "class_view_examples/contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy("class_view_examples:redirect_page")

    def form_valid(self, form):
        # some your useful work
        return super().form_valid(form)

