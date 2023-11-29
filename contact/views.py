from django.http import JsonResponse
from django.shortcuts import render
from .models import Message
from .forms import ContactForm


def contact_form(request):
    if request.POST:
        contact_form = ContactForm(request.POST or None)  # Burada formu oluşturuyoruz. Eğer post varsa formu dolduruyoruz ve validasyona sokuyoruz. Eğer post yoksa boş form oluşturuyoruz.
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message_text = request.POST.get('message')
            Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text
            )
            message = "Thanks for your message! Contact form sent successfully."
            success = True
        else:
            message = 'Please check the form.'
            success = False
    else:
        success = False
        message = 'Something went wrong. Please try again.'

    context = {
        "message": message,
        "success": success
    }

    return JsonResponse(context)


def contact(request):
    contact_form = ContactForm()
    context = {
        "contact_form": contact_form  # Bu sayfaya formu gönderme sebebimiz bu contact form içindeki validasyonları html içerisinde kullanmak için.
    }
    return render(request, 'contact.html', context)
