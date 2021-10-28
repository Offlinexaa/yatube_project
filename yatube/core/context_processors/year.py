"""Процессор контекста year"""
from datetime import date


def year(request):
    """Добавляет в контекст переменную year, содержащую текущий год"""
    return {
        'year': date.today().year,
    }
