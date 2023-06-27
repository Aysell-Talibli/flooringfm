from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ( 'text', )


@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('footer_text', )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(PortfolioCategory)
class PortfolioCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Slider)
class HomeTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


@register(HomeContact)
class HomeContactTranslationOptions(TranslationOptions):
    fields = ('title', 'text')