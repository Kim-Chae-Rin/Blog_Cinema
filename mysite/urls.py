"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.UserCreateView.as_view(), name='register'),
    path('accounts/register/done', views.UserCreateDoneTV.as_view(), name='register_done'),


    # shkim
    path('', views.HomeView.as_view(), name='home'),

    # 애플리케이션 url 관리를 시작합니다.
    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail')
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),

    path('movie/', views.movieAPI_TV, name='using_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
