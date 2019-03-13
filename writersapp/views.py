from django.shortcuts import render
from django.utils import timezone

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Comment
from .forms import PostForm

# Create your views here.

class PostListView(ListView):
	model = Post
	template_name = 'writersapp/index.html'
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context["user_pub_posts"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False)
	    context["user_draft"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")
	    return context

class DraftListView(ListView):
	template_name = 'writersapp/draft_list.html'
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context["user_pub_posts"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False)
	    context["user_draft"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")
	    return context
	def get_queryset(self):
		return Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")

class PostDetailView(DetailView):
	model = Post
	template_name = 'writersapp/post_detail.html'
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context["user_pub_posts"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False)
	    context["user_draft"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")
	    return context


class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'detail']
	template_name = 'writersapp/post_create.html'

	def form_valid(self, form):
		form.instance.author = self.request.user 
		return super().form_valid(form)

class PostUpdateView(UpdateView):
	model = Post
	fields = ['title', 'detail']
	template_name = 'writersapp/post_update.html'

class PostPublishView(UpdateView):
	model = Post
	fields = ['title', 'detail']
	template_name = 'writersapp/post_detail.html'

	def form_valid(self, form):
		form.instance.pub_date = timezone.now()
		return super().form_valid(form)
class PostPublishedview(ListView):
	def get_queryset(self, **kwargs):
		return Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False)
	template_name = 'writersapp/published_list.html'
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context["user_pub_posts"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False)
	    context["user_draft"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")
	    return context



class PostDeleteView(DeleteView):
	pass

# class ChangePassView(UpdateView):
# 	model = 
