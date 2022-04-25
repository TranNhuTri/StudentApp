from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        'name': 'Tran Nhu Tri',
        'skills': ['html', 'css', 'js', '.net', 'django'],
        'content': '<div class="alert alert-primary" role="alert">Hello Django!</div>'
    }
    return render(request, 'home.html', context)

def about_view(request):
    return render(request, 'about.html', {})

def contact_view(request):
    return render(request, 'contact.html', {})
