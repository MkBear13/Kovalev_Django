"""
URL configuration for friender project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import  include, path
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views
from rest_framework.authtoken import views
from . import settings

from .views import (
    # some_view,
    # MyView,
    # some_template_view,
    Home_view,
    hotels_view,
    Users_view,
    user_comment_view,
    book_room,
    UserDetailView,
    Create_user,
    HotelCommentFormView,
    compute_factorial,
    create_profile,
    # persons_view,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('venues/', views.venues, name='venues'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('home/', Home_view.as_view(), name="home"),
    path('hotels', hotels_view, name="hotels"),
    path('users', login_required(Users_view.as_view()), name="users"),
    path('user_comment', user_comment_view, name="user_comment"),
    path('book/<str:hotel_name>/<int:user_id>/<str:room_number>/',  book_room, name='book_room'),
    path('create_user/', Create_user.as_view(), name='create_user'),
    path('comment_add', HotelCommentFormView.as_view(), name="comment_add"),
    path('user/<int:id>', UserDetailView.as_view(), name='user-detail'),
    path('create_profile', create_profile, name="profile_add"),
    path('api/', include("friender_api.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('factorial/<int:number>', compute_factorial, name='factorial'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)