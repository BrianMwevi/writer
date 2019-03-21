from django.shortcuts import render
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

class PostListView(ListView):
	login_required = 'home'
	model = Post
	template_name = 'writersapp/index.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		all_post = Post.objects.all()
		context["rand_post"] = all_post.filter(pub_date__isnull=False).order_by("-pub_date")[:3]
		context["all_post"] = all_post.filter(pub_date__isnull=False).order_by("-pub_date")[3:]
		if self.request.user.is_authenticated:
			context["user_pub_posts"] = all_post.filter(author__exact=self.request.user, pub_date__isnull=False).order_by("-pub_date")
			context["user_draft"] = all_post.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")			
		return context

class DraftListView(LoginRequiredMixin, ListView):
	login_required = 'home'
	template_name = 'writersapp/draft_list.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["user_pub_posts"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False)
		context["user_draft"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")
		context['latest_post'] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False).order_by('-created_date')[:3]
		return context
	def get_queryset(self):
		return Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")

class PostDetailView(LoginRequiredMixin, DetailView):
	login_required = 'home'
	login_url = "accounts:register"
	model = Post
	template_name = 'writersapp/post_detail.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["user_pub_posts"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=False)
		context["user_draft"] = Post.objects.filter(author__exact=self.request.user, pub_date__isnull=True).order_by("-created_date")
		context["comment_form"] = CommentForm
		return context


class PostCreateView(LoginRequiredMixin, CreateView):
	login_required = 'home'
	model = Post
	fields = ['title', 'detail']
	template_name = 'writersapp/post_create.html'

	def form_valid(self, form):
		form.instance.author = self.request.user 
		form.instance.draft = True
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
	login_required = 'home'
	model = Post
	fields = ['title', 'detail']
	template_name = 'writersapp/post_update.html'

class PostPublishView(LoginRequiredMixin, UpdateView):
	# login_required = 'home'
	model = Post
	fields = ['title', 'detail']
	template_name = 'writersapp/post_detail.html'

	def form_valid(self,form):
		
		form.instance.pub_date = timezone.now()
		form.instance.draft = False
		return super().form_valid(form)
class PostPublishedview(ListView):
	# login_required = 'home'
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

class CommentView(LoginRequiredMixin, CreateView):
	login_url = "accounts:registration"
	model = Comment
	form_class = CommentForm
	template_name = 'writersapp/post_detail.html'

	# def form_valid(self,form):
	# 	form.instance.post = '1'
	# 	return super().form_valid(form)

	def get_object(self, pk, **kwargs):
		print(self.request.user.get_full_name)
		print(pk)


