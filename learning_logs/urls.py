"""Определяет схемы URL для learning_logs."""

from django.urls import path, re_path, register_converter
from . import views
from . import converters
#
# register_converter(converters.FourDigitYearConverter, "yyyy")
#
# app_name = 'learning_logs'

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_by_postlist, name='tag')







#     path('topics/', views.topics, name='topics'),
#     path('topics/<int:topic_id>/', views.topic, name='topic'),
#     path('new_topic/', views.new_topic, name='new_topic'),
#     path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
#     path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
#     path('tests/', views.tests),
#     path('tests/<int:tests_id>/', views.test_id),
#     path('tests/<slug:tests_slug>/', views.test_slug, name='test'),
#     path('archive/<yyyy:year>/', views.archive)
]
