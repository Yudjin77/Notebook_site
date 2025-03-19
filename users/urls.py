from django.urls import path, include

app_name = 'users'

'''Включение авторизаций по умолчанию'''
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]