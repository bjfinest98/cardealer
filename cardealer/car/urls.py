from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blogdetails/', views.blogdetails, name="blogdetails"),
    path('blog/', views.blog, name="blog"),
    path('cardetails/', views.cardetails, name="cardetails"),
    path('cars/', views.cars, name="cars"),
    path('contact/', views.contact, name="contact"),
    path('team/', views.team, name="team"),
    path('terms/', views.terms, name="terms"),
    path('testimonials/', views.testimonials, name="testimonials"),
    
]



