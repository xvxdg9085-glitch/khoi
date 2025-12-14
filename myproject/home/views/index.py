from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def index_view(request):
    return render(request, 'index.html')

def forgot_password(request):
    return render(request, 'page-forgot-password.html')
def pricing(request):
    return render(request, 'pricing.html')
def how_it_works(request):
    return render(request, 'how_it_works.html')
def about(request):
    return render(request, 'about.html')
def faq(request):
    return render(request, 'faq.html')
def services(request):
    return render(request, 'services.html')
def error_404_view(request, exception=None):
    return render(request, '404.html', status=404)
def logout_view(request):
    logout(request)
    return redirect('signin')