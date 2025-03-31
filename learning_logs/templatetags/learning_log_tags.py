from django import template
import learning_logs.views as views
from learning_logs.models import Category, TagPost
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('learning_logs/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count('posts')).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('learning_logs/list_tags.html')
def show_all_tags():
    tags = TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0)
    return {'tags': tags}


