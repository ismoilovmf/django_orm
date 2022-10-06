from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'max_price':
        phones = phones.order_by('-price')
    else:
        phones = phones.order_by('price')
    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    s = ' '.join(slug.split("-")).title()
    # i = Phone.objects.filter(name=s) #почему-то так не получилось
    for i in Phone.objects.all():
        if i.name == s:
            context = {"phone": i}
            break
    return render(request, template, context)
