# home/views/signin.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..forms.forms import CustomerLoginForm


def signin_view(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Điều hướng về trang chủ sau khi đăng nhập thành công
                return redirect('homepage')
            else:
                # Thêm lỗi tổng thể (hiển thị ở form.non_field_errors trong template)
                form.add_error(None, "Invalid username or password.")
    else:
        form = CustomerLoginForm()

    return render(request, 'signin.html', {'form': form})