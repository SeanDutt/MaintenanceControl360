from django.shortcuts import redirect, render
from .models import Comment, Project
from .forms import CommentForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    return render(request, 'pages/home.html')

def projects(request):
    galleries = Project.objects.all()

    context = {
        'galleries': galleries
    }

    return render(request, 'pages/projects.html', context)

def gallery_view(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'pages/gallery.html', {"project":project})

def testimonials(request):
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial submitted successfully. Thank you for your input!')
            return render(request, 'pages/testimonials.html')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)

    else:
        comment_form = CommentForm

    context = {
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'pages/testimonials.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['full_name']
            subject = f"{name} has requested a quote"
            from_email = form.cleaned_data['email_address']
            body = {
            'full_name': form.cleaned_data['full_name'],
            'address': form.cleaned_data['address'],
            'phone_number': form.cleaned_data['phone_number'],
            'email': form.cleaned_data['email_address'],
            'message':form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
                messages.success(request, 'Contact request submitted successfully. We will get back to you ASAP.')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)

      
    form = ContactForm()
    return render(request, "pages/contact.html", {'form':form})