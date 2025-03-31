import uuid
import os
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddPostForm, UploadFileForm
from .models import Women, Category, TagPost, UploadFiles
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

cats_db = [
    {'id': 1, 'name': 'Actors'},
    {'id': 2, 'name': 'Singers'},
    {'id': 3, 'name': 'Sportsmen'},
]

def index(request):
    posts = Women.published.all().select_related('cat').order_by('-time_create')
    data = {
        'title': 'Main Page',
        'posts': posts,
        'menu': menu,
        'cat_selected': 0,
    }
    return render(request, 'learning_logs/index-learn.html', context=data)

# def handle_upload_file(f):
#     ext = os.path.splitext(f.name)[-1]
#     unique_filename = f"{uuid.uuid4()}{ext}"
#     save_path = os.path.join("learning_log/uploads/", unique_filename)
#     with open(save_path, "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_upload_file(form.cleaned_data['file'])
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
        # handle_upload_file(request.FILES['file_upload'])
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         # handle_upload_file(form.cleaned_data['file'])
    #         fp = UploadFiles(file=form.cleaned_data['file'])
    #         fp.save()
    # else:
    #     form = UploadFileForm()
    #
    return render(request, 'learning_logs/about-learn.html',
                  {'title': 'about Site', 'menu': menu, 'form': form})


def addpage(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # # print(form.cleaned_data)
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect('home ')
            # except:
            #     form.add_error(None, "Ошибка Добавления поста")
            return redirect('home')
    else:
        form = AddPostForm()

    date = {
        'menu': menu,
        'title': 'Adding new page',
        'form': form,
    }
    return render(request, 'learning_logs/addpage.html', date)

def contact(request):
    return HttpResponse("Returning call")

def login(request):
    return HttpResponse("Autorization")

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')
    data = {
        'title': f'Category: {category.name}',
        'posts': posts,
        'menu': menu,
        'cat_selected': category.pk
    }
    return render(request, 'learning_logs/index-learn.html', context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'post': post,
        'menu': menu,
        'cat_selected': 1,
    }

    return render(request, 'learning_logs/post.html', data)


def show_tag_by_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=1).select_related('cat')
    data = {
        'title': f'Tag: {tag.tag}',
        'posts': posts,
        'menu': menu,
        'cat_selected': None,
    }

    return render(request, 'learning_logs/index-learn.html', context=data)




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