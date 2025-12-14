from ..models import ProductCategory
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

def category_list_view(request):
    categories = ProductCategory.objects.filter(is_active=True)
    return render(request, 'category_list.html', {'categories': categories})

def product_by_category(request, category_id):
    category = get_object_or_404(ProductCategory, id=category_id)
    products = category.products.all().order_by('-created_at')
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/product_list.html', {
        'category': category,
        'page_obj': page_obj,
    })