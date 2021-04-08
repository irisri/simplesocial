from django.conf.urls import url
# Django has a login and logout view
from django.contrib.auth import views as auto_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # Connect to the template name
    url('login/', auto_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # Django has a defalt view
    url('logout/', auto_views.LogoutView.as_view(), name='logout'),
    # Already connected in the views.py
    url('signup/', views.SignUp.as_view(), name="signup"),

]