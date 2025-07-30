from django.shortcuts  import render,redirect
from.models  import Contactmessage
from django.core.mail import send_mail
from django.conf  import settings

 

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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contactmessage.objects.create(
        name =name,
        email =email,
        subject =subject,
        message =message,
    )

 

        body =f""" 

        name:{name}
        email:{email}
        subject:{subject}
        

        message:
        {message}
        """



        send_mail(
            subject= subject,
            message= body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['alaoopeyemi740@gmail.com'],
            fail_silently=False,

        )

        return redirect('contact')
    return render(request, 'contact.html')



    
    
    message.success(request, "Your message has been sent. Thank you!")
    return redirect('contact')

    return render(request, 'contact.html')
 




def home(request):
    return render(request, 'index.html')


def team(request):
    return render(request, 'team.html')


def terms(request):
    return render(request, 'terms.html')


def testimonials(request):
    return render(request, 'testimonials.html')