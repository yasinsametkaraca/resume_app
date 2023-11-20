from django.http import JsonResponse
from django.shortcuts import render


def contact_form(request):
    context = {
        'success': True,
        'message': 'Thanks for your message! Contact form sent successfully.'
    }
    return JsonResponse(context)


def contact(request):
    return render(request, 'contact.html')
