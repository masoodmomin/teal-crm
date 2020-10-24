from django.shortcuts import render, redirect
from .models import Customer, Product, Order
from .filters import ProductFilter
from .forms import Form, ProductForm, ContactForm
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

@login_required
def dashboard(request):
    orders = Order.objects.all()
    orders_label = set()
    for o in orders:
        orders_label.add(o.product)
    orders_group = list(Order.objects.values('product').annotate(dcount=Count('product')))
    og = []
    for o in orders_group:
        og.append(o["dcount"])
    total_orders = orders.count()
    recent_orders = orders.order_by('-date_created')[:5]
    context  = {'orders': orders, 'orders_label': orders_label, 'products': products,
    'total_orders':total_orders, 'recent_orders':recent_orders,'og':og}
    return render(request,'crm/dashboard.html', context)

@login_required
def products(request):
    products = Product.objects.all()
    pf = ProductFilter(request.GET, queryset=products)
    products = pf.qs
    return render(request,'crm/products.html',{'products':products,'pf':pf})

@login_required
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products')
    context = {'form': form}
    return render(request,'crm/form_page.html',context)

@login_required
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    context = {'form':form}
    return render(request,'crm/form_page.html', context)

@login_required
def orders(request):
    orders = Order.objects.order_by("-date_created")
    return render(request,'crm/orders.html',{'orders':orders})

@login_required
def contacts(request):
    req = request.GET.get('search',None)
    if req is not None:
        query = request.GET.get('search')
        customers = Customer.objects.filter(Q(name__icontains=query) | Q(email__icontains=query)
        | Q(phone__icontains=query)
        | Q(address__icontains=query))
    else:
        customers = Customer.objects.all()
    return render(request,'crm/contacts.html',{'customers':customers})

@login_required
def add_contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contacts')
    context = {'form':form}
    return render(request,"crm/form_page.html",context)

@login_required
def update_contact(request, pk):
    contact = Customer.objects.get(id=pk)
    form = ContactForm(instance=contact)
    if request.method == 'POST':
        form = ContactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/contacts')
    context = {'form': form}
    return render(request,'crm/form_page.html',context)

@login_required
def delete_contact(request, pk):
    contact = Customer.objects.get(id=pk)
    contact.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def customer_orders(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    total_orders = order.count()
    context = {'customer':customer,'order':order, 'total_orders':total_orders}
    return render(request,'crm/customer_orders.html', context)

@login_required
def create_order(request):
    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/orders')
    context = {'form':form}
    return render(request,'crm/form_page.html', context)

@login_required
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = Form(instance=order)
    if request.method == 'POST':
        form = Form(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/orders')
    context = {'form': form}
    return render(request,'crm/form_page.html',context)
    
@login_required
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Username or Password is not correct.")
    return render(request, 'crm/signin.html',{})

def signout(request):
    logout(request)
    return redirect('signin')