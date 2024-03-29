"""
URL configuration for Django_learn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.global_settings import STATIC_ROOT
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from Django_learn.settings import MEDIA_ROOT
from app_user.views import (SetNewWebEmail, Home, Welcome, LoginView, RegisterView, ActiveUser, LogoutView,
                            FindPassword, ResetPassword)

urlpatterns = [
    re_path('^set-new-web-email/$', SetNewWebEmail.as_view(), name='首次设置邮箱'),  # 首次设置邮箱页面的 URL 模式
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}, name='静态'),
    re_path(r'user/', include(('app_user.urls', 'user'), namespace='user')),
    path('', Home.as_view(), name='主页'),  # 应用程序的主页
    re_path('^Welcome/$', Welcome.as_view(), name='欢迎页面'),  # 欢迎页面
    re_path('^login/$', LoginView.as_view(), name='登录'),  # 登录页面的 URL 模式
    re_path('^register/$', RegisterView.as_view(), name='注册'),  # 注册页面的 URL 模式
    re_path('active/(?P<active_code>.*)/', ActiveUser.as_view(), name='激活账户'),
    re_path('^log-out/$', LogoutView.as_view(), name='退出'),  # 退出登录页面的 URL 模式
    re_path('^find-password/$', FindPassword.as_view(), name='找回密码'),  # 退出登录页面的 URL 模式
    re_path('^password-reset/(?P<reset_code>.*)/', ResetPassword.as_view(), name='重置密码'),
]
