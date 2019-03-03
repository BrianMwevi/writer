from django.urls import path 

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = "writersapp"

urlpatterns = [
	# path('', PostDetailView.as_view(), name='post_list'),
	path('detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('create/<int:pk>/', PostCreateView.as_view(), name='post_create'),
	path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
	path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
