from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name = 'books-home' ),
    path('showall/', views.show, name='books-show'),
    path('show/<int:id>', views.showbyid, name='books-showbyid')
]