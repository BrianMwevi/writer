from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Comment
from .forms import PostForm

# Create your views here.

class PostListView(ListView):
	model = Post
	template_name = 'writersapp/index.html'

class PostDetailView(DeleteView):
	model = Post
	template_name = 'writersapp/post_detail.html'


class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'detail']
	template_name = 'writersapp/post_create.html'

	def form_valid(self, form):
		form.instance.author = self.request.user 
		return super().form_valid(form)

class PostUpdateView(UpdateView):
	pass

class PostDeleteView(DeleteView):
	pass

# class ChangePassView(UpdateView):
# 	model = 
