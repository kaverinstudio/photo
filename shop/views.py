from django.shortcuts import render
from django.views.generic.base import View
from .models import ShopCardModel, ShopCardPhotos


class ProductsViewsList(View):
    def get(self, request):
        cat = ShopCardModel.objects.all()
        products = ShopCardModel.objects.all()
        photos = []
        for i in products:
            photos.append(ShopCardPhotos.objects.filter(show_id=i.id).first())
        context = {
            'products': products,
            'category': cat,
            'products_photos': photos
        }
        return render(request, 'shop/shop-page.html', context)


class ProductsViewsDetail(View):
    def get(self, request, id):
        product = ShopCardModel.objects.all().filter(id=id)
        photo = ShopCardPhotos.objects.all()
        first_photo = ShopCardPhotos.objects.filter(show_id=id).first()
        context = {
            'product': product,
            'product_photo': photo,
            'first_photo': first_photo
        }
        return render(request, 'shop/shop-page-detail.html', context)


class ProductViewsCategory(View):
    def get(self, request, category):
        products = ShopCardModel.objects.all().filter(category=category)
        cat = ShopCardModel.objects.all()
        photos = []
        for i in products:
            photos.append(ShopCardPhotos.objects.filter(show_id=i.id).first())
        context = {
            'products': products,
            'category': cat,
            'products_photos': photos
        }
        return render(request, 'shop/shop-page.html', context)
