from django.db import models
from django.utils import timezone 
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect


from django.contrib.auth import get_user_model
User = get_user_model()

import misaka

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.TextField(max_length=100)
	detail = models.TextField(default="")
	detail_html = models.TextField(default="")
	created_date = models.DateTimeField(default=timezone.now)
	pub_date = models.DateTimeField(null=True, blank=True)
	draft = models.BooleanField(default=False)


	def save(self, *args, **kwargs):
		self.detail_html = misaka.html(self.detail)
		super().save(args, kwargs)

	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"

	def get_absolute_url(self):
		return reverse_lazy("writersapp:post_detail", kwargs={"pk":self.pk})

	def __str__(self):
		return self.title


class Comment(models.Model):
	writer = models.CharField(max_length=100)
	comment = models.TextField(default="")
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	com_date = models.DateTimeField(default=timezone.now)
	approve = models.BooleanField(default=False)

	def approved(self):
		self.approve = True
		self.save()

	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comments"

	def __str__(self):
		return self.comment

