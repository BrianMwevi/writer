from django.urls import path 

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, DraftListView, PostPublishView,PostPublishedview

app_name = "writersapp"

urlpatterns = [
	# path('', PostDetailView.as_view(), name='post_list'),
	path('detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('create/', PostCreateView.as_view(), name='post_create'),
	path('drafts/', DraftListView.as_view(), name='drafts'),
	path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
	path('publish/<int:pk>/', PostPublishView.as_view(), name='post_publish'),
	path('published/list/', PostPublishedview.as_view(), name='published'),
	path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
