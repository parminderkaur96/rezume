from . import views
from django.urls import path
urlpatterns = [
    path("home/",views.Homepage.as_view(),name='home'),
    path("contact/",views.contact,name='contact'),
    path("about/",views.About.as_view(),name='about'),
    path("resume/",views.Resumee.as_view(),name='resume'),
    path("port/",views.Portfolioo.as_view(),name='port'),
    path("detail/<int:pk>/",views.Blogpost,name="detail")
]