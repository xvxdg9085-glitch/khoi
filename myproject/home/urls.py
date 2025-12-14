from django.urls import path
from .views import signup, signin, index, post,category,product

urlpatterns = [
    path('', index.index_view, name='homepage'),
    path('post', post.post_list, name='post'),
    path('post/<int:post_id>', post.post_detail, name='post_detail'),
    path('forgot-password', index.forgot_password, name='forgot_password'),
    path('pricing', index.pricing, name='pricing'),
    path('how-it-works', index.how_it_works, name='how_it_works'),
    path('about', index.about, name='about'),
    path('faq', index.faq, name='faq'),
    path('signup', signup.signup_view, name='signup'),
    path('signin', signin.signin_view, name='signin'),
    path('logout', index.logout_view, name='logout'),
    path('services', index.services, name='services'),
    path('categories/', category.category_list_view, name='category_list'),
    path('categories/', category.category_list_view, name='category_list'),
    path('category/<int:category_id>/products/',
         category.product_by_category, name='product_by_category'),
    path("products/", product.product_list, name="product_list"),
    path('product/<int:product_id>/',
         product.product_detail, name='product_detail'),
    path('404', index.error_404_view, name='error_404'),
]