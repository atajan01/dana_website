from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("home/", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("courses/", views.courses, name='courses'),
    path("group/<int:id>/", views.group_spec, name='group_spec'),
    path("blog/", views.blog, name='blog'),
    path("contact/", views.contact, name='contact'),
    path("save_contact/", views.save_contact, name='save_contact'),
    
    
]



