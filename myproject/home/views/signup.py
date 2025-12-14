# home/views.py

from django.shortcuts import render, redirect
from ..forms.forms import CustomerRegistrationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Tạo mới khách hàng
            return redirect('signin')  # Điều hướng đến trang đăng nhập
    else:
        form = CustomerRegistrationForm()

    return render(request, 'signup.html', {'form': form})
