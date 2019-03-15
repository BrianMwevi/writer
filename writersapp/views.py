from django.shortcuts import render
from django.utils import timezone

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Comment
from .forms import PostForm

# Create your views here.

class PostListView(PermissionRequiredMixin, ListView):
	permission_required = 'home'
	model = Post
	template_name = 'writersapp/index.html'
	def get_context_data(self, **kwargs):
		all_post = Post.objects.all()
		context = super().get_context_data(**kwargs)
		context["user_pub_posts"] = all_post.filter(author__exact=self.request.user, pub_date__isnull=False)
		context["user_draft"] = all_post.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")
		context["rand_post"] = all_post.filter(pub_date__isnull=False).order_by("-pub_date")[:3]
		context["all_post"] = all_post.filter(pub_date__isnull=False).order_by("-pub_date")[3:]
	
		return context

class DraftListView(PermissionRequiredMixin, ListView):
	permission_required = 'home'
	template_name = 'writersapp/draft_list.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["user_pub_posts"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False)
		context["user_draft"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")
		context['latest_post'] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False).order_by('-created_date')[:3]
		return context
	def get_queryset(self):
		return Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")

class PostDetailView(PermissionRequiredMixin, DetailView):
	permission_required = 'home'
	model = Post
	template_name = 'writersapp/post_detail.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["user_pub_posts"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False)
		context["user_draft"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")
		return context


class PostCreateView(PermissionRequiredMixin, CreateView):
	permission_required = 'home'
	model = Post
	fields = ['title', 'detail']
	template_name = 'writersapp/post_create.html'

	def form_valid(self, form):
		form.instance.author = self.request.user 
		return super().form_valid(form)

class PostUpdateView(PermissionRequiredMixin, UpdateView):
	permission_required = 'home'
	model = Post
	fields = ['title', 'detail']
	template_name = 'writersapp/post_update.html'

class PostPublishView(PermissionRequiredMixin, UpdateView):
	permission_required = 'home'
	model = Post
	fields = ['title', 'detail']
	template_name = 'writersapp/post_detail.html'

	def form_valid(self, form):
		form.instance.pub_date = timezone.now()
		return super().form_valid(form)
class PostPublishedview(PermissionRequiredMixin, ListView):
	permission_required = 'home'
	def get_queryset(self, **kwargs):
		return Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False)
	template_name = 'writersapp/published_list.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["user_pub_posts"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False).order_by("-pub_date")
		context["user_draft"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")
		return context



class PostDeleteView(DeleteView):
	pass

# class ChangePassView(UpdateView):
#   model = 
