from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from .views import index, contato, cadastro


urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('signup/', cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login')
]