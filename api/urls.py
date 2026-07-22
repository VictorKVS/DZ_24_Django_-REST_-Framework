from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    CategoryDetailView,
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Категории
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('categories/<int:pk>/detail/', CategoryDetailView.as_view(), name='category-detail-books'),

    # Книги
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]
