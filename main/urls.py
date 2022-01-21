from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('servises/', views.servises, name='servises'),
    path('order/', views.BasicUploadView.as_view(), name='order'),
    path('<int:id>/delete/', views.delete_photo, name='delete'),
    path('order/confirm/', views.edit_upload_form, name='confirm'),
    path('complite/', views.OrderComplite.as_view(), name='complite'),
    path('added-order/', views.confirm_order, name='added-order'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
