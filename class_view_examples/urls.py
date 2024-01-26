from django.urls import path

from . import views

app_name = "class_view_examples"
urlpatterns = [
    path("standard_methods/", views.StandardMethodRequest.as_view(salutation="Hi"), name="standard_method"),
    path("simple_template/", views.SimpleTemplate.as_view(), name="simple_template"),
    path("redirection/", views.SimpleRedirectView.as_view(), name="class_redirect_view"),
    path("redirect_stump/", views.RedirectStump.as_view(), name="redirect_page"),
    path("publisher/", views.PublisherListView.as_view(), name="publisher_view"),

]
