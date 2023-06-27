from django.db import models

from ckeditor.fields import RichTextField

class Blog(models.Model):
    slug = models.SlugField(null=True, unique=True)
    title=models.CharField(max_length=100)
    text=models.TextField()
    image=models.ImageField()

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=100, default='Others')
    image=models.ImageField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    slug = models.SlugField(null=True, unique=True)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description=RichTextField(verbose_name="Mehsul haqqinda etrafli melumat")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_discounted=models.BooleanField(default=False)
    new_price=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    code=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    @property
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', kwargs={'slug': self.slug})
    
class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='images' )
    image=models.ImageField()

    def __str__(self):
        return self.product.name
    
class About(models.Model):
    image=models.ImageField()
    text=models.TextField()

    def __str__(self):
        return self.text

class Contact(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    message=models.TextField()

    def __str__(self):
        return f'{self.name, self.surname}'
    
class Apply(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.product.name
 
class PortfolioCategory(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    category=models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='portfolios')
    name=models.CharField(max_length=100)
    image=models.ImageField()

    def __str__(self):
        return self.name

class Partner(models.Model):
    image=models.ImageField()

class Map(models.Model):
    link=models.URLField(max_length=500)


class SocialMedia(models.Model):
    class SocialChoices(models.TextChoices):
        INSTAGRAM = "insta", "Instagram"
        FACEBOOK = "fb", "Facebook"
        TIKTOK = "tiktok", "Tiktok"
        WHATSAPP = "wp", "Whatsapp"
        LINKEDIN = "linkedin", "Linkedin"
        TWITTER = "twitter", "Twitter"
    app=models.CharField(max_length=110, choices=SocialChoices.choices)
    link=models.TextField(null=True)
    def __str__(self):
        return self.app

class Main(models.Model):
    phone=models.CharField(max_length=50, null=True)
    address=models.CharField(max_length=50, null=True)
    email=models.EmailField(null=True)
    footer_text=models.TextField(null=True)
    footer_logo=models.ImageField(null=True)
    header_logo=models.ImageField(null=True)
    home_logo=models.ImageField(null=True)

class Slider(models.Model):
    title=models.CharField(max_length=50)
    text=models.CharField(max_length=80)
    image=models.ImageField()
    def __str__(self):
        return self.title

class HomeContact(models.Model):
    title=models.CharField(max_length=50)
    text=models.CharField(max_length=80)

    def __str__(self):
        return self.title

class HomeApply(models.Model):
    name=models.CharField(max_length=70)
    surname=models.CharField(max_length=70)
    message=models.TextField()
    
    def __str__(self):
        return f'{self.name, self.surname}'
    
class EmailName(models.Model):
    subscription_email=models.EmailField()

    def __str__(self):
        return self.subscription_email

class FunFact(models.Model):
    name=models.CharField(max_length=70, null=True)
    count=models.IntegerField()
    def __str__(self):
        return self.name

class BackgroundImage(models.Model):
    about=models.ImageField(null=True)
    products=models.ImageField(null=True)
    blogs=models.ImageField(null=True)
    contact=models.ImageField(null=True)