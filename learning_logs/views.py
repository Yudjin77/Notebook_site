from django.shortcuts import render, redirect
# from .models import Topic, Entry
# from .forms import TopicForm, EntryForm
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = [
    {"title":"About us", "url_name": "about"},
    {"title":"Add post", "url_name": "addpage"},
    {"title":"Returning call", "url_name": "contact"},
    {"title":"Enter", "url_name": "login"}
]

data_db = [
    {'id': 1, 'title': "Margo", 'content':'''<h1>Margot Elise Robbie</h1> was born on July 2, 1990 in Dalby, Queensland, Australia to Scottish parents. 
    Her mother, Sarie Kessler, is a physiotherapist, and her father, is Doug Robbie. 
    She comes from a family of four children, having two brothers and one sister.''', 'is_published': True},
    {'id': 2, 'title': "David", 'content': "Rich billioner", 'is_published': True},
    {'id': 3, 'title': "Rick", 'content': "Best of the best", 'is_published': True}
]

cats_db = [
    {'id': 1, 'name': 'Actors'},
    {'id': 2, 'name': 'Singers'},
    {'id': 3, 'name': 'Sportsmen'},
]

def index(request):
    data = {
        'title': 'Main Page',
        'posts': data_db,
        'menu': menu,
        'cat_selected': 0,
    }
    return render(request, 'learning_logs/index-learn.html', context=data)

def about(request):
    return render(request, 'learning_logs/about-learn.html', {'title': 'about Site', 'menu': menu})

def addpage(request):
    return HttpResponse("Adding of post")

def contact(request):
    return HttpResponse("Returning call")

def login(request):
    return HttpResponse("Autorization")

def show_category(request, cat_id):
    data = {
        'title': 'View  by Category',
        'posts': data_db,
        'menu': menu,
        'cat_selected': cat_id,
    }
    return render(request, 'learning_logs/index-learn.html', context=data)


def show_post(request, post_id):
    return HttpResponse(f'Show of page with id = {post_id}')


# Create your views here.
# def index(request):
#     return render(request, 'learning_logs/index.html')
#
# def topics(request):
#     topics = Topic.objects.order_by('date_add')
#     context = {'topics': topics}
#     return render(request, 'learning_logs/topics.html', context)
#
# def topic(request, topic_id):
#     topic = Topic.objects.get(id=topic_id)
#     entries = topic.entry_set.order_by('-date_added')
#     context = {'topic': topic, 'entries': entries}
#     return render(request, 'learning_logs/topic.html', context)
#
# def new_topic(request):
#     '''defining a new topic'''
#     if request.method != 'POST':
#         form = TopicForm()
#     else:
#         form = TopicForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('learning_logs:topics')
#
#     #Returning empty form
#     context = {'form': form}
#     return render(request, 'learning_logs/new_topic.html', context)
#
# def new_entry(request, topic_id):
#     '''definding a new entry'''
#     topic = Topic.objects.get(id=topic_id)
#     if request.method != 'POST':
#         form = EntryForm()
#     else:
#         form = EntryForm(data=request.POST)
#         if form.is_valid():
#             new_entry = form.save(commit=False)
#             new_entry.topic = topic
#             new_entry.save()
#             return redirect('learning_logs:topic', topic_id=topic_id)
#
#     # Returning empty form
#     context = {'form': form, 'topic': topic}
#     return render(request, 'learning_logs/new_entry.html', context)
#
# def edit_entry(request, entry_id):
#     '''Redacting current entry'''
#     entry = Entry.objects.get(id=entry_id)
#     topic = entry.topic
#     if request.method != "POST":
#         form = EntryForm(instance=entry)
#     else:
#         form = EntryForm(instance=entry, data=request.POST)
#         form.save()
#         return redirect('learning_logs:topic', topic_id=topic.id)
#
#     context = {'entry': entry, 'topic': topic, 'form': form}
#     return render(request, 'learning_logs/edit_entry.html', context)
#