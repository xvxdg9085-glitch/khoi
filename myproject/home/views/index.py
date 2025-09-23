from django.shortcuts import render

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