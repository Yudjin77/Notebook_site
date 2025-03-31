from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.forms import TextInput, Textarea
from django.utils.deconstruct import deconstructible
from .models import Category, Husband, Women, TagPost



@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789-"
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать латинские символы, дефис и пробел"

    def __call__(self, value, *args, **kwargs):
        if not set(value) <= set(self.ALLOWED_CHARS):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='Муж',empty_label='Не замужем')

    tags = forms.ModelMultipleChoiceField(
        queryset=TagPost.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'size': 6}),  # Виджет с множественным выбором
        label="Теги",
    )

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tags', ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-input'}),
            'content': Textarea(attrs={'cols': 50, 'rows': 5}),
            # 'tags': )
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")
        elif len(title) < 5:
            raise ValidationError("Длина должна быть больше 5 символов")
        return title


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')


#
# class TopicForm(forms.ModelForm):
#     class Meta:
#         model = Topic
#         fields = ['text']
#         labels = {'text': 'New Topic Name'}
#
# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = ['text']
#         labels = {'text': 'Entry'}
#         widgets = {'text': forms.Textarea(attrs={'cols': 120})}
#
