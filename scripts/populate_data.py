import os
import sys
import django

# Добавляем корень проекта в sys.path, чтобы Python мог найти модуль 'config'
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from api.models import Category, Book
from datetime import date

print("🗑️ Очищаем старые данные...")
Book.objects.all().delete()
Category.objects.all().delete()

print("\n📚 Создаем категории...")
cat1 = Category.objects.create(
    name='Фантастика',
    description='Книги жанра фантастика'
)
cat2 = Category.objects.create(
    name='Классика',
    description='Классическая литература'
)
cat3 = Category.objects.create(
    name='Программирование',
    description='Книги по программированию и IT'
)

print(f"✅ Создано категорий: {Category.objects.count()}")

print("\n📖 Создаем книги...")
Book.objects.create(
    title='Дюна',
    author='Фрэнк Герберт',
    published_date=date(1965, 8, 1),
    category=cat1
)
Book.objects.create(
    title='1984',
    author='Джордж Оруэлл',
    published_date=date(1949, 6, 8),
    category=cat1
)
Book.objects.create(
    title='Война и мир',
    author='Лев Толстой',
    published_date=date(1869, 1, 1),
    category=cat2
)
Book.objects.create(
    title='Python для начинающих',
    author='Марк Лутц',
    published_date=date(2013, 7, 1),
    category=cat3
)

print(f"✅ Создано книг: {Book.objects.count()}")
print("\n🎉 База данных готова для тестирования!")
