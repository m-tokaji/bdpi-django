"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from interfata.views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, GenreCreateView, GenreDeleteView, GenreListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/edit/<int:pk>/', BookUpdateView.as_view(), name='book-edit'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('genres/', GenreListView.as_view(), name='genres-list'),
    path('genres/add/', GenreCreateView.as_view(), name='genre-add'),
    path('genres/delete/<int:pk>/', GenreDeleteView.as_view(), name='genre-delete'),
    path('admin/', admin.site.urls),
]
