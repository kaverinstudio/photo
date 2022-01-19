from django.urls import path
from .views import ProductsViewsDetail, ProductsViewsList, ProductViewsCategory


app_name = 'shop'

urlpatterns = [
    path('product/', ProductsViewsList.as_view(), name='product'),
    path('product/<int:id>', ProductsViewsDetail.as_view(), name='detail'),
    path('product/<category>', ProductViewsCategory.as_view(), name='category'),
]
