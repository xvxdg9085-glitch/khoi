from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Product


def product_list(request):
    product_list = Product.objects.all().order_by('-id')
    paginator = Paginator(product_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products/product_list.html", {'page_obj': page_obj})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    images = product.images.all()
    return render(request, 'products/product_detail.html', {
        'product': product,
        'images': images,
    })