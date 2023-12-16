# myapp/templatetags/myapp_extras.py
from django import template
from django.utils.html import mark_safe

register = template.Library()

@register.filter
def highlight_search(text, search_term):
    if search_term:
        highlighted_text = text.replace(search_term, f'<span class="highlight">{search_term}</span>')
        return mark_safe(highlighted_text)
    return text
