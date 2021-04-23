"""cvfeed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from post import views as post_views
from feed import views as feed_views
from users import views as user_views

urlpatterns = [
    path('', feed_views.index_feed),
    path('user/<slug:username>/', feed_views.user_feed),
    path('tag/<slug:tag>/', feed_views.tag_feed),
    path('search/', feed_views.search),
    path('reports/', feed_views.reports_feed),
    path('reports/<int:post_id>/', feed_views.report_post),
    path('reports/remove/', feed_views.remove_post),
    path('post/', post_views.new_post),
    path('post/<int:post_id>/', post_views.view_post),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', user_views.register, name='register'),
    path('admin/', admin.site.urls),
]
