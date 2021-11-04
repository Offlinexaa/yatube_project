from django import template


register = template.Library()


@register.filter
def addclass(field, css):
    """Добавляет артибут класс в виджет"""
    return field.as_widget(attrs={'class': css})
