from django.urls import path

from . import views

app_name = "class_view_examples"
urlpatterns = [
    path("", views.RootPage.as_view(), name="root"),
    path("standard_methods/", views.StandardMethodRequest.as_view(salutation="Hi"), name="standard_method"),
    path("simple_template/", views.SimpleTemplate.as_view(), name="simple_template"),
    path("redirection/", views.SimpleRedirectView.as_view(), name="class_redirect_view"),
    path("redirect_stump/", views.RedirectStump.as_view(), name="redirect_page"),
    path("publisher_list/", views.PublisherListView.as_view(), name="publisher_view"),
    path("publisher_detail/<int:pk>", views.PublisherDetailView.as_view(), name="publisher_detail"),
    path("contact_form/", views.ContactFormView.as_view(), name="contact_form"),
    path("author_detail/<int:pk>", views.AuthorDetailView.as_view(), name="author_detail"),
    path("author/add/", views.AuthorCreateView.as_view(), name="author_add"),
    path("author/<int:pk>/", views.AuthorUpdateView.as_view(), name="author_update"),
    path("author/<int:pk>/delete/", views.AuthorDeleteView.as_view(), name="author_delete"),
]
