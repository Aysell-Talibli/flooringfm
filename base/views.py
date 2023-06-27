from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Max
from django.db.models import Q
def home(request):
    about=About.objects.last()
    home_data=Slider.objects.all()
    categories=Category.objects.all()
    portfolios=Portfolio.objects.all()
    portfolio_categories=PortfolioCategory.objects.all()
    blogs=Blog.objects.all()
    partners=Partner.objects.all()
    social_medias=SocialMedia.objects.all()
    main_info=Main.objects.last()
    facts=FunFact.objects.all()
    form=HomeApplyForm()
    form2=EmailForm()
    if request.method=='POST':
        if request.POST.get("subscription_email"):
            form2=EmailForm(request.POST)
            if form2.is_valid():
                form2.save()
        else:
            form=HomeApplyForm(request.POST)
            if form.is_valid():
                form.save()
     
    current_category=request.GET.get('category')
    
    category_first=PortfolioCategory.objects.first()
    if current_category == None:
        portfolios=Portfolio.objects.filter(category__name=category_first)
    else:
        portfolios=Portfolio.objects.filter(category__name=current_category)
    
    
    return render(request, 'home.html', {'categories':categories,'about':about,
        'portfolios':portfolios, 'blogs':blogs, 'form':form, 'form2':form2, 
        'partners':partners, 'social_medias':social_medias,'facts':facts, 'main_info':main_info,
        'home_data':home_data, 'portfolio_categories':portfolio_categories, 'current_category': current_category})

def about(request):
    
    about=About.objects.last()
    
    return render(request, 'about.html', {'about':about})

def products(request):
    categories=Category.objects.all()
    category=request.GET.get('category')
    all_products=Product.objects.all()
    paginator = Paginator(all_products, 3)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)
    if category==None:
        
        if request.method == 'GET':
            name = request.GET.get("search-field")
            name2 = request.GET.get("field-name")
            if name is not None:
                products = Product.objects.all().filter(Q(name__icontains=name))
            if name2 is not None:
                products = Product.objects.all().filter(Q(name__icontains=name2))
        if 'min' in request.GET and 'max' in request.GET:
            
            min_price = request.GET.get('min')
            max_price = request.GET.get('max')
            if min_price =='':
                min_price=0
            if max_price =='':
                max_price=Product.objects.aggregate(Max('price'))['price__max']
            products = Product.objects.all().filter( Q(is_discounted=True, new_price__gte=min_price, new_price__lte=max_price, new_price__isnull=False) | Q(is_discounted=False, price__gte=min_price, price__lte=max_price))
            print(products)  
    else:
        products=Product.objects.filter(category__name=category)

    return render(request, 'products.html', {'products':products,
        'categories': categories })

def product_detail(request, slug):
    form=ApplyForm()
    product=Product.objects.get(slug=slug)
    print(product.images.all())
    similar_products=Product.objects.filter(category=product.category)
    
    if request.method == 'POST':
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        form = Apply(product=product,name=name, email=email, phone=phone_number)
        form.save()
        form=ApplyForm()
    return render(request, 'product-detail.html', 
            {'product':product, 'similar_products':similar_products, 'form':form})
 

def blog(request):
    all_blogs=Blog.objects.all()
    paginator = Paginator(all_blogs, 2)
    page_number = request.GET.get('page', 1)
    blogs = paginator.page(page_number)
    return render(request, 'blog.html', {'blogs':blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog-detail.html', {'blog':blog})

def contact(request):
    map=Map.objects.last()
    main_info=Main.objects.last()
    if request.method=='POST':
        form=ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ContactForm()
    return render(request, 'contact.html', {'form':form, 'map':map,
            'main_info':main_info})

