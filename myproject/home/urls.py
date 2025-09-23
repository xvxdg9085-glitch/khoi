from django.urls import path
from .views import index
from .views.post import post_detail, post_list
from .views import signup

urlpatterns = [
    path('', index.index_view, name='homepage'),
    path('post', post_list, name='post'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
    path('forgot-password', index.forgot_password, name='forgot_password'),
    path('pricing', index.pricing, name='pricing'),
    path('how-it-works', index.how_it_works, name='how_it_works'),
    path('about', index.about, name='about'),
    path('faq', index.faq, name='faq'),
    path('signup', signup.signup_view, name='signup'),
]