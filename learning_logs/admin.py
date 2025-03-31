from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Women, Category

class MariedFilter(admin.SimpleListFilter):
    title = "Статус женщины"
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        if self.value() == 'single':
            return queryset.filter(husband__isnull=True)



@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'husband', 'tags']
    # exclude = ['tags', 'is_published']
    readonly_fields = ['post_photo']
    prepopulated_fields = {'slug': ('title', )}
    filter_vertical = ['tags']
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    ordering = ['-time_create', 'title']
    list_editable = ['is_published']
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name', 'is_published']
    save_on_top = True

    @admin.display(description="Изображение", ordering='content')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50>")
        return "Без Фото"

    @admin.action(description="Опубликовать записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=1)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Снять записи с публикации")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=0)
        self.message_user(request, f"{count} записей снято с публикации", messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


# Register your models here.
# from .models import Topic, Entry
#
# admin.site.register(Topic)
# admin.site.register(Entry)

