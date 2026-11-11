from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.home,name="home"),
    path("about/", views.about,name="about"),
    path("service/", views.service,name="service"),
    path("contact/", views.contact,name="contact"),
    path("product/", views.product,name="product"),
    path("registration/",views.registration,name="registration"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("update/<int:pk>",views.update,name="update"),
    path("delete/<int:jk>",views.delete,name="delete"),
    path("product11/",views.product11,name="product11"),
    path("registration22/",views.registration22,name="registration22")

]