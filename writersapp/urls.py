from django.urls import path 

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, DraftListView, PostPublishView

app_name = "writersapp"

urlpatterns = [
	# path('', PostDetailView.as_view(), name='post_list'),
	path('detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('create/', PostCreateView.as_view(), name='post_create'),
	path('drafts/', DraftListView.as_view(), name='drafts'),
	path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
	path('update/<int:pk>/', PostPublishView.as_view(), name='post_publish'),
	path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
