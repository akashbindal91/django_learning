"""mysite_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

from blog import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # as_view() : since all views are class based views

    # path('', views.PostListView.as_view(), name='post_list'),
    path('about/',  views.AboutView.as_view(), name='about'),
    path('post/<int:pk>' , views.PostDetailView.as_view()  ,name='post_detail'),
    path('post/create/' , views.CreatePostView.as_view()  ,name='post_create'),
    path('post/<int:pk>/update/' , views.PostUpdateView.as_view()  ,name='post_update'),
    path('post/<int:pk>/delete/' , views.PostDeleteView.as_view()  ,name='post_delete'),
    path('post/draft/' , views.DraftListView.as_view()  ,name='post_draft_list'),
]
