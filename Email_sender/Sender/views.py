from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    context = {
        'title' : 'Homepage'
    }
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        send_mail(
            message_name,
            message,
            message_email,
            ['rono2170@gmail.com']
        )

        context['message_name'] = message_name

        return render(request, 'Sender/home.html', context)

    else:
        return render(request, 'Sender/home.html', context)