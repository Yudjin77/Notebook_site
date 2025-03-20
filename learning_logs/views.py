from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse

def index(request):
    return HttpResponse('The Page of app learning_logs')

def categories(request, cat_id):
    if cat_id % 2 == 1:
        raise Http404()
    return HttpResponse(f'<h1>Posts of Categories by ID</h2><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Posts of Categories by Slug</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2025:
        uri = reverse('cats_id', args=('1234', ))
        return redirect(uri)
    return HttpResponse(f"<h1>Page from archive</h1><p>year: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")


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