from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about-us.html')

def blogdetails(request):
    return render(request, 'blog-details.html')


def blog(request):
    return render(request, 'blog.html')


def cardetails(request):
    return render(request, 'car-detail.html')


def cars(request):
    return render(request, 'cars.html')


def contact(request):
    return render(request, 'contact.html')


def home(request):
    return render(request, 'index.html')


def team(request):
    return render(request, 'team.html')


def terms(request):
    return render(request, 'terms.html')


def testimonials(request):
    return render(request, 'testimonials.html')