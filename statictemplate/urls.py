from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('contact',views.contact ,name="contact"),
    path('index',views.index),
    path('blog',views.blog),
    path('about',views.about),
    path('projects',views.projects),
    path('proj1',views.proj1),
    path('singlepost',views.singlepost),
    path('contactsend',views.contactsend),
    path('test',views.test),
]
