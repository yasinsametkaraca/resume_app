from django.http import JsonResponse
from django.shortcuts import render
from .models import Message


def contact_form(request):

    if request.POST:
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
        success = False
        message = 'Something went wrong. Please try again.'

    context = {
        "message": message,
        "success": success
    }

    return JsonResponse(context)


def contact(request):
    return render(request, 'contact.html')
