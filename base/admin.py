from django.contrib import admin
from .models import *
# Register your models here.


class ImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(PortfolioCategory)
admin.site.register(Portfolio)
admin.site.register(Main)
admin.site.register(SocialMedia)
admin.site.register(ProductImage) 
admin.site.register(Slider)    
admin.site.register(HomeContact)
admin.site.register(Apply)
admin.site.register(FunFact)
admin.site.register(HomeApply)
admin.site.register(EmailName)
admin.site.register(Map)
admin.site.register(BackgroundImage)