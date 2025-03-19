"""Определяет схемы URL для learning_logs."""

from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "yyyy")

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('tests/', views.tests),
    path('tests/<int:tests_id>/', views.test_id),
    path('tests/<slug:tests_slug>/', views.test_slug, name='test'),
    path('archive/<yyyy:year>/', views.archive)
]
