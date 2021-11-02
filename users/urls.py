from users import views as user_views
from django.urls import path
urlpatterns = [
    path('signup/', user_views.signup, name='signup'),
    path('login/', user_views.login, name='login')
    
]