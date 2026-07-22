from rest_framework import generics
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Book, Category
from .serializers import (
    BookSerializer,
    CategorySerializer,
    CategoryDetailSerializer
)


# ==========================================
# Представления для категорий
# ==========================================

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """Список всех категорий или создание новой категории."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Получение, обновление или удаление категории по ID."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


@extend_schema_view(
    get=extend_schema(
        summary="Детальная категория с книгами",
        description="Получение категории с вложенными данными (книги в категории). "
                    "Использует prefetch_related для оптимизации запросов к БД."
    )
)
class CategoryDetailView(generics.RetrieveAPIView):
    """
    Детальное отображение категории с вложенным списком книг.
    Использует CategoryDetailSerializer для вложенного вывода.
    """
    queryset = Category.objects.prefetch_related('books')
    serializer_class = CategoryDetailSerializer
    permission_classes = [AllowAny]


# ==========================================
# Представления для книг
# ==========================================

class BookListCreateAPIView(generics.ListCreateAPIView):
    """Список всех книг или создание новой книги."""
    queryset = Book.objects.select_related('category').all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Получение, обновление или удаление книги по ID."""
    queryset = Book.objects.select_related('category').all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
