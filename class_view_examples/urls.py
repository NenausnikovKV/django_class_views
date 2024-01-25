from django.urls import path

from . import views

app_name = "class_view_examples"
urlpatterns = [
    path("simple_template/", views.SimpleTemplate.as_view(), name="simple_template"),
    path("standard_methods/", views.StandardMethodRequest.as_view(salutation="Hi"), name="standard_method"),
    path("publisher_list/", views.PublisherListView.as_view(), name="publisher_view"),
    path("publisher/", views.PublisherDetailView.as_view(), name="publisher_detail"),
]
