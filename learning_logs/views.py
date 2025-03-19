from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_add')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    '''defining a new topic'''
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    #Returning empty form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    '''definding a new entry'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Returning empty form
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    '''Redacting current entry'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        form.save()
        return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

#request это ссылка на django класс HttpResponse которая содержит информации о запросе
def tests(request):
    return HttpResponse("<h1>Тестовая страница из приложения learning_log</h2>")

def test_id(request, tests_id):
    return HttpResponse(f"Страница  с запросом int {tests_id}")

def test_slug(request, tests_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"Страница  с запросом slug {tests_slug}")

def archive(request, year):
    if year > 2023:
        uri = reverse('learning_logs:test', args=('sport', ))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"Архив по годам {year}")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h2>")
