from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Comment

# Create your views here.

class PostListView(ListView):
	model = Post
	template_name = 'writersapp/index.html'

class PostDetailView(DeleteView):
	pass

class PostCreateView(CreateView):
	pass

class PostUpdateView(UpdateView):
	pass

class PostDeleteView(DeleteView):
	pass
