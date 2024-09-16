from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.

# def product_create_view(request):
    
#     form = RawProductForm() # for GET request
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         "form" : form
#     }
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = title = request.POST.get('title')
#         print(my_new_title)
#     # Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    # initial_data = {
    #     'title' : 'my_product'
    # }
    #form = ProductForm(request.POST or None, initial=initial_data)
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id) #prefered method
    #obj = Product.objects.get(id=1)
    if request.method == "POST": #Confirms deletion. Doesn't actually delete.
        obj.delete()
        return redirect('../../')
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {
        'object': obj,
    }
    return render(request, "products/product_delete.html", context)


# def render_initial_data(request):
#     initial_data = {
#         'title' : 'my_product'
#     }
#     form = RawProductForm(request.POST or None, initial=initial_data)
#     context = {
#         'form' : form
#     }
#     return render(request, 'products/product_create.html', context)

def dynamic_lookup_view(request, id):
    obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id) #prefered method
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        'object' : obj
    }
    return render(request, 'products/product_detail.html', context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, "products/product_list.html", context)