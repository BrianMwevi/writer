from django.contrib import admin
from django.urls import path, include

from writersapp.views import PostListView

urlpatterns = [
	path('',PostListView.as_view(), name='home'),
	path('', include('writersapp.urls', namespace='writersapp')),
    path('admin/', admin.site.urls),
]
