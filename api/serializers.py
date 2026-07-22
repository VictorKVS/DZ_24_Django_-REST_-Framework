from rest_framework import serializers
from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    """Простой сериализатор категории (без вложенных книг).
    Используется внутри BookSerializer, чтобы избежать циклических ссылок."""
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class BookSerializer(serializers.ModelSerializer):
    """Сериализатор книги. Категория выводится как вложенный объект."""
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'category', 'category_id']


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Сериализатор категории с вложенным списком книг.
    Именно он используется в новом эндпоинте /categories/<pk>/detail/."""
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'books']
