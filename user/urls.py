from django.urls import path
from .views import UserSignupView, LoginForm, logout_view, UserEditView

app_name = 'user'

urlpatterns = [
    path('login/', LoginForm.as_view(), name='login'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('<int:pk>/edit/', UserEditView.as_view(), name='edit'),
    path('logout/', logout_view, name='logout'),
]
