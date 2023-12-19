from portfolio_v2.forms import ContactForm
from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            message = form.cleaned_data['message']
            EmailMessage(
                'Contact Form Submission from {}'.format(name),
                message,
                ['sena.stefano@gmail.com'],
                [],
                reply_to=[email]
            ).send()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return HttpResponse('cool, it worked')